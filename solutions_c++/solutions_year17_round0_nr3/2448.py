#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <set>
#include <vector>
using namespace std;

long long pow2(long long t)
{
    if (t == 0) return 1;

    long long result = 1;
    while (t--)
    {
        result *= 2;
    }
    return result;
}

long long getlv(long long no)
{
    if (no <= 1) return 0;

    long long num = 2;
    long long lv = 1;
    while (num <= no)
    {
        num *= 2;
        lv++;
    }
    return lv - 1;
}

void cal(long long n, long long k, long long &r1, long long &r2)
{
    long long lv = getlv(k);
    long long num = pow2(lv);

    long long result = (n + 1 - num) / num;
    long long extra = n - (result * num + num - 1 );

    long long exceedcnt = k - num;
    if (exceedcnt < extra) result++;

    result--;
    if (result%2 == 0)
    {
        r1 = result / 2;
        r2 = r1;
    }
    else
    {
        r1 = result / 2 + 1;
        r2 = r1 - 1;
    }

}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    long long T,TT;

    cin>>T;
    for(TT = 1; TT <= T; TT++)
    {
        long long n,k,r1,r2;
        cin>>n>>k;
        cal(n, k, r1, r2);
        cout<<"Case #"<<TT<<": "<<r1<<" "<<r2<<endl;
    }

    return 0;
}
