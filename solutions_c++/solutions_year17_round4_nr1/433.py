#include <cstdio>

int G[109];
int k[5];

int main(){
    freopen("A-large (3).in", "r", stdin);
    freopen("Alargeout2.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, P;
        scanf("%d %d", &N, &P);
        for (int i = 0; i < P; i++){
            k[i] = 0;
        }
        //if (t==76) printf("T=76:N=%d\n",N);
        for (int i = 0; i < N; i++){
            scanf("%d", &G[i]);
            k[G[i]%P]++;
        }
        if (P==2){
            printf("Case #%d: %d\n", t, k[0]+(k[1]+1)/2);
        }
        else if (P==3){
            if (k[1]>k[2]){
                printf("Case #%d: %d\n", t, k[0]+k[2]+(k[1]-k[2]+2)/3);
            }
            else {
                printf("Case #%d: %d\n", t, k[0]+k[1]+(k[2]-k[1]+2)/3);
            }
        }
        else if (P==4){
            int ans = k[0];
            if (k[1]>k[3]){
                ans += k[3];
                ans += k[2]/2;
                if (k[2]%2==1){
                    if (k[1]-k[3]>=2){
                        ans++;
                        k[1] -= 2;
                        ans += (k[1]-k[3]+3)/4;
                    }
                    else {
                        ans++;
                    }
                }
                else {
                    ans += (k[1]-k[3]+3)/4;
                }
            }
            else {
                ans += k[1];
                ans += k[2]/2;
                if (k[2]%2==1){
                    if (k[3]-k[1]>=2){
                        ans++;
                        k[3] -= 2;
                        ans += (k[3]-k[1]+3)/4;
                    }
                    else {
                        ans++;
                    }
                }
                else {
                    ans += (k[3]-k[1]+3)/4;
                }
            }
            printf("Case #%d: %d\n", t, ans);
        }
    }
}
