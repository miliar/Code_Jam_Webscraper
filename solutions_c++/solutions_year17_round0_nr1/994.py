#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstring>
using namespace std;
char c[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, cas=0, k, n;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s%d", c, &k);
        n = strlen(c);
        int ans = 0;
        for(int i=0;i+k-1<n;i++)
        {
            if(c[i]=='-')
            {
                for(int j=0;j<k;j++)
                {
                    if(c[i+j]=='+')
                    c[i+j]='-';
                    else
                    c[i+j]='+';
                }
                ans++;
            }
        }
        int im=0;
        for(int i=0;i<n;i++)
        {
            if(c[i]=='-')
            {
                im=1;
                break;
            }
        }
        printf("Case #%d: ", ++cas);
        if(im)
        puts("IMPOSSIBLE");
        else
        printf("%d\n", ans);
    }
}
