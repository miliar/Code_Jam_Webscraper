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

int n, k;
double u, a[55], b[55];

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> n >> k;
        cin >> u;
        FOR(i,1,n) cin >> a[i];
        double dau = 0;
        double cuoi = 1;
        double res = 0;
        FOR(p,1,1000) {
            double mid = (dau+cuoi) / 2;
            double U = u;
            FOR(i,1,n) {
                b[i] = a[i];
                if (b[i] > mid) continue;
                else {
                    double h = mid-b[i];
                    double e = min(U, h);
                    b[i] += e;
                    U -= e;
                }
            }
            bool co = true;
            FOR(i,1,n)
                if (b[i] < mid) {
                    co = false;
                    break;
                }
            if (co) {
                dau = mid;
                double w = 1;
                FOR(i,1,n) {
                    w *= b[i];
                }
                res = max(res, w);
            }
            else cuoi = mid;
        }
        cout << fixed << setprecision(9) << res << endl;
    }
    return 0;
}
