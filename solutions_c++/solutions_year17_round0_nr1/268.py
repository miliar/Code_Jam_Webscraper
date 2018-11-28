#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int T,k;
char s[1009];
int main(){
//    freopen("A-large.in","r",stdin);
//    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%s%d",s,&k);
        int n=strlen(s),ans=0;
        for(int i=0;i<=n-k;++i){
            if(s[i]=='-'){
                for(int j=0;j<k;++j)s[i+j]=s[i+j]=='-'?'+':'-';
                ++ans;
            }
        }
        bool f=1;
        for(int i=n-k+1;i<n;++i)if(s[i]=='-')f=0;
        printf("Case #%d: ",ca);
        if(f)printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
