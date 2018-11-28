#include <cstdio>
#include <set>
#include <cmath>
#define MAXN 105
#define INF 0x3f3f3f3f
#define INFd 1e100
#define eps 1e-7
using namespace std;

int nrt, n, nrq, start, dest;
int reach[MAXN], speed[MAXN];
int ma[MAXN][MAXN], dist[MAXN][MAXN];
double tt[MAXN];

struct Comp {
    bool operator()(int a, int b) const {
        if(fabs(tt[a] - tt[b]) < eps)
            return a < b;
        return tt[a] < tt[b];
    }
};

set<int, Comp> s;

int main() {

    scanf("%d", &nrt);
    for(int t = 1; t <= nrt; ++t) {
        scanf("%d %d", &n, &nrq);
        for(int i = 1; i <= n; ++i)
            scanf("%d %d", &reach[i], &speed[i]);

        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                scanf("%d", &ma[i][j]);
                dist[i][j] = ((ma[i][j] == -1) ? INF : ma[i][j]);
            }
        }


        for(int k = 1; k <= n; ++k) {
            for(int i = 1; i <= n; ++i) {
                for(int j = 1; j <= n; ++j) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        printf("Case #%d: ", t);
        while(nrq--) {
            scanf("%d %d", &start, &dest);
            for(int i = 1; i <= n; ++i)
                tt[i] = INFd;
            tt[start] = 0;

            s.clear();
            s.insert(start);
            while(!s.empty()) {
                int x = *s.begin();
                s.erase(s.begin());
                if(x == dest)
                    break;

                for(int i = 1; i <= n; ++i) {
                    if(dist[x][i] < INF && dist[x][i] <= reach[x]) {
                        double newTT = tt[x] + 1.0 * dist[x][i] / speed[x];

                        if(newTT < tt[i]) {
                            if(s.count(i))
                                s.erase(i);
                            tt[i] = newTT;
                            s.insert(i);
                        }
                    }
                }
            }

            printf("%.10f ", tt[dest]);
        }
        printf("\n");
    }

    return 0;
}