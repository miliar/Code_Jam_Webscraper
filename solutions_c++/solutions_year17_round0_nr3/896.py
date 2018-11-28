#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define MAXN 21010
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(ll i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(ll i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<ll, ll> II;
typedef vector<II> vi;

ll t, n, k;
queue<II> q;
map<ll, ll> ma;

void solve()
{
    while (!q.empty()) q.pop();
    q.push(II(-n,1));
    while (k) {
        ma.clear();
        while (!q.empty()) {
            II g = q.front();
            q.pop();
            ll num = -g.X;
            ll quantity = g.Y;
            if (quantity >= k) {
                cout << num/2 << " " << (num-1)/2 << endl;
                return;
            }
            k -= quantity;
            if (num/2) ma[-num/2] += quantity;
            if ((num-1)/2) ma[-(num-1)/2] += quantity;
        }
        for (map<ll, ll>::iterator it = ma.begin(); it!=ma.end(); it++) q.push(II(it->X, it->Y));
    }
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> n >> k;
        solve();
    }
    return 0;
}
