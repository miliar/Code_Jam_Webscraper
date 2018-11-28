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

int n, k;
dbl s, a[55];

int main() {
    fin("t.in");
    fout("t.out");
    sync;

    int T;
    cin >> T;
    cout << fixed << setprecision(10);
    ff(numt, 1, T) {
        cin >> n >> k;
        cin >> s;
        fi(1, n) {
            cin >> a[i];
        }
        sort(a + 1, a + n + 1);
        reverse(a + 1, a + n + 1);
        dbl h = a[k], h0;
        a[0] = 1.0;
        ei(k - 1, 0) {
            h0 = h;
            h = min(a[i], h + s / (dbl)(k - i));
            s -= (h - h0) * (dbl)(k - i);
            if (s < eps) {
                fj(i + 1, k) {
                    a[j] = h;
                }
                break;
            }
        }
        dbl ans = 1.0;
        fi(1, k) {
            ans *= a[i];
        }

        cout << "Case #" << numt << ": " << ans << endl;
    }
    return 0;
}