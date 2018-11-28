#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

const int INF = (int)(1e9 + 1337);
const int64 LINF = (int64)(4e18);
const double EPS = (double)(1e-11);
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)

int n, k;
double u;
double p[100];

void solve()
{
    cin >> n >> k >> u;
    for(int i = 0; i < n; i++)
        cin >> p[i];
    double l = 0, r = 1.0;
    for(int i = 0; i < 256; i++)
    {
        double mid = (l + r) / 2.0;
        double tres = 0;
        for(int j = 0; j < n; j++)
        {
            double dt = max(0.0, mid - p[j]);
            tres += dt;
        }
        if(tres < u)
            l = mid;
        else
            r = mid;
    }
    double mn = (l + r) / 2.0;
    double ans = 1.0;
    for(int i = 0; i < n; i++)
        ans *= max(p[i], mn);
    cout.precision(10);
    cout << fixed << ans;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
    
    int ts;
    cin >> ts;
    for(int i = 1; i <= ts; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
}


