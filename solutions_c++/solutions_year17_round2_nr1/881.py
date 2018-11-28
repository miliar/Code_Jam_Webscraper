#include "math.h"
#include <algorithm>
#include <set>
#include <complex>
#include <stack>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
#define rep(i, n) for (lli i = 0; i < (n); i++)
#define rrep(i, n) for (lli i = (n)-1; i >= 0; i--)
using namespace std;
typedef long long int lli;

int n;
double x[10005], s[10005];

double d;
bool ok(double v)
{
    double time = d / v;
    rep(i, n)
    {
        if (x[i] + time * s[i] < d) {
            return false;
        }
    }
    return true;
}
int main()
{
    int t;
    cin >> t;
    rep(i, t)
    {
        cin >> d >> n;
        rep(i, n)
        {
            cin >> x[i] >> s[i];
        }
        double u = 1e20, l = 0;
        rep(j, 100)
        {
            double m = (u + l) / 2;
            if (ok(m)) {
                l = m;
            } else {
                u = m;
            }
        }
        printf("Case #%d: %.10f\n", i + 1, u);
    }
}
