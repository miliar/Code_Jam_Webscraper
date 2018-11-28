#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define PI acos(-1)
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
const int M = 1005;
double dp[M][M][3];
bool visit[M][M][3];
pair<double, double> a[M];
int n, k;
double calc(int i, int cur, bool atleast) {
        if(i == n) {
                if(cur == k) {
                        return 0;
                }
                return -1e18;
        }
        if(cur > k) {
                return -1e18;
        }
        if(visit[i][cur][atleast]) {
                return dp[i][cur][atleast];
        }
        visit[i][cur][atleast] = 1;
        double ans = -1e18;
        if(!atleast) {
                ans = max(ans, calc(i + 1, cur + 1, 1) + PI * (2.0 * a[i].f * a[i].s + a[i].f * a[i].f));
        } else {
                ans = max(ans, calc(i + 1, cur + 1, 1) + 2.0 * PI * a[i].f * a[i].s);
        }
        ans = max(ans, calc(i + 1, cur, atleast));
        return dp[i][cur][atleast] = ans;
}
int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cin >> n >> k;
                for(int i = 0; i < n; i++) {
                        cin >> a[i].f >> a[i].s;
                }
                sort(a, a + n, greater<pair<double, double> > ());
                printf("Case #%d: %.12lf\n", c, calc(0, 0, 0));
                memset(visit, 0, sizeof visit);
        }
        return 0;
}
