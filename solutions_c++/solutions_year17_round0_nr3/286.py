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
        static map <ll, ll> q;
        ll n, k, l, s, l1, l2;
        cout << "Case #" << numt << ": ";
        cin >> n >> k;
        q.clear();
        q[-n] = 1;
        while (k > 0) {
            l = -(q.begin()->f);
            s = q.begin()->s;
            q.erase(q.begin());
            if (l & 1) {
                l1 = l / 2;
                l2 = l / 2;
            } else {
                l1 = l / 2;
                l2 = l / 2 - 1;
            }
            if (s >= k) {
                cout << l1 << " " << l2;
                break;
            }
            k -= s;
            q[-l1] += s;
            q[-l2] += s;
        }
        cout << endl;
    }

    return 0;
}