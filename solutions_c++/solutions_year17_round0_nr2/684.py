#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
long long n, init[20] = {1ll};
bool check(long long x)
{
    int pre = 9;
    while(x)
    {
        if(x%10 > pre)  return false;
        pre = x % 10;
        x /= 10;
    }
    return true;
}
long long solve(long long x)
{
    int num[20], idx = -1;
    while(x)
        num[++idx] = x%10,  x/=10;

    long long ans = 0;
    for(int i=idx;i;--i)
    {
        ans *= 10;
        if(num[i] <= num[i-1])
            ans += num[i];
        else {
            ans += num[i];
            ans--;
            if(!check(ans))
                ans = solve(ans);
            return ans = ans * init[i] + init[i]-1;
        }
    }
    ans*=10;
    ans += num[0];
    return ans;
}
int main()
{
    freopen("G:\\B.in", "r", stdin);
    freopen("G:\\B.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<20;i++)
        init[i] = init[i-1]*10;
    for(int ica=1;ica<=T;ica++)
    {
        scanf("%I64d",&n);
        //cout<<n<<endl;
        printf("Case #%d: %I64d\n", ica, solve(n));
    }
}