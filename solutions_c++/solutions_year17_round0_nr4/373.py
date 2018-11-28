#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

struct Solver {
    int n, m;
    vector<vector<char> > mp;
    vector<vector<char> > org;

    bool xRow[120];
    bool xCol[120];
    
    vector<int> graph[220];
    vector<int> matched;

    Solver() {
        cin >> n >> m;
        mp.assign(n + 1, vector<char>(n + 1, '.'));
        matched.assign(220, -1);
        memset(xRow, 0, sizeof(xRow));
        memset(xCol, 0, sizeof(xCol));
        for (int i = 0; i < m; ++i) {
            char c;
            int a,b;
            cin >> c >> a >> b;
            mp[a][b] = c;
            if (c == 'x' || c == 'o') {
                xRow[a] = true;
                xCol[b] = true;
            }
        }
        org = mp;
    }

    int getCoor1(int r, int c) {
        return r + c;
    }

    int getCoor2(int r, int c) {
        return r - c + n;
    }

    void buildGraph() {
        vector<bool> used1(220, false);
        vector<bool> used2(220, false);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (mp[i][j] == '+' || mp[i][j] == 'o') {
                    used1[getCoor1(i, j)] = true;
                    used2[getCoor2(i, j)] = true;
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (!used1[getCoor1(i, j)] && !used2[getCoor2(i, j)]) {
                    graph[getCoor1(i, j)].push_back(getCoor2(i, j));
                }
            }
        }
    }

    bool recur(int cur, vector<bool> &v) {
        if (v[cur]) {
            return false;
        }
        v[cur] = true;
        for (int next : graph[cur]) {
            if (matched[next] == -1) {
                matched[next] = cur;
                return true;
            }
            
            if (recur(matched[next], v)) {
                matched[next] = cur;
                return true;
            }
        }
        return false;
    }
    
    void match() {
        for (int i = 0; i <= 2 * n; ++i) {
            vector<bool> v(220, false);
            recur(i, v);
        }
        for (int i = 0; i <= 2 * n; ++i) {
            if (matched[i] != -1) {
                int a = matched[i];
                int b = i - n;
                int r = (a + b) / 2;
                int c = a - r;
                if (mp[r][c] == '.') {
                    mp[r][c] = '+';
                } else if (mp[r][c] == 'x') {
                    mp[r][c] = 'o';
                } else {
                    throw "assert 1";
                }
            }
        }
    }

    void fillX() {
        int c = 1;
        for (int r = 1; r <= n; ++r) {
            if (xRow[r]) {
                continue;
            }
            while (xCol[c]) {
                ++c;
            }
            if (mp[r][c] == '.') {
                mp[r][c] = 'x';
            } else if (mp[r][c] == '+') {
                mp[r][c] = 'o';
            } else {
                throw "assert 2";
            }
            ++c;
        }
    }

    
    int getSingleScore(char c) {
        return c == 'o' ? 2 : (c == '+' || c == 'x' ? 1 : 0);
    }

    int getScore(vector<vector<char> > &v) {
        int score = 0;
        for (auto & vv : v) {
            for (auto c : vv) {
                score += getSingleScore(c);
            }
        }
        return score;
    }
    
    void dump(vector<vector<char> > &v) {
        for (int i = 1; i < v.size(); ++i) {
            for (int j = 1; j < v.size(); ++j) {
                cerr << v[i][j];
            }
            cerr << endl;
        }
    }

    void verify2() {
        bool used[4][300] = {0};
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (mp[i][j] == 'x' || mp[i][j] == 'o')  {
                    if (used[0][i] || used[1][j]) {
                        cerr << "x: " << i << ' ' << j << endl; 
                        throw "xxx";
                    }
                    used[0][i] = true;
                    used[1][j] = true;
                }
                if (mp[i][j] == '+' || mp[i][j] == 'o')  {
                    int a = getCoor1(i, j);
                    int b = getCoor2(i, j);
                    if (used[2][a] || used[3][b]) {
                        cerr << "+: " << a << ' ' << b << endl; 
                        throw "+++";
                    }
                    used[2][a] = true;
                    used[3][b] = true;
                }
            }
        }
    }
    
    void solve() {
        buildGraph();
        match();
        fillX();

        int numDiff = 0;
        ostringstream oss;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (mp[i][j] != org[i][j]) {
                    oss << mp[i][j] << ' ' << i << ' ' << j << endl;
                    ++numDiff;
                }
            }
        }
        cout << getScore(mp) << ' ' << numDiff << endl;
        //dump(mp);
        verify2();
        cout << oss.str();
    }
};

int main() {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        Solver solver;
        solver.solve();
    }
}
