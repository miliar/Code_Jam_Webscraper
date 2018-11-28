#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define X first
#define Y second
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

int n, p, T;
int d[102][102][102][4];
int k[4];
int a[102];

int main() {
    fin("t.in");
    fout("t.out");
    sync;
    cin >> T;
    ff(numt, 1, T) {
        cin >> n >> p;
        clean(k);
        fi(1, n) {
            cin >> a[i];
            a[i] %= p;
            ++k[a[i]];
        }
        memset(d, -1, sizeof d);
        d[0][0][0][0] = k[0];
        fi(0, k[1]) {
            fj(0, k[2]) {
                fq(0, k[3]) {
                    ff(s, 0, p - 1) {
                        if (d[i][j][q][s] == -1)
                            continue;
                        int ti, tj, tq, ts;

                        ti = i;
                        tj = j;
                        tq = q;
                        ts = s;
                        
                        ++ti;
                        ts = (ts + 1) % p;
                        d[ti][tj][tq][ts] = max(d[ti][tj][tq][ts], d[i][j][q][s] + (s == 0));
                        ti = i;

                        ++tj;
                        ts = (ts + 1) % p;
                        d[ti][tj][tq][ts] = max(d[ti][tj][tq][ts], d[i][j][q][s] + (s == 0));
                        tj = j;

                        ++tq;
                        ts = (ts + 1) % p;
                        d[ti][tj][tq][ts] = max(d[ti][tj][tq][ts], d[i][j][q][s] + (s == 0));
                        tq = q;

                    }

                }
            }
        }

        int ans = 0;
        fi(0, p - 1) {
            ans = max(ans, d[k[1]][k[2]][k[3]][i]);
        }
        cout << "Case #" << numt << ": " << ans << endl;
    }
    return 0;
}