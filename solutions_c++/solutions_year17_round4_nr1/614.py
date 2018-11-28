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
const ll mod = (ll)(1e9 + 7);
const int MAX_N = 100010;

int T, n, P, cases = 0;
int num[5], data[MAX_N];

int main() {       

     freopen("1.in", "r", stdin);
     freopen("1.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &P);
        memset(num, 0, sizeof (num));

        for (int i = 0; i < n; ++i) {
            scanf("%d", &data[i]);
            num[data[i] % P]++;
        }

        int ans = num[0];
        if (P == 2) {
            ans += (num[1] + 1) / 2;
        } else if (P == 3) {
            if (num[1] > num[2]) swap(num[1], num[2]);

            ans += num[1] + (num[2] - num[1] + 2) / 3;
        } else {
            if (num[1] > num[3]) swap(num[1], num[3]);

            ans += num[1];
            num[3] -= num[1];
            int Max = 0;
            for (int i = 0; i <= n; ++i) {
                int base = i;
                int Left = num[3] - i * 4;
                if (Left < 0) break;

                if (Left / 2 > num[2]) {
                    base += num[2];
                    Left -= 2 * num[2];
                    if (Left) {
                       // base += (Left + 3) / 4;4
                        base++;
                    }
                } else {
                    base += Left / 2;
                    int t = num[2] - Left / 2;
                    base += t / 2;
                    if ((Left % 2) || (t % 2)) base++;
                }
                Max = max(Max, base);
            }
            ans += Max;
        }
        printf("Case #%d: %d\n", ++cases, ans);
    }

    return 0;
}
    
