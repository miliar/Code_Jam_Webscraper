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

typedef pair<int, int> II;
typedef vector<II> vi;

ll t, n, N, a[30];

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> n;
        ll h = n;
        N = 0;
        while (h) {
            a[++N] = h % 10;
            h /= 10;
        }
        FOR(i,1,N/2) swap(a[i], a[N-i+1]);
        FOR(i,1,N)
            if (a[i] < a[i-1]) {
                ll k = i-1;
                a[k]--;
                while (a[k] < a[k-1]) {
                    k--;
                    a[k]--;
                }
                FOR(j,k+1,N) a[j] = 9;
                break;
            }
        ll res = 0;
        FOR(i,1,N) res = res * 10 + a[i];
        cout << res << endl;
    }
    return 0;
}
