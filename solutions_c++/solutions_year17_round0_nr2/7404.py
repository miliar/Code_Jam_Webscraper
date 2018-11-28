#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w", stdout);
    int t, i;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        int digit[30];
        long long n;
        memset(digit, 0, sizeof(digit));
        scanf("%lld", &n);
        int j=0;
        while(n)
        {
            digit[j] = n%10;
            j++;
            n /= 10;
        }
        int lim = j, flag=1;
        for(j=0; j<lim-1; j++)
        {
            if(digit[j]<digit[j+1])
            {
                flag = 0;
                break;
            }
        }
        printf("Case #%d: ", i);
        if(flag)
        {
            for(j=lim-1; j>=0; j--) printf("%d", digit[j]);
            printf("\n");
        }
        else
        {
            int idx, pt=0;
            while(!pt)
            {
                for(j=lim-1; j>0; j--)
                {
                    if(digit[j]>digit[j-1])
                    {
                        digit[j]--;
                        if(j==lim-1)
                        {
                            if(digit[j]==0)
                            {
                                for(idx=0; idx<lim-1; idx++) printf("9");
                                printf("\n");
                                pt=1;
                                break;
                            }
                            else
                            {
                                for(idx=lim-1; idx>=j; idx--) printf("%d", digit[idx]);
                                for( ; idx>=0; idx--) printf("9");
                                printf("\n");
                                pt=1;
                                break;
                            }
                        }
                        else
                        {
                            if(digit[j] < digit[j+1])
                            {
                                break;
                            }
                            else
                            {
                                for(idx=lim-1; idx>=j; idx--) printf("%d", digit[idx]);
                                for( ; idx>=0; idx--) printf("9");
                                printf("\n");
                                pt=1;
                                break;
                            }
                        }
                    }
                }
            }

        }

    }

    return 0;
}
