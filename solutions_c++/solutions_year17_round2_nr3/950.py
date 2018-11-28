#include <cstdio>
#include <vector>
#define INF 10000000000003
using namespace std;

vector<double> result[105];
int horseD[105], horseS[105];
long long DP[105][105];
double ti[105][105];

int main(){
    int totalCases;
    scanf("%d", &totalCases);
    for(int T = 1; T <= totalCases; ++T){
        int N, Q;
        scanf("%d%d", &N, &Q);
        for(int i = 1; i <= N; ++i){
            scanf("%d%d", &horseD[i], &horseS[i]);
        }
        for(int i = 1; i <= N; ++i){
            for(int j = 1; j <= N; ++j){
                scanf("%d", &DP[i][j]);
                if(DP[i][j] == -1)
                    DP[i][j] = INF;
            }
        }
        for(int k = 1; k <= N; ++k){
            for(int i = 1; i <= N; ++i){
                for(int j = 1; j <= N; ++j){
                    if(DP[i][j] > DP[i][k] + DP[k][j])
                       DP[i][j] = DP[i][k] + DP[k][j];
                }
            }
        }
        /*
        printf("\n");
        for(int i = 1; i <= N; ++i){
            for(int j = 1; j <= N; ++j){
                if(DP[i][j] != INF)
                    printf("%d ", DP[i][j]);
                else
                    printf("- ");
            }
            printf("\n");
        }
        */
        for(int i = 1; i <= N; ++i){
            for(int j = 1; j <= N; ++j){
                if(DP[i][j] > horseD[i])
                    ti[i][j] = INF;
                else
                    ti[i][j] = (double)DP[i][j]/horseS[i];
                if(i == j)
                    ti[i][j] = 0;
            }
        }
        for(int k = 1; k <= N; ++k){
            for(int i = 1; i <= N; ++i){
                for(int j = 1; j <= N; ++j){
                    if(ti[i][j] > ti[i][k] + ti[k][j])
                       ti[i][j] = ti[i][k] + ti[k][j];
                }
            }
        }
        /*
        for(int i = 1; i <= N; ++i){
            for(int j = 1; j <= N; ++j){
                if(ti[i][j] != INF)
                    printf("%.6lf ", ti[i][j]);
                else
                    printf("-.------");
            }
            printf("\n");
        }
        */
        for(int i = 1; i <= Q; ++i){
            int u, v;
            scanf("%d%d", &u, &v);
            result[T].push_back(ti[u][v]);
        }
    }
    for(int T = 1; T <= totalCases; ++T){
        printf("Case #%d:", T);
        for(int i = 0; i < result[T].size(); ++i){
            printf(" %.6lf", result[T][i]);
        }
        printf("\n");
    }
    return 0;
}
