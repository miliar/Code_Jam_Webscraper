#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <memory.h>
#include <iomanip>

using namespace std;

char s[55][55];
char l[55][55];
char r[55][55];

void solve() {
    int n, m;
    scanf("%d%d\n", &n, &m);
    for (int i = 1; i <= n; i++) {
        gets(s[i] + 1);
    }
    for (int i = 0; i <= n + 1; i++) {
        for (int j = 0; j <= m + 1; j++) {
            l[i][j] = r[i][j] = '#';
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i][j] != '?') {
                for (int ii = i + 1; ii <= n; ii++) {
                    if (s[ii][j] != '?') {
                        break;
                    } else {
                        s[ii][j] = s[i][j];
                    }
                }
                for (int ii = i - 1; ii >= 1; --ii) {
                    if (s[ii][j] != '?') {
                        break;
                    } else {
                        s[ii][j] = s[i][j];
                    }
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i][j] == '?') {
                l[i][j] = l[i][j - 1];
            } else {
                l[i][j] = s[i][j];
            }
        }
        for (int j = m; j >= 1; --j) {
            if (s[i][j] == '?') {
                r[i][j] = r[i][j + 1];
            } else {
                r[i][j] = s[i][j];
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i][j] == '?') {
                if (l[i][j] != '#') {
                    s[i][j] = l[i][j];
                } else {
                    s[i][j] = r[i][j];
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        puts(s[i] + 1);
    }
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d", &tc);
    for (int i = 1; i <= tc; i++) {
        printf("Case #%d:\n", i);
        solve();
    }
    return 0;
}