#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
#include <queue>
#include <cstring>
#include <set>
#include <map>

using namespace std;

const int maxN = 100010, maxK = 60, modP = 10007;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define ll long long
#define F first
#define S second
#define mp make_pair

int m, n, check[30][30], checkr[30], test;
char s[30][30], res[30][30];

int main() {
    scanf("%d\n", &test);
    foru(t, 1, test) {
        scanf("%d %d\n", &m, &n);
        repu(i, m) {
            checkr[i] = 0;
            repu(j, n) check[i][j] = 0;
        }
        repu(i, m) {
            scanf("%s\n", s[i]);
            repu(j, n)
                if (s[i][j] != '?') check[i][j] = 1, checkr[i] = 1;
        }
        repu(i, m)
            repu(j, n)
                if (s[i][j] <= 'Z' && s[i][j] >= 'A') {
                    int maxr = i, minr = i;
                    int maxc = j, minc = j;
                    while (maxc + 1 < n && check[i][maxc + 1] == 0) ++maxc, check[i][maxc] = 1;
                    while (minc - 1 >= 0 && check[i][minc - 1] == 0) --minc, check[i][minc] = 1;
                    while (maxr + 1 < m && checkr[maxr + 1] == 0) ++maxr;
                    while (minr - 1 >= 0 && checkr[minr - 1] == 0) --minr;
                    foru(r, minr, maxr)
                        foru(c, minc, maxc) res[r][c] = s[i][j];
                }
        printf("Case #%d:\n", t);
        repu(i, m) {
            repu(j, n) cout << res[i][j];
            cout << endl;
        }
    }
}
