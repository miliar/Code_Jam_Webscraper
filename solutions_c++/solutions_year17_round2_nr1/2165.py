#include <bits/stdc++.h>
using namespace std;
#define fin "A-large.in"
#define fou "A.out"
#define ff(i, a, b) for(int i = a; i <= b; i ++)
#define fd(i, a, b) for(int i = a; i >= b; i --)
#define x first
#define y second
#define endl '\n'
typedef long long data;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
const int N = 1010;

int test, n, D;
double k[N], v[N], k2[N], v2[N];
int pos[N];

void read()
{
    cin >> D >> n;
    ff(i, 1, n) cin >> k[i] >> v[i];
}

bool cmp(int u, int v) {return k[u] < k[v];}

inline double equation(double k1, double v1, double k2, double v2) // k1 + v1 * x = k2 + v2 * x;
{
    return (k2 - k1) / (v1 - v2);
}

inline double unequa(double k, double v, double t)
{
    return k / t + v;
}

void solve(int tnum, double ans = 1e15 + 1, double D2 = D)
{
    ff(i, 1, n) pos[i] = i;
    sort(pos + 1, pos + n + 1, cmp);
    ff(i, 1, n) k2[i] = k[i], v2[i] = v[i];
    ff(i, 1, n) k[i] = k2[pos[i]], v[i] = v2[pos[i]];

//    fd(i, n - 1, 1)
//    {
//        if (v[i] >= v[i + 1])
//        {
//            double t = equation(k[i], v[i], k[i + 1], v[i + 1]);
//            D2 = min(D2, k[i] + v[i] * t);
//            k[i + 1] = D2;
//        }
//        else {
//            k[i + 1] = k[i];
//            v[i + 1] = v[i];
//        }
//    }

    k[n + 1] = D;
    ff(i, 1, n)
    //if (k[i] != k[i + 1] && v[i] != v[i + 1])
    {
         ans = min(ans, unequa(k[i], v[i], (D - k[i]) / v[i]));
        // cerr << k[i] << " " << v[i] << endl;
    }
    cout.precision(7);
    cout << fixed << "Case #" << tnum << ": " << ans << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen(fin,"r",stdin), freopen(fou,"w",stdout);
    cin >> test;
    ff(i, 1, test)
    read(),
    solve(i);
    return 0;
}
