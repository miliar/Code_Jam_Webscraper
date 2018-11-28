#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 33;
string cake[maxn];


int main() {
    freopen("ainput.txt", "r", stdin);
    freopen("aoutput.txt", "w", stdout);
    int T, ca = 0;
    scanf("%d", &T);
    int n, m;
    while (scanf("%d %d", &n, &m) != EOF) {
        for (int i = 0; i < n; ++i) cin >> cake[i];
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (cake[i][j] == '?') cake[i][j] = cake[i - 1][j];
            }
        }
        for (int i = n - 2; i >= 0; --i) {
            for (int j= 0; j < m; ++j) {
                if (cake[i][j] == '?') cake[i][j] = cake[i + 1][j];
            }
        }
        for (int j = 1; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                if (cake[i][j] == '?') cake[i][j] = cake[i][j - 1];
            }
        }
        for (int j = m - 2; j >= 0; --j) {
            for (int i = 0; i < n; ++i) {
                if (cake[i][j] == '?') cake[i][j] = cake[i][j + 1];
            }
        }
        printf("Case #%d:\n", ++ca);
        for (int i = 0; i < n; ++i) {
            printf("%s\n", cake[i].c_str());
        }
    }
    return 0;
}