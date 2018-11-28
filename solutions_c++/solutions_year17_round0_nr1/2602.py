#include<bits/stdc++.h>
#include<string.h>
using namespace std;
char s[1002];
int main()
{
    freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        int k;
        scanf("%s",s+1);
        scanf("%d",&k);
        int n=strlen(s+1);
        int i=1,j,f=0,cnt=0;
        while(i<=n)
        {
            for(j=i;j<=n;j++)
            {
                if(s[j]=='+')
                    continue;
                else
                    break;
            }
            if(j<=n)
                {
                    if(n-j+1<k)
                    {
                        f=1;
                        break;
                    }
                    cnt++;
                }
            int idx=j;
            for(j=idx;j<=idx+k-1 && j<=n ;j++)
            {
                if(s[j]=='+')
                    s[j]='-';
                else
                    s[j]='+';
            }
            i=idx+1;
        }
        if(f)
        {
            printf("Case #%d: IMPOSSIBLE\n",x);
        }
        else
        {
            printf("Case #%d: %d\n",x,cnt);
        }
    }
    return 0;
}
