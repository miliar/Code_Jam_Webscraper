#include <iostream>
#include <string>
using namespace std;

int main() {
    int t, n, m, vis[50][50];
    char a[50][50];
    string s;
    cin >> t;
    for (int ti=0; ti<t; ti++) {
        cin >> n >> m;
        for (int i=0; i<n; i++) {
            cin >> s;
            for (int j=0; j<m; j++) {
                a[i][j] = s[j];
                if (a[i][j] != '?') {
                    vis[i][j] = 1;
                } else {
                    vis[i][j] = 0;
                }
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (vis[i][j] == 1) {
                    int x, y, x1, x2;
                    x = i+1; y = j;
                    while (x < n and a[x][y] == '?') {
                        a[x][y] = a[i][j];
                        x++;
                    }
                    x1 = x-1;

                    x = i-1; y = j;
                    while (x >=0 and a[x][y] == '?') {
                        a[x][y] = a[i][j];
                        x--;
                    }
                    x2 = x+1;

                    y = j-1;
                    while (y >= 0){
                        int flag = 0;
                        for (int k=x2; k<=x1; k++) {
                            if (a[k][y] != '?') {
                                flag = 1;
                            }
                        }
                        if (flag == 0) {
                            for (int k=x2; k<=x1; k++) {
                                a[k][y] = a[i][j];
                            }
                        } else {
                            break;
                        }
                        y--;
                    }

                    y = j+1;
                    while (y <= m-1){
                        int flag = 0;
                        for (int k=x2; k<=x1; k++) {
                            if (a[k][y] != '?') {
                                flag = 1;
                            }
                        }
                        if (flag == 0) {
                            for (int k=x2; k<=x1; k++) {
                                a[k][y] = a[i][j];
                            }
                        } else {
                            break;
                        }
                        y++;
                    }
                }
            }
        }

        int flag = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (a[i][j] == '?') {
                    flag = 1;
                }
            }
        }

        if (flag == 1) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (vis[i][j] == 0) {
                        a[i][j] = '?';
                    }
                }
            }

            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (vis[i][j] == 1) {
                        int x, y, y1, y2;
                        x = i; y = j+1;
                        while (y < m and a[x][y] == '?') {
                            a[x][y] = a[i][j];
                            y++;
                        }
                        y1 = y-1;

                        x = i; y = j-1;
                        while (x >=0 and a[x][y] == '?') {
                            a[x][y] = a[i][j];
                            y--;
                        }
                        y2 = y+1;

                        x = i-1;
                        while (x >= 0){
                            int flag = 0;
                            for (int k=y2; k<=y1; k++) {
                                if (a[x][k] != '?') {
                                    flag = 1;
                                }
                            }
                            if (flag == 0) {
                                for (int k=y2; k<=y1; k++) {
                                    a[x][k] = a[i][j];
                                }
                            } else {
                                break;
                            }
                            x--;
                        }

                        x = i+1;
                        while (x <= n-1){
                            int flag = 0;
                            for (int k=y2; k<=y1; k++) {
                                if (a[x][k] != '?') {
                                    flag = 1;
                                }
                            }
                            if (flag == 0) {
                                for (int k=y2; k<=y1; k++) {
                                    a[x][k] = a[i][j];
                                }
                            } else {
                                break;
                            }
                            x++;
                        }
                    }
                }
            }
        }

        cout << "Case #" << ti+1 << ":" << endl;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                cout << a[i][j];
            }
            cout << endl;
        }

    }
}
