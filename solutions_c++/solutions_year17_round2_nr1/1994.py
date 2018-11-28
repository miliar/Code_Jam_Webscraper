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
typedef pair<int, int> ii;
typedef vector<int> vi;

#define MAXN 1005
#define MOD 1000000007

ii c[MAXN];
int d, n;

double solve() {
    sort(c, c + n);

    long double t = -INF;
    for(int i = n-1; i >= 0; i --) {
        long double a = d - c[i].first;
        t = max(t, a / c[i].second);
    }

    double ret = (d + 0.0) / t;
    return ret;
}

int main() { _
    int T;

    /**/
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    /**/

    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> d >> n;
        FOR(i, 0, n)    cin >> c[i].first >> c[i].second;

        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(6) << solve() << endl;
    }

    return 0;
}
