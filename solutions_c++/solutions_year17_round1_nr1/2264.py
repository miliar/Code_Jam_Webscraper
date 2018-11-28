#include <bits/stdc++.h>

using namespace std;

int vis[100][100];

string grid[100];
int R, C;

int cnt(int r1, int c1, int r2, int c2, char& ch) {
    int cnt = 0;
    for(int i = r1 ; i<= r2 ; i++) {
        for(int j = c1 ; j <= c2 ; j++) {
            if(grid[i][j] != '?') {
                cnt ++;
                ch = grid[i][j];
            }
        }
    }
    return cnt;
}

void fillRect(int r, int c) {
    pair<int, int> otherEnd(-1, -1);
    int chosen = '?';
    for(int i = r ;i < R ; i++) {
        for(int j = c ; j < C; j++) {
            char ch;
            if(cnt(r, c, i, j, ch) == 1) {
                auto now = make_pair(i, j);
                if(now > otherEnd) {
                    otherEnd = now;
                    chosen = ch;
                }
            }
        }
    }
    for(int i = r ; i<= otherEnd.first; i++) {
        for(int j = c ;j <= otherEnd.second ;j++) {
            grid[i][j] = chosen;
            vis[i][j] = 1;
        }
    }
}

void solve() {
    memset(vis, 0, sizeof vis);
    cin >> R >> C;
    for(int i = 0 ;i < R ; i++) {
        cin >> grid[i];
    }
    for(int i = 0 ;i < R ; i++) {
        for(int j = 0 ;j < C; j ++) {
            if(!vis[i][j]) {
                fillRect(i, j);
            }
        }
    }
    for(int i = 0 ;i < R ; i++) {
        cout << grid[i] << endl;
    }
}

int main() {
    int test;
    cin >> test;
    for(int t = 1 ; t <= test; t++) {
        cout << "Case #" << t << ":" << endl;
        solve();
    }
    return 0;
}
