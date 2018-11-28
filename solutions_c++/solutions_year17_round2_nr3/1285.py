#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define fori(i, n) for (int i = 0; i < (int)(n); ++i)
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif

    int i, j, k;
    int T, TT;
    cin >> TT;
    for (T = 1; T <= TT; T++)
    {
        printf("Case #%d: ", T);
        int N, Q;
        cin >> N >> Q;
        double E[N], S[N], D[N], DD[N];
        int U, V;
        fori(i, N) {
            cin >> E[i] >> S[i];
        }
        fori(i, N) {
            fori(j, N) {
                double dist;
                cin >> dist;
                if (i + 1 == j) {
                    D[j] = dist;
                }
            }
        }
        DD[0] = 0;
        for (int i = 1; i < N; ++i) {
            DD[i] = DD[i-1] + D[i];
        }

        // Q == 1
        cin >> U >> V; // 1, N -> 0 -> N-1
        U--; V--;
        double f[N];
        f[0] = 0;
        for (int i = 1; i <= V; ++i) {
            f[i] = f[i-1] + D[i];
            fori(j, i) {
                if (E[j] >= DD[i]-DD[j]) {
                    // switch horse
                    double tmp = f[j] + (DD[i]-DD[j])/S[j];
                    f[i] = min(tmp, f[i]);
                }
            }
        }
        printf("%.8lf\n", f[V]);

    }
	return 0;
}
