#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cassert>
using namespace std;

const int MAXN = 100;
const int MAXQ = 100;
const double oops = 1e17;

const int LIMIT = 1e9 + 7;

int mat[MAXN + 5][MAXN + 5];
int speed[MAXN + 5], maxDist[MAXN + 5];
int n,Q;
int source, sink;

int dist[MAXN + 5][MAXN + 5];

double tim[MAXN + 5][MAXN + 5];

double ans[MAXQ + 5];

void warshall() {
    for (int c=0;c<n;c++) {
        for (int c2=0;c2<n;c2++)
            dist[c][c2] = mat[c][c2] < 0 ? LIMIT : mat[c][c2];
        dist[c][c] = 0;
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                dist[i][j] = min(dist[i][j], LIMIT);
            }
        }
}

void warshallTime() {
    int c,c2;
    for (c=0;c<n;c++)
        for (c2=0;c2<n;c2++)
            tim[c][c2] = oops;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] <= maxDist[i])
                tim[i][j] = 1. * dist[i][j] / speed[i];
        }
    }
    for (int k = 0; k < n; k ++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tim[i][j] = min(tim[i][j], tim[i][k] + tim[k][j]);
}

int main() {
    freopen("pony.in","r",stdin);
    freopen("pony.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        scanf("%d%d",&n,&Q);
        for (c=0;c<n;c++) {
            scanf("%d%d",&maxDist[c],&speed[c]);
        }
        for (c=0;c<n;c++)
            for (c2=0;c2<n;c2++)
                scanf("%d",&mat[c][c2]);
        warshall();
        warshallTime();
        printf("Case #%d:",test);
        for (c=0;c<Q;c++) {
            int u,v;
            scanf("%d%d",&u,&v);
            u--;v--;
            printf(" %.8f",tim[u][v]);
        }
        printf("\n");
    }
    
    return 0;
}
