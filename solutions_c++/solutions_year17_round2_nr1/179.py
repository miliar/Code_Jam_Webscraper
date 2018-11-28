/*
 * (c) fushar (Ashar Fuadi)
*/

#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

const double EPS = 1e-9;
const int MAX = 1005;

typedef long long ll;

int T;
ll D;
int N;
ll K[MAX], S[MAX];

bool can(double v) {
    REP(i, N) {
        if (D*S[i]+EPS < (D-K[i])*v) {
            return false;
        }
    }
    return true;
}

int main() {
    scanf("%d", &T);
    REP(tc, T) {
        cin >> D >> N;
        REP(i, N) {
            int k;
            cin >> K[i] >> S[i];
        }

        double lo = 0, hi = 1e15;
        double res;
        REP(x, 100) {
            double mid = (lo + hi) / 2;
            if (can(mid)) {
                res = mid;
                lo = mid;
            } else {
                hi = mid;
            }
        }

        printf("Case #%d: %.7lf\n", tc+1, res);
    }
}
