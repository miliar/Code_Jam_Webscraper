#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
const int maxn = 100;
long double eps = 1e-12;
int q[maxn][maxn], r[maxn], n, p;
bool v[maxn][maxn];
int cntL(int x, int r)
{
    return (int)(floor(eps + x/(0.9*r)));
}
int cntR(int x, int r)
{
    return (int)(ceil(-eps + x/(1.1*r)));
}
int _main()
{
    int ans = 0;
    cin >> n >> p;
    for(int i = 0; i < n; i++)cin >> r[i];
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < p; j++)cin >> q[i][j];
        sort(q[i], q[i] + p);
    }
    memset(v, 0, sizeof(v));
    for(int i = p-1; i >= 0; i--)
    {
        int lo = cntR(q[0][i], r[0]), hi = cntL(q[0][i], r[0]);
        if(lo > hi)continue;
        vector <int> w; w.pb(i);
        for(int j = 1; j < n; j++)
        for(int k = p-1; k >= 0; k--)if(!v[j][k])
        {
            int l = cntR(q[j][k], r[j]), ri = cntL(q[j][k], r[j]);
            if(min(ri, hi) >= max(l, lo))
            {
                w.pb(k);
                break;
            }
        }
        if(w.size() == n)
        {
            ans++;
            for(int j = 0; j < n; j++)v[j][w[j]] = 1;
        }
    }
    return ans;
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
        cout << "Case #" << i << ": " << _main() << "\n";
    }
    return 0;
}
