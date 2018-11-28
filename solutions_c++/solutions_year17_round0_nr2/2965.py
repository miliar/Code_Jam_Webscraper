#include <stdio.h>
#include <algorithm>
#include <cstring>
using namespace std;

int T;
int n;
char s[25];

int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);

    scanf("%d\n",&T);
    for(int it = 1; it<=T; it++)
    {
        printf("Case #%d: ",it);

        scanf("%s\n",s+1);
        n = strlen(s+1);

        if( n == 1 )
        {
            printf("%c",s[1]);
            printf("\n");
            continue;
        }

        int pos; s[0] = '0';
        for(pos=1;pos<=n;pos++)
            if( s[pos]<s[pos-1] ) break;

        if( pos == n+1 )
        {
            for(int i=1;i<=n;i++) printf("%c",s[i]);
            printf("\n");
            continue;
        }

        for(;pos>1 && s[pos-1]>s[pos]; pos--) s[pos-1]--;
        if( s[1] == '0')
        {
            for(int i=2;i<=n;i++) printf("9");
            printf("\n");
            continue;
        }

        for(int i=1;i<=pos;i++) printf("%c",s[i]);
        for(int i=pos+1;i<=n;i++) printf("9");
        printf("\n");
    }
    return 0;
}
