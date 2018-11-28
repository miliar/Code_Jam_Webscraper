#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define er erase
#define bg begin()
#define ed end()
#define f first
#define s second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
#define files(name) fin(name".in"); fout(name".out")
#define enter cout << "\n"
#define space cout << " "
#define endl "\n"
#define fi(st,n) for (int i = (st); i <= (n); ++i)
#define fj(st,n) for (int j = (st); j <= (n); ++j)
#define fk(st,n) for (int k = (st); k <= (n); ++k)
#define fq(st,n) for (int q = (st); q <= (n); ++q)
#define fw(st,n) for (int w = (st); w <= (n); ++w)
#define ff(i, st, n) for (int (i) = (st); (i) <= (n); ++(i))
#define ei(st,n) for (int i = (st); i >= (n); --i)
#define ej(st,n) for (int j = (st); j >= (n); --j)
#define ek(st,n) for (int k = (st); k >= (n); --k)
#define ef(i, st, n) for (int (i) = (st); (i) >= (n); --(i))
#define ri(st,n) for (int i = (st); i < (n); ++i)
#define rj(st,n) for (int j = (st); j < (n); ++j)
#define rk(st,n) for (int k = (st); k < (n); ++k)
#define rq(st,n) for (int q = (st); q < (n); ++q)
#define rf(i, st, n) for (int (i) = (st); (i) < (n); ++(i))
#define clean(a) memset((a),0,sizeof (a))
#define sync ios_base::sync_with_stdio(0);cin.tie(0)
#define y1 dsklmlvmd

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int inf = (int)1e9;
const dbl eps = (dbl) 1e-8;
const int mod = (int) 1e9 + 7;
const int maxn = (int) 1e5 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0));


int main() {
    fin("t.in");
    fout("t.out");
    sync;
    int T;
    cin >> T;
    ff(numt, 1, T) {
        static int a[111][111], st_a[111][111];
        int n, m;
        clean(a);
        cin >> n >> m;
        fi(1, m) {
            static string typ;
            static int x, y;
            cin >> typ >> x >> y;
            if (typ == "+" || typ == "o")
                a[x][y] |= 1;
            if (typ == "x" || typ == "o")
                a[x][y] |= 2;
        }
        static int row[222], column[222];
        clean(row);
        clean(column);
        fi(1, n)
            fj(1, n) {
                st_a[i][j] = a[i][j];
                if (a[i][j] & 2) {
                    row[i] = 1;
                    column[j] = 1;
                }
            }
        fi(1, n)
            fj(1, n) {
                if (!row[i] && !column[j]) {
                    row[i] = 1;
                    column[j] = 1;
                    a[i][j] |= 2;
                }
            }

        clean(row);
        clean(column);
        static int row_cnt[222], column_cnt[222];
        clean(row_cnt);
        clean(column_cnt);
        fi(1, n)
            fj(1, n) {
                ++row_cnt[i + j];
                ++column_cnt[i - j + n];
                if (a[i][j] & 1) {
                    row[i + j] = 1;
                    column[i - j + n] = 1;
                }
            }

        static set <pair <int, pii> > q;
        q.clear();
        fi(1, n) {
            fj(1, n) {
                q.ins(mp(row_cnt[i + j] + column_cnt[i - j + n], mp(i, j)));
            }
        }
        while (q.size()) {
            int i, j;
            i = q.begin()->s.f;
            j = q.begin()->s.s;
            q.erase(q.begin());
//            if (i == 5)
//                cout << "i == 5 " << j << " " << endl;
            if (row[i + j] || column[i - j + n])
                continue;
            row[i + j] = 1;
            column[i - j + n] = 1;
//            cout << i << " " << j << endl;
            a[i][j] |= 1;
        }
        int k = 0, ans = 0;
        fi(1, n)
            fj(1, n) {
                if (a[i][j] != st_a[i][j]) {
                    ++k;
                }
                if (a[i][j] & 1)
                    ++ans;
                if (a[i][j] & 2)
                    ++ans;
            }
        cout << "Case #" << numt << ": ";
        cout << ans << " " << k << endl;
        fi(1, n)
            fj(1, n)
                if (a[i][j] != st_a[i][j]) {
                    if (a[i][j] == 1)
                        cout << "+ ";
                    if (a[i][j] == 2)
                        cout << "x ";
                    if (a[i][j] == 3)
                        cout << "o ";
                    cout << i << " " << j << endl;
                }
    }

    return 0;
}