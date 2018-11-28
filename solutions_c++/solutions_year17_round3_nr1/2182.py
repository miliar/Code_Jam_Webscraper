#include <stdio.h>
#include <algorithm>
#include <vector>

#define pi 3.14159265
#define DEBUG false

using namespace std;

typedef long long int lli;
typedef pair<lli, lli> plli;

int T;
int n,k;
plli pans[1000005];

bool const gt(plli a,plli b)
{
    return a > b;
}

int count_larger(int s, lli val)
{
    int c = 0;
    for (int i = s; i < n; i++)
    {
        if ( pans[i].second >= val ) c++;
    }
    return c;
}

double choose(int s, int l)
{
    if ( l == 0 ) return 0.0;
    double res = 0.0;
    lli R = pans[s].first, Rh = pans[s].second;
    if ( l == k ) res += pi * (double)(R*R);
    res += 2.0 * pi * (double)Rh;
    double r1 , r2 = r1 = 0.0;
    if ( s+l < n) r1 = choose(s + 1, l);
    if ( l > 0 ) r2 = choose(s + 1, l - 1);
    res += r2;
    res = max(res, r1);
    return res;
}

int main () {
    scanf("%d", &T);
    for (int i = 1; i<=T; i++) {
        printf("Case #%d: ", i);
        scanf("%d %d", &n, &k);
        for (int j = 0; j < n; j++) {
            lli r,h;
            scanf("%lld %lld", &r, &h);
            pans[j] = make_pair(r,r*h);
        }
        sort(pans, pans + n, gt);
        double Max = choose(0, k);
        printf("%lf\n", Max);
    }
    return 0;
}