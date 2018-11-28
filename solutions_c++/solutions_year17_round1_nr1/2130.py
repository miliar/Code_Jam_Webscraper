#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in", "r", stdin);
    char a[50][50];
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int R, C;
        cin >> R >> C;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                cin >> a[r][c];
            }
        } 
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (a[r][c] != '?') {
                    char ch = a[r][c];
                    for (int j = c+1; j < C; ++j) {
                        if (a[r][j] != '?') {
                            break;
                        } else {
                            a[r][j] = ch;
                        }
                    }
                    for (int j = c-1; j >= 0; --j) {
                        if (a[r][j] != '?') {
                            break;
                        } else {
                            a[r][j] = ch;
                        }
                    }
                }
            }
        }
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (a[r][c] != '?') {
                    char ch = a[r][c];
                    for (int i = r+1; i < R; ++i) {
                        if (a[i][c] != '?') {
                            break;
                        } else {
                            a[i][c] = ch;
                        }
                    }
                    for (int i = r-1; i >= 0; --i) {
                        if (a[i][c] != '?') {
                            break;
                        } else {
                            a[i][c] = ch;
                        }
                    }
                }
            }
        }
	cout << "Case #" << t << ": " << endl;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                cout << a[r][c]; 
            }
            cout << endl;
        }

    }
}
