#include <bits/stdc++.h>
#define FOR(i,a,b) for (int i=a; i <=b ; i++)
#define FO(i,a,b) for (int i=a; i < b ; i++)
#define FORD(i,a,b) for (int i=a; i >=b ; i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SET(arr,c) memset(arr,c,sizeof(arr))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define PI 2 * acos(0.0)
#define debug cout << "#PASS" << endl;
#define sqr(x) (x) * (x)
#define cube(x) (x) * (x) * (x)
using namespace std;

template <class T> int getbit(int i, T X) { return (X & (1<<(i-1))); }
template <class T> T onbit(int i, T X) { return (X | (1<<(i-1))); }
template <class T> T offbit(int i, T X) { return (X | (1<<(i-1)) - (1<<(i-1))); }
template <class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template <class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

int dx[4]={0, 0, -1, 1};
int dy[4]={-1, 1, 0, 0};

typedef pair <ll, ll> II;
typedef pair <int, II> III;

const int inf = 1e9;
const ll linf = 1e18;
const int maxn = 20;
const int MOD = 1e9 + 7;


/***********VAR***********/
int res = 0, N, P, r[maxn + 5], q[maxn + 5][maxn + 5], dd[maxn + 5], kq[maxn + 5];
/*************************/

void enter() {
    cin >> N >> P;
    FOR(i, 1, N) cin >> r[i];
    FOR(i, 1, N) FOR(j, 1, P) cin >> q[i][j];
}

void ghinhan() {
    int ans = 0;

    FOR(i, 1, P) {
        // cout << "ii = " << i << endl;
        int cnt = 0;
        int minx = -inf;
        int maxx = inf;

        FOR(j, 1, N) {
            int k;
            if (j == 1) k = q[j][i];
            else k = q[j][kq[i]];
            int canduoi = (100 * k) / (110 * r[j]);
            if ((100 * k) % (110 * r[j])) ++canduoi;
            minx = max(minx, canduoi);
            int cantren = (100 * k) / (90 * r[j]);
            //cout << "canduoi, cantren: " << canduoi << " " << cantren << endl;
            if (cantren < canduoi) break;
            ++cnt;
            maxx = min(maxx, cantren);
        }
        // cout << "cnt = " << cnt << " N = " << N << endl;
        // cout << maxx << " " << minx << endl;
        if ((maxx >= minx) && (cnt == N)) ++ans;
    }
    res = max(res, ans);
}

void hv(int i) {
    FOR(j, 1, P)  if (dd[j] == 0) {
        dd[j] = 1;
        kq[i] = j;
        if (i == P) ghinhan();
        else hv(i + 1);
        dd[j] = 0;
    }
}

void solve() {
    if (N == 1) {
        int ans = 0;
        FOR(i, 1, P) {
            int canduoi = (100 * q[N][i]) / (110 * r[N]);
            if ((100 * q[N][i]) % (110 * r[N])) ++canduoi;
            //minx = max(minx, canduoi);
            int cantren = (100 * q[N][i]) / (90 * r[N]);
            if (cantren < canduoi) continue;
            ++ans;
        }
        cout << ans << endl;
    }
    else {
        // cout << "pass" << endl;
        SET(dd, 0);
        hv(1);
        cout << res << endl;
   }
}

int main() {

    #ifndef ONLINE_JUDGE
    freopen("B-small-attempt2.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int test;
    cin >> test;
    FOR(t, 1, test) {
        enter();
        cout << "Case #" << t << ": ";
        res = 0;
        solve();
    }
    return 0;
}

