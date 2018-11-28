#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#define pdd pair<double,double>
#define pid pair<int,double>
#define F first
#define S second
#define mp make_pair
#define ll long long
#define INF 0x3f3f3f3f3f3f3f3f

using namespace std;

int T;
int N,Q;
pdd horse[105];
ll adj[105][105];
double adj2[105][105];
vector<pid> graph[105];

int main(){
    freopen("data2.in","r",stdin);
    freopen("data2.out","w",stdout);
    scanf("%d",&T);
    for (int z = 1; z <= T; z++){
        scanf("%d%d",&N,&Q);
        for (int i = 1; i <= N; i++) scanf("%lf%lf",&horse[i].S,&horse[i].F);
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                scanf("%lld",&adj[i][j]);
                if (adj[i][j] == -1) adj[i][j] = INF;
            }
        }
        for (int k = 1; k <= N; k++){
            for (int i = 1; i <= N; i++){
                for (int j = 1; j <= N; j++){
                    adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j]);
                }
            }
        }
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                if (i != j && adj[i][j] <= horse[i].S){
                    adj2[i][j] = adj[i][j]/horse[i].F;
                }else adj2[i][j] = INF;
            }
        }
        for (int k = 1; k <= N; k++){
            for (int i = 1; i <= N; i++){
                for (int j = 1; j <= N; j++){
                    adj2[i][j] = min(adj2[i][j],adj2[i][k] + adj2[k][j]);
                }
            }
        }
        printf("Case #%d: ",z);
        int x,y;
        while(Q--){
            scanf("%d%d",&x,&y);
            printf("%.6lf ",adj2[x][y]);
        }
        printf("\n");
    }
    return 0;
}
