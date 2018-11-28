#include <bits/stdc++.h>
#define MAX_N 1005
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define LOWBIT(x) ( (x) & -(x) )

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

int dx[] = {0 , -1 , 0 , 1};
int dy[] = {1 , 0 , -1 , 0};

int test;

struct cake {
    ll R , H;

    bool operator < (const cake &hs) const {
        return R > hs.R;
    }

    double S;
};

int n , k;
cake a[MAX_N];
long long dp[MAX_N][MAX_N];

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";

        cin >> n >> k;

        FOR(i , 1 , n) cin >> a[i].R >> a[i].H;

        sort(a + 1 , a + n + 1);

        FOR(i , 0 , n)
            FOR(j , 0 , k) dp[i][j] = 0;

        dp[1][1] = a[1].R * a[1].R + 2 * a[1].R * a[1].H;

        FOR(i , 2 , n) dp[i][1] = max(dp[i - 1][1] , a[i].R * a[i].R + 2 * a[i].R * a[i].H);

        FOR(i , 2 , n)
            FOR(j , 2 , k)
                dp[i][j] = max(dp[i - 1][j] , dp[i - 1][j - 1] + 2LL * a[i].R * a[i].H);

        double res = 0.0;
        if (k == 1) {
            FOR(i , 1 , n) res = max(res , (double) dp[i][1]);
        }
        else res = (double) dp[n][k];

        res *= pi;

        cout << fixed << setprecision(20) << res << endl;
    }

	return 0;
}
