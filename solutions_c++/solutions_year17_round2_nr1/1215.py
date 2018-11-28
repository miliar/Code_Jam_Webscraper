#include <bits/stdc++.h>
#define all(a) (a).begin(),(a).end()
#define ld long double
#define ll long long
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
#define pi pair<int,int>
#define y1 fdfs
using namespace std;

const int N = 1e3 + 5;
const long double eps = 1e-6;
pair<long long, long long> a[N];
int n, t;
long long D;

bool f(long double v0)
{
    for (int i = 0; i < n; ++i)
    {
        if (v0 <= a[i].y) continue;
        if (v0 * a[i].x < D * (v0 - a[i].y)) return 0;
    }
    return 1;
}

long double solve()
{
    cin >> D >> n;
    for (int i = 0; i < n; ++i)
        cin >> a[i].x >> a[i].y;
    long double l = 0, r = 1e18;
    for (int it = 0; it < 300; ++it)
    {
        long double mid = (l + r) / 2;
        if (f(mid)) l = mid;
               else r = mid;
    }
    if (f(r)) return r;
    return l;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout.precision(6);
        cout << "Case #" << i<< ": " << fixed << solve() << "\n";
    }
}
