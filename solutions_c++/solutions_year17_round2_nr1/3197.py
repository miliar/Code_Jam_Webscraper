#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(ll i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(ll i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<int, int> II;
typedef vector<II> vi;

struct data {
    ll root, mspeed;
} a[1010];

bool operator< (data a, data b) {
    return a.root > b.root;
}

ll n, m;

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll t;
    cin >> t;
    FOR(o,1,t) {
        cin >> m >> n;
        FOR(i,1,n) cin >> a[i].root >> a[i].mspeed;
        sort(a+1, a+n+1);
        ll A = 0, B = 1;
        FOR(i,1,n) {
            ll h = m-a[i].root;
            if (h*B > A*a[i].mspeed) {
                A = h;
                B = a[i].mspeed;
            }
        }
        cout << "Case #" << o << ": ";
        cout << fixed << setprecision(9) << m*B/double(A) << endl;
    }
    return 0;
}
