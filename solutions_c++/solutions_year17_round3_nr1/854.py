#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<int, int> II;
typedef vector<II> vi;

struct data {
    ll r, h;
} a[1010];

bool operator< (data a, data b)
{
    return a.r < b.r;
}

int n, k;
ll dp[1010][1010], f[1010];

int main()
{
    double PI = acos(-1);
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> n >> k;
        FOR(i,1,n) cin >> a[i].r >> a[i].h;
        sort(a+1, a+n+1);
        FOR(i,1,n)
            FOR(j,1,k) dp[i][j] = 0;
        FOR(i,0,k) f[i] = 0;
        FOR(i,1,n)
            FORE(j,k,1) {
                if (j > i) continue;
                dp[i][j] = f[j-1] + 2*a[i].h*a[i].r;
                f[j] = max(f[j], dp[i][j]);
            }
        ll res = 0;
        FOR(i,1,n) res = max(res, dp[i][k] + a[i].r*a[i].r);
        cout << fixed << setprecision(6) << res*PI << endl;
    }
    return 0;
}
