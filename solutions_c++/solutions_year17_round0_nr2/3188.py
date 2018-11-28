#include <bits/stdc++.h>
#define fread(ch) freopen(ch,"r",stdin)
#define fwrite(ch) freopen(ch,"w",stdout)

using namespace std;
using LL = long long;

LL n;

bool cal()
{
    LL tmp = n;
    LL b,pre,now;
    pre = 10;
    b = 1;

    while(tmp)
    {
        now = tmp%10;
        tmp /= 10;
        if(now > pre)
        {
            n = n-n%b-1;
            return false;;
        }
        pre = now;
        b *= 10;
    }

    return true;
}

int main()
{
    fread("B-large.in");
    fwrite("out.out");
    int t;

    scanf("%d",&t);

    for(int z = 1; z <= t; ++z)
    {
        scanf("%lld",&n);
        while(!cal());

        printf("Case #%d: %lld\n",z,n);
    }

    return 0;
}
