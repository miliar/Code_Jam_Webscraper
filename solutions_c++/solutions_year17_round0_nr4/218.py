#include <bits/stdc++.h>
using namespace std;
#define VI vector<int>
const int diagx[5] = {1, 1, -1, -1};
const int diagy[5] = {1, -1, -1, 1};
const int dx[5] = {0, 0, 1, -1};
const int dy[5] = {1, -1, 0, 0};

vector<string> placeCrosses(vector<string> a) {
    int n = a.size();

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j) {
            int have = false;
            for(int dir = 0; dir < 4; ++dir) {
                int x = i, y = j;
                while(x >= 0 and x < n and y >= 0 and y < n) {
                    if(a[x][y] == 'x' or a[x][y] == 'o')
                        have = true;
                    x += dx[dir];
                    y += dy[dir];
                }
            }
            if(not have) {
                a[i][j] = 'x';
            }
        }
    
    return a;
}

bool match(int node, vector<VI> &G, VI &L, VI &R, VI& used) {
    if(used[node])
        return false;

    used[node] = 1;

    for(auto v : G[node]) {
        if(R[v] == -1) {
            L[node] = v;
            R[v] = node;
            return true;
        }
    }

    for(auto v : G[node]) {
        if(match(R[v], G, L, R, used)) {
            L[node] = v;
            R[v] = node;
            return true;
        }
    }

    return false;
}

vector<string> placePluses(vector<string> a) {
    int n = a.size();
        
    vector<string> bad(n, string(n, '.'));

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j) {
            if(a[i][j] == '.' or a[i][j] == 'x')
                continue;
            for(int dir = 0; dir < 4; ++dir) {
                int x = i, y = j;
                while(x >= 0 and x < n and y >= 0 and y < n) {
                    bad[x][y] = '#';
                    x += diagx[dir];
                    y += diagy[dir];
                }
            }
        }
    
    int N = 3 * n + 4;

    vector<VI> G(N);
    vector<int> L(N, -1), R(N, -1), used(N, 0);

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
            if(bad[i][j] == '.') {
                int x = i + j + n;
                int y = i - j + n;
                G[x].push_back(y);
            }
    
    bool changed = false;

    do {
        changed = false;
        used = vector<int> (N, 0);
        for(int i = 0; i < N; ++i)
            if(L[i] == -1 and match(i, G, L, R, used)) {
                changed = true;
            }
    } while(changed);

    for(int i = 0; i < N; ++i) {
        if(L[i] >= 0) {
            int x = (i + L[i] - 2 * n) / 2;
            int y = (i - n - x);
            a[x][y] = '+';
        }
    }
    
    return a;
}

int main() {
    ifstream cin("D.in");
    ofstream cout("D.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        int n; cin >> n;
        int m; cin >> m;
    
        vector<string> a(n, string(n, '.'));

        for(int i = 0; i < m; ++i) {
            char tip; cin >> tip;
            int x, y; cin >> x >> y;
            x--, y--;
            a[x][y] = tip;
        }   
        
        vector<string> b = placeCrosses(a);
        vector<string> c = placePluses(a);
        
        vector<pair<int, int>> pos;
        vector<char> tip;
        
        for(int i = 0; i < n; ++i) 
            for(int j = 0; j < n; ++j) {
                if((a[i][j] == '+' and b[i][j] == 'x') or (a[i][j] == 'x' and c[i][j] == '+')) {
                    a[i][j] = 'o';
                    pos.push_back(make_pair(i, j));
                    tip.push_back('o');
                } else if(a[i][j] == '.' and b[i][j] == 'x' and c[i][j] == '+') {
                    a[i][j] = 'o';
                    pos.push_back(make_pair(i, j));
                    tip.push_back('o');
                } else if(a[i][j] == '.' and c[i][j] == '+') {
                    a[i][j] = '+';
                    pos.push_back(make_pair(i, j));
                    tip.push_back('+');
                } else if(a[i][j] == '.' and b[i][j] == 'x') {
                    a[i][j] = 'x';
                    pos.push_back(make_pair(i, j));
                    tip.push_back('x');
                }
            }

        int score = 0;

        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                if(a[i][j] == 'o') {
                    score += 2;
                } else if(a[i][j] != '.') {
                    score += 1;
                }

        cout << score << " " << pos.size() << "\n";

        for(int i = 0; i < int(pos.size()); ++i)
            cout << tip[i] << " " << pos[i].first + 1 << " " << pos[i].second + 1 << "\n";
    }
}
