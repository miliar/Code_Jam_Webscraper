
#include<bits/stdc++.h>
using namespace std;
int dp[55][55],a[55],b[55][55],flag[55];
int main(void){
    freopen("123.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,k,n,m,T,ca=1,ans,bre,cnt;
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                scanf("%d",&b[i][j]);
            }
            sort(b[i],b[i]+m);
        }
        ans=0;bre=0;
        memset(dp,0,sizeof(dp));
        for(k=1;;k++){
            cnt=0;
            for(i=0;i<n;i++){
                double ANS=a[i]*(0.9)*k,ANSS=a[i]*(1.1)*k;
                for(j=0;j<m;j++){
                    if(dp[i][j]) continue ;
                    if(ANS<=b[i][j]&&ANSS>=b[i][j]){
                        cnt++;
                        flag[i]=j;
                        break;
                    }
                }
                if(ANS>b[i][m-1]) bre=1;
            }
            if(cnt==n){
                ans++;
                for(i=0;i<n;i++){
                    dp[i][flag[i]]=1;
                }
            }
            if(bre) break;
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
}
