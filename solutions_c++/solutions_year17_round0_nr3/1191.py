#include <bits/stdc++.h>


using namespace std;


long long mx[65],cnt[65];
long long power[65];

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("outmainC.txt","w",stdout);
    power[0] = 1LL;
    for(int i = 1;  i < 65; i++)
    {
        power[i] = power[i-1] * 2LL;
    }
    //cout << power[1] << endl;
    int T;
    long long n, k;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%lld %lld",&n,&k);
        long long _a, _b;
        if(k==1)
        {
            if(n%2==0)
            {
                _a = n/2;
                _b = n/2 - 1;
            }
            else
            {
                _a = n/2;
                _b = n/2;
            }
            printf("Case #%d: %lld %lld\n",t,_a,_b);
            continue;
        }

        mx[0] = n;
        cnt[0] = 1;
        int i = 1;

        long long dead = 1;
        while(n)
        {
            mx[i] = mx[i-1]/2;
            if(mx[i-1]%2==0)
            {
                cnt[i] = cnt[i-1];
            }
            else
            {
                cnt[i] = 2*cnt[i-1] + (power[i-1]-cnt[i-1]);
            }
//            cout << k << endl;
//            cout << dead << endl;
//            cout << power[i] << endl;
            if(k-dead <= power[i])
            {
                if(k-dead <= cnt[i])
                {
                    if(mx[i]%2==1)
                    {
                        _a = mx[i]/2;
                        _b = mx[i]/2;
                    }
                    else
                    {
                        _a = mx[i]/2;
                        _b = mx[i]/2 - 1;
                    }
                }
                else
                {
                    if((mx[i]-1)%2==1)
                    {
                        _a = (mx[i]-1)/2;
                        _b = (mx[i]-1)/2;
                    }
                    else
                    {
                        _a = (mx[i]-1)/2;
                        _b = (mx[i]-1)/2 - 1;
                    }
                }
                break;
            }
            i++;
            n/= 2;
            dead += power[i-1];
        }
        printf("Case #%d: %lld %lld\n",t,_a,_b);
    }
    return 0;
}
