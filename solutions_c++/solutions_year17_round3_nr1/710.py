#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;
const double pi = 3.1415926535;
const int maxn = 1010;
struct cake
{
    long long r, h;
};
int test, n, k;
cake a[maxn];
double ans, sum;
class cmp1
{
    public:
        bool operator() (double a, double b)
        {
            return a > b;
        }
};
priority_queue <double, vector <double>, cmp1> heap;


bool cmp(cake a,cake b)
{
    return a.r < b.r;
}

double cv( cake x)
{
    return (double) x.h * 2 * pi * x.r;
}

double dt (cake x)
{
    return (double) pi * x.r * x.r;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; ++t)
    {
        while (!heap.empty()) heap.pop();
        ans = 0, sum = 0;
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; ++i) scanf("%lld%lld", &a[i].r, &a[i].h);
        sort(a + 1, a + n + 1, cmp);
        for (int i = 1; i <= n; ++i)
        {
            while (heap.size() >= k)
            {
                sum -= heap.top();
                heap.pop();
            }
            heap.push( cv(a[i]) );
            sum += cv(a[i]);
            ans = max(ans, sum + dt(a[i]));
        }
        printf("Case #%d: %.6f\n", t, ans);
    }
    return 0;
}
