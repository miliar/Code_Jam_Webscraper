#include<cstdio>
#include<cstring>
const int N=1005;
char str[N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++){
        int k;
        scanf("%s %d",str+1,&k);
        int len=strlen(str+1);
        int ans=0;
        for(int i=1;i<=len-k+1;i++){
            if(str[i]=='-'){
                for(int j=i;j<i+k;j++) {
                    if(str[j]=='+')str[j]='-';
                    else str[j]='+';
                }
                ans++;
            }
        }
        int flag=1;
        for(int i=1;i<=len;i++){
            if(str[i]!='+')flag=0;
        }
        printf("Case #%d: ",ca);
        if(flag)printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
