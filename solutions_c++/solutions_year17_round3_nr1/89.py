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
pii a[1010];
double f[1010][1010];
int u[1010][1010];
int timer;
const double PI = acos(-1);

double dyn(int cur, int pre)
{
    if(cur > n)
        return 0;
    if(u[cur][pre] == timer)
        return f[cur][pre];

    double res = 0;

    u[cur][pre] = timer;
    return f[cur][pre] = res;
}

void solve()
{
    cin >> n >> k;
    for(int i = 1; i <= n; i++)
        cin >> a[i].first >> a[i].second;
    sort(a + 1, a + 1 + n, greater<pii>());
    double ans = 0;
    priority_queue<double> q;
    double tt = 0;
    for(int i = n; i >= 1; i--)
    {
        double dt = 2.0 * a[i].first * a[i].second;
        //cout << tt << ' ' << dt << '\n';
        ans = max(ans, dt + sq((double)a[i].first) + tt);
        q.push(-dt);
        tt += dt;
        while((int)q.size() > k - 1)
        {
            if(!q.empty())
                tt += q.top();
            q.pop();
        }
    }
    cout.precision(10);
    cout << fixed << ans * PI;
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


