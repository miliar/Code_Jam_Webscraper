#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define ld long double
using namespace std;
const int maxn = 1002;
ll n, d;
ld t[maxn];
ld k[maxn], s[maxn];
pair <ld, ld> h[maxn];
ld _main(int tt)
{
    cin >> d >> n;
    for(int i = 0; i < n; i++)cin >> h[i].f >> h[i].s;
    sort(h, h + n);
    for(int i = 0; i < n; i++)
    {
        k[i] = h[i].f;
        s[i] = h[i].s;
    }
    for(int i = n-1; i >= 0; i--)
    {
        ld ans = (d-k[i])/s[i];
        for(int j = i+1; j < n; j++)if(s[j] < s[i])
        {
            ans = max(ans, t[j]);
        }
        t[i] = ans;
    }
    return d / (*max_element(t, t + n));
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt; cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        cout << "Case #" << i << ": " << fixed << setprecision(12) << _main(i) << "\n";
    }
    return 0;
}
