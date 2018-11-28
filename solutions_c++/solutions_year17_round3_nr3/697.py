#include <bits/stdc++.h>
using namespace std;

#define in cin
#define out cout

#define REP(i,n) for(int i=0; i<n; i++)
#define REP2(i,s,e) for(int i=s; i<e; i++)
#define REPD(i,s,e,d) for(int i=s; i<=e; i+=d)
#define REPE(i,s,e) for(int i=s; i<=e; i++)
#define REPR(i,s,e) for(int i=s; i>=e; i--)

#define all(v) v.begin(), v.end()
#define pb push_back

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define rd(n) scanf("%d", &n)

#define x first
#define y second
#define intINF 2147483647
#define llINF 9223372036854775807LL
#define MOD 1000000007

void solve(int tc)
{
    int n, k; cin >> n >> k;
    double X; cin >> X;

    vector<double> v(n);
    for(int i=0; i<n; i++) cin >> v[i];

    double L = 0.00;
    double R = 1.00;
    int it = 100;
    while(it--)
    {
        double M = (L+R)/2;
        double remain = X;

        for(int i=0; i<n; i++)
        {
            double t = max(M-v[i], 0.0);
            remain -= t;
        }

        if(remain > 0) L = M;
        else R = M;
    }

    for(int i=0; i<n; i++)
    {
        v[i] += max(L-v[i], 0.0);
    }

    double res = 1.00;
    for(int i=0; i<n; i++) res *= v[i];

    printf("Case #%d: %.9f\n", tc, res);
}

int main()
{
#ifndef ONLINE_JUDGE
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);
#endif

    int tc; scanf("%d", &tc);
    for(int i=1; i<=tc; i++) solve(i);


    return 0;
}
