#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large-out.txt","w",stdout);
    int T,len,k,ans;
    string s;cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>s>>k;
        len=s.size();ans=0;
        for(int i=0;i<len;i++){
            if(s[i]=='+')continue;
            ans++;
            if(i+k>len){
                ans=-1;
                break;
            }
            for(int j=i;j<i+k&&j<len;j++){
                if(s[j]=='+')s[j]='-';
                else s[j]='+';
            }
        }
        printf("Case #%d: ",ca);
        if(ans==-1)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
