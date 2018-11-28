#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int digit[20];
int ans[20];

bool dfs(int n,int last,bool fp){
    if(n == -1) return true;
    int maxx = fp?digit[n]:9;
    for(int i = maxx;i >= 0;i--){
        if(i < last) return false;
        if(dfs(n-1,i,fp&&i==digit[n])){
            ans[n] = i;
            return true;
        }
    }
    return false;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,cas = 1;
    ll n;
    scanf("%d",&T);
    while(T--){
        scanf("%I64d",&n);
        int len = 0;
        while(n){
            digit[len++] = n%10;
            n /= 10;
        }
        dfs(len-1,-1,true);
        printf("Case #%d: ",cas++);
        int flag = 1;
        for(int i = len-1;i >= 0;i--){
            if(ans[i] != 0) flag = 0;
            if(ans[i]==0&&flag) continue;
            printf("%d",ans[i]);
        }
        printf("\n");
    }
    return 0;
}
