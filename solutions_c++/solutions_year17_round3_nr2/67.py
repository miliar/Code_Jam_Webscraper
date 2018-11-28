#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define f first
#define s second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
#define files(name) fin(name".in"); fout(name".out")
#define endl "\n"
#define fi(st,n) for (int i = (st); i <= (int)(n); ++i)
#define fj(st,n) for (int j = (st); j <= (int)(n); ++j)
#define fk(st,n) for (int k = (st); k <= (int)(n); ++k)
#define fq(st,n) for (int q = (st); q <= (int)(n); ++q)
#define fw(st,n) for (int w = (st); w <= (int)(n); ++w)
#define ff(i, st, n) for (int (i) = (st); (i) <= (int)(n); ++(i))
#define ei(st,n) for (int i = (st); i >= (int)(n); --i)
#define ej(st,n) for (int j = (st); j >= (int)(n); --j)
#define ek(st,n) for (int k = (st); k >= (int)(n); --k)
#define ef(i, st, n) for (int (i) = (st); (i) >= (int)(n); --(i))
#define ri(st,n) for (int i = (st); i < (int)(n); ++i)
#define rj(st,n) for (int j = (st); j < (int)(n); ++j)
#define rk(st,n) for (int k = (st); k < (int)(n); ++k)
#define rq(st,n) for (int q = (st); q < (int)(n); ++q)
#define rf(i, st, n) for (int (i) = (st); (i) < (int)(n); ++(i))
#define clean(a) memset((a),0,sizeof (a))
#define sync ios_base::sync_with_stdio(0);cin.tie(0)
#define y1 dsklmlvmd

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;

const int inf = (int)1e9;
const ll linf = (ll)1e18;
const dbl eps = (dbl) 1e-8;
const int mod = (int) 1e9 + 7;
const int maxn = (int) 1e5 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0));

int d[1503][1503][2], n, m, t[1503];

int main() {
    fin("t.in");
    fout("t.out");
    sync;
    int T;
    cin >> T;
    ff(numt, 1, T) {
        cin >> n >> m;
        clean(t);
        fi(1, n) {
            int l, r;
            cin >> l >> r;
            fj(l, r - 1) {
                t[j] |= 1;
            }
        }
        fi(1, m) {
            int l, r;
            cin >> l >> r;
            fj(l, r - 1) {
                t[j] |= 2;
            }
        }
        ll tday = 60 * 24;

        ll ans = inf;

        fi(0, tday) {
            fj(0, tday) {
                ff(flag, 0, 1) {
                    d[i][j][flag] = inf;
                }
            }
        }
        if ((t[0] & 1) == 0)
            d[0][1][0] = 0;
        fi(0, tday - 2) {
            fj(0, tday / 2) {
                ff(fl, 0, 1) {
                    if ((t[i + 1] & (1 + fl)) == 0)
                        d[i + 1][j + (!fl)][fl] = min(d[i + 1][j + (!fl)][fl], d[i][j][fl]);
                    if ((t[i + 1] & (1 + !fl)) == 0)
                        d[i + 1][j + fl][!fl] = min(d[i + 1][j + fl][!fl], d[i][j][fl] + 1);
                }
            }
        }
        ans = min(d[tday - 1][tday / 2][0], d[tday - 1][tday / 2][1] + 1);

        fi(0, tday) {
            fj(0, tday) {
                ff(flag, 0, 1) {
                    d[i][j][flag] = inf;
                }
            }
        }
        if ((t[0] & 2) == 0)
            d[0][0][1] = 0;

        fi(0, tday - 2) {
            fj(0, tday / 2) {
                ff(fl, 0, 1) {
                    if ((t[i + 1] & (1 + fl)) == 0)
                        d[i + 1][j + (!fl)][fl] = min(d[i + 1][j + (!fl)][fl], d[i][j][fl]);
                    if ((t[i + 1] & (1 + !fl)) == 0)
                        d[i + 1][j + fl][!fl] = min(d[i + 1][j + fl][!fl], d[i][j][fl] + 1);
                }
            }
        }
        ans = min(ans, (ll)min(d[tday - 1][tday / 2][0] + 1, d[tday - 1][tday / 2][1]));
        cout << "Case #" << numt << ": " << ans << endl;
    }
    return 0;
}