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
    ll T, b[11], n;
    char c[11];
    pair <ll, char> a[11];

    cin >> T;
    ff(numt, 1, T) {
        cin >> n >> b[1] >> b[3] >> b[2] >> b[6] >> b[4] >> b[5];
        cout << "Case #" << numt << ": ";

        c[1] = 'R';
        c[3] = 'O';
        c[2] = 'Y';
        c[6] = 'G';
        c[4] = 'B';
        c[5] = 'V';
        
        a[1] = mp(b[1], c[1]);
        a[2] = mp(b[2], c[2]);
        a[3] = mp(b[4], c[4]);
        sort(a + 1, a + 3 + 1);
        reverse(a + 1, a + 3 + 1);

        if (a[1].f > a[2].f + a[3].f) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        cout << a[1].s;
        --a[1].f;
        int cnth = 0;
        while (a[1].f < a[2].f + a[3].f) {
//            cout << a[1].f << " " << a[2].f << " " << a[3].f << endl;
            if (cnth % 2 == 0) {
                --a[2].f;
                cout << a[2].s;
            }
            else {
                --a[3].f;
                cout << a[3].s;
            }
            ++cnth;
        }
        fi(1, a[1].f) {
            cout << a[1].s;
            if (a[2].f > 0) {
                cout << a[2].s;
                --a[2].f;
            } else {
                cout << a[3].s;
            }
        }
        cout << endl;

    }
    return 0;
}