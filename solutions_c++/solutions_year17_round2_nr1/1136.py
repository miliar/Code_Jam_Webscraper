#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cnt;
    cin >> cnt;
    int n, s;
    long long d, k;
    double rst;
    for(int c = 1; c <= cnt; ++c)
    {
        cin >> d >> n;
        double maxtime = 0;
        while(n--)
        {
            cin >> k >> s;
            maxtime = max(maxtime, (d - k) / (double)s);
        }
        rst = d / maxtime;
        printf("Case #%d: %.6lf\n", c, rst);
    }
    return 0;
}
