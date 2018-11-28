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

#define PROBLEM "B"

const int MAXC = 1024;
const int MAXN = 1024;
int a[MAXC];
int w[MAXN];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        memset(a, 0, sizeof a);
        memset(w, 0, sizeof w);

        int n, c, m;
        cin >> n >> c >> m;
        for (int i = 0; i < m; i++) {
            int p, b;
            cin >> p >> b;
            a[b]++;
            w[p]++;
        }

        int minrides = (m + n - 1) / n;
        for (int i = 1; i <= c; i++) {
            if (a[i] > minrides) {
                minrides = a[i];
            }
        }

        int slots = 0;
        for (int p = 1; p <= n; p++) {
            if (w[p] > minrides) {
                if (w[p] > minrides + slots) {
                    int extra = w[p] - (minrides + slots);
                    int addrides = (extra + p - 1) / p;
                    minrides += addrides;
                    slots += addrides * (p-1);
                    assert(w[p] <= minrides + slots);
                }
                slots -= w[p] - minrides;
            } else {
                slots += minrides - w[p];
            }
        }

        // 29 + 15 = 3 * 44 = 132
        // 10 20 100 = 130

        slots = 0;
        int promo = 0;
        for (int p = 1; p <= n; p++) {
            if (w[p] > minrides) {
                assert(w[p] <= minrides + slots);
                promo += w[p] - minrides;
                slots -= w[p] - minrides;
            } else {
                slots += minrides - w[p];
            }
        }

        printf("%d %d", minrides, promo);

        printf("\n");
    }

    return 0;
}
