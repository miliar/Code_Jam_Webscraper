#include <cstdio>
#include <cstring>
#define N 1005
using namespace std;
int T,k,len,ans,j;
char s[N];
int main(void){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d%*c",&T);
    for(int t=1;t<=T;++t){
        scanf("%s%d%*c",s,&k);
        len=strlen(s);ans=0;
        bool flag=1;
        for(int i=0;i<len;++i)if(s[i]=='-'){
            ans++;
            for(j=0;j<k&&i+j<len;++j){
                if(s[i+j]=='-')s[i+j]='+';
                else s[i+j]='-';
            }
            if(j!=k){
                flag=0;
                break;
            }
        }
        if(flag)printf("Case #%d: %d\n",t,ans);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
}
