#include <stdio.h>
#include <algorithm>
#include <cstring>
#define maxn 1005
using namespace std;

int T;
int n,K;
char s[maxn];

int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);

    scanf("%d\n",&T);
    for(int it = 1; it<=T; it++)
    {
        printf("Case #%d: ",it);

        scanf("%s %d\n",s+1,&K);
        n = strlen(s+1);

        int nr = 0;
        for(int i=1;i+K-1<=n;i++)
            if( s[i] == '-' )
            {
                nr++;
                for(int j=i;j<=i+K-1;j++)
                if( s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }

        int ok = 1;
        for(int i=1;i<=n;i++)
            if( s[i] == '-')
            {
                ok = 0;
                break;
            }
        if( !ok ) printf("IMPOSSIBLE\n");
        else
            printf("%d\n",nr);
    }
    return 0;
}
