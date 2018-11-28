#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;
typedef long long ll;
#define mp make_pair
#define fi first
#define se second
#define pb push_back

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fll;
const int MAX_N = 10010;

int T, n, cases = 0;
char str[1010];

int solve() {
    int len = strlen(str), ans = 0;
    for (int i = 0; i < len; ++i) {
        if (str[i] == '-') {
            ans++;

            if (i + n - 1 >= len) return -1;
            
            for (int j = 0; j < n; ++j) {
                if (str[i + j] == '-') str[i + j] = '+';
                else str[i + j] = '-';
            }
        }
    }
    return ans;
}

int main() {    
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        scanf("%s", str);
        scanf("%d", &n);

      //  printf("%s %d\n", str, n);
        int ans = solve();
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", ++cases);
        else printf("Case #%d: %d\n", ++cases, ans);
    }
    return 0;
}
    
