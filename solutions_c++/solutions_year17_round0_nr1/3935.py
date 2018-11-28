#include<cstdio>
#include<cstring>
using namespace std;
const int N=1e3+10;
char s[N];
int T,k,kase;
int f[N];
int main()
{
    //freopen("in.in","r",stdin);
    //freopen("out.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%s%d",s,&k);
        int n=strlen(s),cnt=0;
        bool flag=1;
        for(int i=0;i<n;i++)f[i]=(s[i]=='-');
        for(int i=0;i<n;i++)if(f[i]){
            cnt++;
            for(int j=0;j<k;j++){
                f[i+j]^=1;
                if(i+j>=n){
                    flag=0;
                    break;
                }
            }
        }
        printf("Case #%d: ",++kase);
        if(flag)printf("%d\n",cnt);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
