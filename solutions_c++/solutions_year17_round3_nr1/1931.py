#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

struct value
{
    long double r, h, s;
};

const long double PI = 3.141592653589793238462643;
long long n, k, T, k1;
long double sum, ans;
value a[1000];

bool cmp(value x, value y)
{
    return x.s > y.s;
}

int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>T;
    for (int t = 1; t <= T; ++t)
    {
        cin>>n>>k;
        k1 = k;
        for (int i = 0; i < n; ++i)
        {
            cin>>a[i].r>>a[i].h;
            a[i].s = 2.0 * PI * a[i].r * a[i].h;
        }
        sort(a, a + n, cmp);
        ans = 0;
        for (int j = 0; j < n; ++j)
        {
            sum = a[j].r * a[j].r * PI + a[j].s;
            for(int i = 0; i < k - 1; ++i)
                if(i != j) sum += a[i].s;
                    else ++k;
            k = k1;
            ans = max(ans, sum);
        }
        cout.precision(6);
        cout<<fixed<<"Case #"<<t<<": "<<ans<<"\n";
    }
}
