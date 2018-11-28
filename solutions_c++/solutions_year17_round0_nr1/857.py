#include <bits/stdc++.h>

using namespace std;
const int maxn = 1500;
char str[maxn];
int state[maxn];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,n,k,cas = 1;
    scanf("%d",&T);
    while(T--){
        scanf("%s%d",str,&k);
        n = strlen(str);
        int ans = 0;
        for(int i = 0;i < n;i++){
            if(str[i]=='-') state[i] = 1;
            else state[i] = 0;
        }
        for(int i = 0;i <= n-k;i++){
            if(state[i]){
                for(int j = 0;j < k;j++){
                    state[i+j] ^= 1;
                }
                ans++;
            }
        }
        int flag = 0;
        for(int i = 0;i < n;i++){
            if(state[i] == 1){
                flag = 1;
                break;
            }
        }
        printf("Case #%d: ",cas++);
        if(flag == 0) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
