#include <bits/stdc++.h>
using namespace std;
char S[1005];
int main()
{
    int t; scanf("%d", &t);
    for(int p = 1; p <= t; p++)
    {
        scanf("%s", S);
        //for(int i =0 ; S[i]; i++) printf("%c", S[i]);
        int k; scanf("%d", &k);
        
        int sum = 0;
        for(int i = k-1; S[i]; i++)
        {
                if(S[i-k+1] == '-') 
                {
                    sum++;
                    for(int m = 0; m < k; m++) 
                        if( S[i-m] == '-') S[i-m] = '+';
                        else S[i-m] = '-';
                        
                }
        }
        
        bool czy = true;
        for(int i = 0; S[i]; i++)
            if(S[i] == '-') czy = false;
        
        if(czy) printf("Case #%d: %d\n", p, sum);
        else printf("Case #%d: IMPOSSIBLE\n", p);

    }

return 0;
}