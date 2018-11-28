#include <bits/stdc++.h>
#include <iostream>
using namespace std;

long long d,i,n,k,s;
double m,mm;

void _main()
{
    m=0;
    scanf("%lld%lld", &d, &n);
    for(i=0;i<n;++i)
    {
        scanf("%lld%lld", &k, &s);
        mm=(double)(d-k)/s;
        if(mm>m)
            m=mm;
    }
    printf("%.6lf\n", d/m);
    //cout<<(double)d/m<<endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        printf("Case #%d: ", i);
        _main();
    }
    return 0;
}
