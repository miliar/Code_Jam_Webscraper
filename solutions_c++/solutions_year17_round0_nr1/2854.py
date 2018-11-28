#include<bits/stdc++.h>
using namespace std;
string s;
int vis[10005];
int main(void){
    //freopen("123.in","r",stdin);
    //freopen("out.out","w",stdout);
    int i,j,n,m,T,k,cnt,now,ans,ok,ca=1;
    cin>>T;
    while(T--){
        cin>>s>>k;
        memset(vis,0,sizeof(vis));
        n=s.size();
        n=n-k;
        cnt=0;
        ans=0;
        ok=0;
        for(i=0;i<=n;i++){
            cnt+=vis[i];
            now=cnt;
            if(s[i]=='+'){
                if(now%2){
                    ans++;
                    vis[i+k]--;
                    cnt++;
                }
            }
            else {
                if(now%2==0){
                    ans++;
                    vis[i+k]--;
                    cnt++;
                }
            }
        }
        for(;s[i];i++){
            cnt+=vis[i];
            if(s[i]=='+'){
                if(cnt%2==1) ok=1;
            }
            else {
                if(cnt%2==0) ok=1;
            }
        }
        printf("Case #%d: ",ca++);
        if(ok) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}
