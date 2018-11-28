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
const int M = 105;
int dp[5][M * M * M], a[5];
int n, p;
int calc(int rem, int c) {
        if(!c)
                return 0;
        int h = a[1] * 10000 + a[2] * 100 + a[3];
        if(dp[rem][h] != -1)
                return dp[rem][h];
        int ans = 0;
        for(int i = 1; i < p; i++) {
                if(!a[i])continue;
                a[i]--;
                if(rem >= i) {
                        ans = max(ans, !rem + calc(rem - i, c - 1));
                } else {
                        ans = max(ans, !rem + calc((p - i + rem) % p, c - 1));
                }
                a[i]++;
        }
        return dp[rem][h] = ans;
}
int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cin >> n >> p;
                memset(a, 0, sizeof a);
                memset(dp, -1, sizeof dp);
                int ans = 0;
                for(int i = 0; i < n; i++) {
                        int x;
                        scanf("%d", &x);
                        a[x % p]++;
                        ans += (x % p == 0);
                }
                cout << "Case #" << c << ": " << ans + calc(0, n - ans) << "\n";
        }
        return 0;
}
