#include <stdio.h>

int t;
long long n, k;
long long a, b, an, bn;

int main()
{
    freopen("/Users/IohcEjnim/Desktop/TEMP/C-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/TEMP/result.out", "w", stdout);

    int tn;
    scanf("%d", &t);
    
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%lld %lld", &n, &k);
        a = n; an = 1;
        b = 0; bn = 0;
        
        while (1)
        {
            if (an+bn >= k) break;
            k -= an+bn;
            
            if (bn == 0)
            {
                if (a%2)
                {
                    a /= 2;
                    an *= 2;
                }
                else
                {
                    b = a/2;
                    a = b-1;
                    bn = an;
                }
            }
            
            else
            {
                if (a%2)
                {
                    a = a/2;
                    b = a+1;
                    an += an+bn;
                }
                else
                {
                    b = b/2;
                    a = b-1;
                    bn += an+bn;
                }
            }
        }
        
        printf("Case #%d: ", tn);
        if (k <= bn) printf("%lld %lld\n", b/2, (b-1)/2);
        else printf("%lld %lld\n", a/2, (a-1)/2);
    }
}