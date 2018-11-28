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
const int maxn = (int) 1e3 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0));

int T, n, c, m, person[maxn], s[maxn], l, r;
int promotions;

int check(int z) {
    promotions = 0;
    int sum = 0;
    fi(1, c) {
        if (person[i] > z)
            return 0;
    }
    ei(n, 1) {
//        cout << s[i] << endl;
        if (s[i] <= z) {
            sum = max(sum - (z - s[i]), 0);
            continue;
        }
        s[i] -= z;
        promotions += s[i];
        sum += s[i];
        s[i] += z;
    }
//    cout << "PROm" << endl;
//    cout << promotions << endl;
    if (sum > 0)
        return 0;
    return 1;
}

int main() {
    fin("t.in");
    fout("t.out");
    sync;
    cin >> T;
    ff(numt, 1, T) {
        cin >> n >> c >> m;
        clean(person);
        clean(s);
        fi(1, m) {
            int v, place;
            cin >> place >> v;
            ++person[v];
            ++s[place];
        }
        l = 0;
        r = m;
        while (l < r) {
            int mid = (l + r + 1) / 2;
            if (check(mid))
                r = mid - 1;
            else
                l = mid;
        }
        check(l + 1);
        cout << "Case #" << numt << ": " << l + 1 << " " << promotions << endl;
    }
    return 0;
}