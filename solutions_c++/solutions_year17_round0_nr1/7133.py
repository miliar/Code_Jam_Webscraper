#include <bits/stdc++.h>
using namespace std;
int T,cas=0;
int main(){
    //freopen("A2.in","r",stdin);
    //freopen("A2.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        char raw[2005];
        int turnOver[2005];
        int k,ans=0;
        scanf("%s",&raw);
        scanf("%d",&k);
        int len=strlen(raw);
        for(int i=0;i<len;i++){
            if(raw[i]=='-')turnOver[i]=1;
            else turnOver[i]=0;
        }
        for(int i=0;i<len;i++){
            if(i<len-k+1&&turnOver[i]%2){
                ans++;
                for(int j=0;j<k;j++){
                    turnOver[i+j]+=1;
                }
            }
            if(turnOver[i]%2){ans=-1;break;}
        }
        if(ans==-1)printf("Case #%d: IMPOSSIBLE\n",++cas);
        else printf("Case #%d: %d\n",++cas,ans);
    }
}
