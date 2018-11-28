#include <cstdio>

using namespace std;

const int maxN = 111;
const double maxTime = 1e12;

int T, N, Q;

int E[maxN], S[maxN];

int D[maxN][maxN];

int U[maxN], V[maxN];

double pos[maxN], tm[maxN];

inline double min(double a, double b) {return a < b ? a : b;}

int main() {
#ifdef RS16
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
#endif // RS16

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        scanf("%d%d", &N, &Q);
        for(int i = 1; i <= N; ++i) scanf("%d%d", E+i, S+i);
        for(int i = 1; i <= N; ++i) {
            for(int j = 1; j <= N; ++j) scanf("%d", D[i]+j);
        }
        for(int i = 1; i <= Q; ++i) scanf("%d%d", U+i, V+i);

        pos[1] = 0;
        for(int i = 1; i < N; ++i) pos[i+1] = pos[i] + D[i][i+1];

        for(int i = 1; i <= N; ++i) tm[i] = maxTime;
        tm[1] = 0;
        for(int i = 1; i < N; ++i) {
            for(int j = i+1; j <= N; ++j) {
                if(pos[j]-pos[i] > E[i]) break;
                tm[j] = min(tm[j], tm[i] + (pos[j]-pos[i])/S[i]);
            }
        }
        printf("%.9f\n", tm[N]);
    }
}
