#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
char s[10005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int k;
        scanf("%s %d",s,&k);
        int cur=0;
        int len=strlen(s);
        for(int i=0;s[i];++i)
        {
            if(s[i]=='-'&&i+k<=len)
            {
                for(int j=0;j<k;++j)
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else s[i+j]='-';
                cur++;
            }
        }
        int cnt=0;
        for(int i=0;s[i];++i)
            if(s[i]=='-')
                cnt++;
        printf("Case #%d: ",++ca);
        if(cnt)
            puts("IMPOSSIBLE");
        else printf("%d\n",cur);
    }
}
