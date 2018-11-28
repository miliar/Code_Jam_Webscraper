#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

char grid[105][105];
int n;

void clear_grid() {
    for (int i = 0; i < 105; i++) {
        for (int j = 0; j < 105; j++) {
            grid[i][j] = '.';
        }
    }
}

bool can_add_x(int r, int c) {
    for (int i = 1; i <= n; i++) {
        if (i != c && grid[r][i] != '.' && grid[r][i] != '+')
            return false;
        if (i != r && grid[i][c] != '.' && grid[i][c] != '+')
            return false;
    }
    return true;
}

bool can_add_plus(int r, int c) {
    int i,j;
    if (r - c < 0) {
        i = 1;
        j = i - r + c;
    } else {
        j = 1;
        i = r - c + j;
    }
    while (i <= n && j <= n) {
        // if (r == 1 && c == 1)
            // cout << i << ' ' << j << endl;
        if (i != r && grid[i][j] != '.' && grid[i][j] != 'x') {
            if (r == 1 && c == 1) 
                cout << "fuck " << i << ' ' << j << endl;
            return false;
        }
        i++; j++;
    }
    if (r + c > n) {
        j = n;
        i = r + c - j;
    } else {
        i = 1;
        j = r + c - i;
    }
    while (i <= n && c >= 1) {
        // if (r == 1 && c == 1)
            // cout << i << ' ' << j << endl;
        if (i != r && grid[i][j] != '.' && grid[i][j] != 'x') {
            if (r == 1 && c == 1)
                cout << "shit " << i << ' ' << j << endl;
            return false;
        }
        i++; j--;
    }
    return true;
}

void print_grid() {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << grid[i][j];
        }
        cout << endl;
    }
}

int main() {
    ifstream cin ("in.txt");
    ofstream cout ("out.txt");
    map<char, int> score;
    score['.'] = 0;
    score['x'] = score['+'] = 1;
    score['o'] = 2;

    int T;
    int m;
    cin >> T;
    set<pair<int,int>> v;
    for (int cs = 1; cs <= T; cs++) {
        char ch;
        int r,c;
        clear_grid();
        v.clear();
        cin >> n >> m;
        for (int i = 0; i < m; i++) {
            cin >> ch >> r >> c;
            grid[r][c] = ch;
        }
        for (int i = 1; i <= 1; i++) {
            for (int j = 1; j <= n; j++) {            
                ch = grid[i][j];
                if (ch != '.') continue;
                bool plus = can_add_plus(i, j);
                if (plus) {
                    grid[i][j] = '+';
                    v.insert(make_pair(i, j));
                }
            }
        }
        for (int i = n; i <= n; i++) {
            for (int j = 1; j <= n; j++) {                
                ch = grid[i][j];
                if (ch != '.') continue;
                bool plus = can_add_plus(i, j);
                if (plus) {
                    grid[i][j] = '+';
                    v.insert(make_pair(i, j));
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j<= n; j++) {
                ch = grid[i][j];
                if (ch == 'o') continue;
                bool plus = can_add_plus(i, j);
                bool cross = can_add_x(i, j);
                // cout << i << ' ' << j << ' ' << plus << ' ' << cross << endl;
                if (plus && cross && ch != 'o') {
                    grid[i][j] = 'o';
                    v.insert(make_pair(i, j));
                } else if (cross && ch == '.') {
                    grid[i][j] = 'x';
                    v.insert(make_pair(i, j));
                }
            }
        }
        int total_score = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                total_score += score[grid[i][j]];
            }
        }        
        cout << "Case #" << cs << ": " << total_score << ' ' << v.size() << endl;
        for (auto it = v.begin(); it != v.end(); it++) {
            int r = it->first, c = it->second;
            cout << grid[r][c] << ' ' << r << ' ' << c << endl;
        }
        // for (int i = 1; i <= n; i++) {
        //     for (int j = 1; j <= n; j++) {
        //         cout << grid[i][j];
        //     }
        //     cout << endl;
        // }
        if (n >= 3 && total_score != 3*n - 2) {
            cout << "FUCKKKK" << endl;
            exit(0);
        }
    }
}