#include <cstdio>

using namespace std;

const double EPS = 1e-6;
const double INF = 1e13;
const int MAXN = 1e3+5;

int TC, tc;

int D,N;
int k[MAXN], s[MAXN];

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);
    while(TC--) {
        scanf("%d%d", &D, &N);
        for(int i = 0; i < N; i++) scanf("%d%d", &k[i], &s[i]);
        double lo = EPS, hi = INF;
        while(hi-lo>EPS) {
            bool did=true;
            double mid = (lo+hi)/2;
            for(int i = 0; i < N; i++)
                if(mid>=s[i] && k[i]*mid < D*(mid-s[i])) did = false;
            if(did) lo = mid;
            else hi = mid;
        }
        printf("Case #%d: %.7lf\n", ++tc, lo);
    }
}
