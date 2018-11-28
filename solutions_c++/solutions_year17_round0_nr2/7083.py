#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d", &T);
    char a[20], b[20];
    for( int t=1; t<=T; t++ )
    {
        printf("Case #%d: ", t);
        scanf("%s", a);
        int i, n = strlen(a);
        b[0] = a[0];
        b[n] = 0;
        for( i=1; i<n; i++ )
            if ( a[i] >= a[i-1] )
                b[i] = a[i];
            else
                break;
        if ( i == n ) 
            printf("%s\n", b);
        else
        {
            int j;
            for( j=i; j<n; j++ ) b[j] = '9';
            j = i-1;
            b[j]--;
            while( j>0 && b[j]<b[j-1] )
            {
                b[j] = '9';
                b[j-1]--;
                j--;
            }

            if ( j == 0 && b[0] == '0' )
            {
                printf("%s\n", b+1);
            }
            else
            {
                printf("%s\n", b);
            }
        }
    }
    return 0;
}
