#include <bits/stdc++.h>
#define MAX_N 100100
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
int dp[1500][722][2];
int Ac , Aj;
bool markC[1500] , markJ[1500];

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";

        cin >> Ac >> Aj;

        FOR(i , 0 , 1440) markC[i] = markJ[i] = false;

        while (Ac--) {
            int l , r;
            cin >> l >> r;

            FOR(i , l , r) markC[i] = true;
        }

        while (Aj--) {
            int l , r;
            cin >> l >> r;

            FOR(i , l , r) markJ[i] = true;
        }

        FOR(i , 0 , 24 * 60)
            FOR(j , 0 , 720) dp[i][j][0] = dp[i][j][1] = inf;

        if (!markC[1]) dp[1][1][0] = 1;
        if (!markJ[1]) dp[1][1][1] = 1;

        FOR(i , 2 , 24 * 60)
            FOR(j , 0 , 720) {
                if (markC[i]) {
                    if (!j) continue;

                    dp[i][j][0] = min(dp[i][j][0] , min(dp[i - 1][j - 1][0] , dp[i - 1][j - 1][1] + 1));
                }
                else
                if (markJ[i]) {
                    if (j == i) continue;

                    dp[i][j][1] = min(dp[i][j][1] , min(dp[i - 1][j][0] + 1 , dp[i - 1][j][1]));
                }
                else {
                    if (j) dp[i][j][0] = min(dp[i][j][0] , min(dp[i - 1][j - 1][0] , dp[i - 1][j - 1][1] + 1));
                    if (j < i) dp[i][j][1] = min(dp[i][j][1] , min(dp[i - 1][j][0] + 1 , dp[i - 1][j][1]));
                }
            }

        cout << min(dp[24 * 60][720][0] , dp[24 * 60][720][1]) << endl;
    }

	return 0;
}
