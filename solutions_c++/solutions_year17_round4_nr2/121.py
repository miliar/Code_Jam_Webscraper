#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int test, tt;
int n, c, m;
int p[1000], b[1000];
int c1, c2;
int x[1001];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d%d", &n, &c, &m);
        forn(i, m) scanf("%d%d", p + i, b + i);
        if (c != 2) {
            printf("-1 -1\n");
            cerr << "Done " << test << endl;
            continue;
        }
        c1 = c2 = 0;
        forn(i, m) if (b[i] == 1) {
            if (p[i] == 1) ++c1;
            else ++c2;
        }
        int cnt = c1 + c2;
        forn(i, m) if (b[i] == 2 && p[i] == 1) {
            if (c2) --c2;
            else ++cnt;
        }
        forn(i, m) if (b[i] == 2 && p[i] != 1) {
            if (c1) --c1;
            else if (c2) --c2;
            else ++cnt;
        }
        memset(x, 0, sizeof x);
        int prom = 0;
        forn(i, m) {
            if (++x[p[i]] > cnt) {
                ++prom;
            }
        }
        printf("%d %d\n", cnt, prom);
        cerr << "Done " << test << endl;
    }
    return 0;
}
