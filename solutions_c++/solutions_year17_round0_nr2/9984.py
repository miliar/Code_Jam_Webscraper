#include <iostream>
#include<stdio.h>
#include<cmath>
using namespace std;

int main()
{
    int t, power,cnt = 1;
    unsigned long long n, pre, r, ex, ans,c,y,z,g,temp, base;

freopen("tc.txt", "r", stdin);
    scanf("%d", &t);
    while(t--)
    {
        bool f = false;
        scanf("%lld", &n);

        power = 0;
        ans = 0;
        temp = n;
        while(n > 0)
        {
            base = ceil(pow(10,power));
            r = n%10;
            pre = n/10;
            g = pre;
            pre = pre % 10;
            if(r < pre)
            {
                y = g - 1;
                c = 0;
               unsigned long long x = base;
                while(x)
                {
                    c += x * 9;
                    x /= 10;
                }
                z = ceil(pow(10,power + 1));
                ex = y * z;
                n = y * 10;
                ans = c + ex;

                f = true;

            }
            power++;
            n /= 10;

        }

        if(f)
            printf("Case #%d: %lld\n", cnt++, ans);
        else
            printf("Case #%d: %lld\n", cnt++, temp);

    }
    return 0;
}
