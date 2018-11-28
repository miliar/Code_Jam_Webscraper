#include <stdio.h>
#include <string.h>

int main()
{
    char p[1005];
    int T, k;
    scanf("%d", &T);
    for( int t=1; t<=T; t++ )
    {
        scanf("%s %d", p, &k);
        int n = strlen(p);
        int ans = 0;
        for( int i=0; i<=n-k; i++ )
        {
            if ( p[i] == '-' )
            {
                ans++;
                for( int j=i; j<i+k; j++ )
                    p[j] = ('+' + '-') - p[j];
            }
        }
        int bad = 0;
        for( int i=n-k; i<n; i++ )
            if ( p[i] == '-' ) bad = 1;
        printf("Case #%d: ", t);
        if ( bad ) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
    }
    return 0;
}
