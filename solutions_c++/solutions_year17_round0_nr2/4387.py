#include <bits/stdc++.h>
using namespace std;
int S[30];
int main()
{
  int t; scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
        long long a; scanf("%lld", &a);
        int len = 0;
        for(int k = 0; a ; k++)
        {
            S[k] = a%10;
            a /= 10L ;
            len++;
        }
        
   /*     for(int k = 0; k < len ; k++)
            printf("%d ", S[k]);
        
       printf("len = %d\n", len);*/

        for(int k = len-1; k > 0; k--)
        {
            if(S[k] > S[k-1])
            {
                S[k] = S[k] - 1;
                for(int m = k-1; m >=0 ; m--)
                    S[m] = 9;
              k = len;
            }
        }
        
        long long ans = 0;
        for(int k = len-1; k >= 0 ; k--)
 
        {
            ans = ans * 10L;
            ans += (S[k]);
        }   
        printf("Case #%d: %lld\n", i, ans);
  }

return 0;
}