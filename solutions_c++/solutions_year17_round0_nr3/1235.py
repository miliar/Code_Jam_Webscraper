#include <bits/stdc++.h>

#define PI 3.14159265358979323846
#define EPS 1e-6
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define RFOR(i, a, b) for(int i=int(a)-1; i>=int(b); i--)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef vector<int> vi;

#define MAXN 10
#define MOD 1000000007

ii ans;

void solve(ll n, ll k) {
    priority_queue<ll> pq;
    map<ll, ll> m;

    pq.push(n);
    m[n] = 1;
    while (k) {
        ll f = pq.top() - 1;
        pq.pop();

        ll izq = f / 2;
        ll der = (f / 2) + (f % 2);

        if (k <= m[f+1]) {
            ans.first = der;
            ans.second = izq;
            return;
        }
        k -= m[f+1];

        if (izq == der) {
            if (!m[izq]) pq.push(izq);
            m[izq] = m[izq] + 2 * m[f+1];
        }
        else {
            if (!m[izq]) pq.push(izq);
            m[izq] = m[izq] + m[f+1];

            if (!m[der]) pq.push(der);
            m[der] = m[der] + m[f+1];
        }
    }
}


int main() { _
    int T;
    ll n, k;
    /**/
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    /**/
    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> n >> k;
        solve(n, k);

        cout << "Case #" << t << ": " << ans.first << " " << ans.second << endl;
    }



    return 0;
}


