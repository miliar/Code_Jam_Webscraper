#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PB(x) push_back(x)
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

// const int MNOGO = 0x3fffffff;

#define PROBLEM "C"

const int MAXN = 128;

int64 e[MAXN], s[MAXN];
int64 d[MAXN][MAXN];

int64 ps[MAXN];

double mint[MAXN];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int n, q;
        cin >> n >> q;

        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
            }
        }

        ps[1] = 0;
        for (int i = 2; i <= n; i++) {
            ps[i] = ps[i-1] + d[i-1][i];
        }

        for (int i = 1; i <= n; i++) {
            mint[i] = 1e18;
        }

        mint[1] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (ps[j] - ps[i] <= e[i]) {
                    double cand_time = mint[i] + (1.0 * (ps[j] - ps[i])) / s[i];
                    if (cand_time < mint[j]) {
                        mint[j] = cand_time;
                    }
                } else {
                    break;
                }
            }
        }

        for (int qq = 1; qq <= q; qq++) {
            int u, v;
            cin >> u >> v;

            printf("%0.7lf ", mint[n]);
        }

        printf("\n");
    }

    return 0;
}
