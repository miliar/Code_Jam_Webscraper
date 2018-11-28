#include <bits/stdc++.h>
using namespace std;
int main(){
    int tc;
    scanf("%d",&tc);
    for(int t = 1; t <= tc; t++){
        int N, Q;
        scanf("%d%d",&N, &Q);
        double power[201], speed[201];
        double dis[201][201];
        double ans[201][200];
        int st[200], en[200];
        for(int i = 0; i < N; i++){
            scanf("%lf%lf",&power[i],&speed[i]);
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                scanf("%lf",&dis[i][j]);
                if(dis[i][j] == -1){
                    dis[i][j] = INFINITY;
                }
                ans[i][j] = INFINITY;
            }
        }

        for(int k = 0; k < N; k++){
            for(int i = 0; i < N;i++){
                for(int j = 0; j < N;j++){
                    if(dis[i][k] + dis[k][j] < dis[i][j]){
                        dis[i][j] = dis[i][k] + dis[k][j];
                    }
                }
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N;j++){
                if(dis[i][j]<=power[i]){
                    double temp = dis[i][j]/ speed[i];
                    ans[i][j] = min(ans[i][j], temp);
//                    if(i == 0 && j == 3){
//                        printf("\n%f %f haha\n", dis[i][j], speed[i]);
//                    }
                }
            }
        }

        for(int k = 0; k < N; k++){
            for(int i = 0; i < N;i++){
                for(int j = 0; j < N;j++){
                    if(ans[i][k] + ans[k][j] < ans[i][j]){
                        ans[i][j] = ans[i][k] + ans[k][j];
                    }
                }
            }
        }
        for(int i = 0; i < Q; i++){
            scanf("%d%d",&st[i],&en[i]);
        }

        printf("Case #%d: ",t);
        for(int i = 0; i < Q; i++){
            printf("%f ",ans[st[i]-1][en[i]-1]);
        }
        printf("\n");
    }
    return 0;
}
