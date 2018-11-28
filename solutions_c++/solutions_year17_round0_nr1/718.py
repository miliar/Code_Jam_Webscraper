#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

const int N = 1005;
int T, k;
char s[N];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    int cas = 0;
    while (T--) {
        scanf("%s%d", s, &k);
        int n = strlen(s);
        int cnt = 0;
        for (int i = 0; i < n - k + 1; i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j++) {
                    if (s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
                cnt++;
            }
        }
        int f = 1;
        for (int i = 0; i < n; i++) if (s[i] == '-') f = 0;
        printf("Case #%d: ", ++cas);
        if (!f) printf("IMPOSSIBLE\n");
        else printf("%d\n", cnt);
    }
    return 0;
}
