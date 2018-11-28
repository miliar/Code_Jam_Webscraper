#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char s[1005];
int k;
int solve()
{
    int ret=0;
    int len=strlen(s);
    for(int i=0; i<len; i++)
    {
        if(s[i]=='-')
        {
            if(i+k>len) return -1;
            ret++;
            for(int j=i; j<i+k; j++)
            {
                if(s[j]=='-')s[j]='+';
                else s[j]='-';
            }
        }
    }
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++)
    {
        scanf("%s%d",s,&k);
        int ans=solve();
        printf("Case #%d: ", cases);
        if(ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
