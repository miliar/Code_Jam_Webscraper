#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;
typedef pair<int, pii> pip;

#define fi first
#define se second

#define SIZE 1005

pii X[SIZE];
ll Y[SIZE];

int main()
{
    double pi = acos(-1);
    int T;
    scanf("%d", &T);
    for (int _c = 0; _c < T; _c ++) {
        printf("Case #%d: ", _c + 1);
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i ++) {
            scanf("%lld%lld", &X[i].fi, &X[i].se);
        }
        double f_ans = 0;
        for (int i = 0; i < N; i ++) {
            double ans = pi * X[i].fi * X[i].fi;
            ans += 2 * pi * X[i].fi * X[i].se;
            for (int j = 0; j < N; j ++) {
                Y[j] = X[j].fi * X[j].se;
                if (j == i) Y[j] = 0;
                if (X[j].fi > X[i].fi) Y[j] = 0;
                //printf("!!-! %d !!!\n", Y[j]);
            }
            sort(Y, Y + N);
            //printf("~~%lf\n", ans);
            for (int j = 0; j < K - 1; j ++) {
                //printf("!!! %d !!!\n", N - 1 - j);
                ans += 2 * pi * Y[N - 1 - j];
            }
            f_ans = max(ans, f_ans);
        }
        printf("%.9lf\n", f_ans);
    }
    return 0;
}
