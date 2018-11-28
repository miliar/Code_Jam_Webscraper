#include <bits/stdc++.h>

using namespace std;

long long int n,t;

int main()
{
    freopen("B-small-attempt3.in","r",stdin);

    freopen("output_file_name.out","w",stdout);

    scanf("%lld",&t);

    for(long long int i=1; i<=t; i++)
    {
        scanf("%lld",&n);

        for(long long int j=n; j>=1; j--)
        {
            long long int num = j,rem,prevrem;

            prevrem = num % 10;

            num /= 10;

            long long int cnt = 1,digit = 1;

            while(num != 0)
            {
               rem = num % 10;

               if(rem <=  prevrem)
               {
                    num /= 10;
                    prevrem = rem;
               }
               else
               {
                   break;
               }
            }

            if(num == 0)
            {
                printf("Case #%lld: %lld\n",i,j);
                break;
            }
        }
    }

    return 0;
}
