#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<iostream>

#define eps 1e-10
#define INF (1<<30)
#define PI acos(-1.0)
using namespace std;
typedef long long ll;

int a[110];

int main() {
    freopen("/Users/vino/Desktop/A-small-attempt2.in", "r", stdin);
    freopen("/Users/vino/Desktop/A-small-attempt2.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        int n, p;
        cin >> n >> p;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        int ans = 0;
        if (p == 2) {
            int s = 0;
            for (int i = 1; i <= n; i++) {
                if (a[i] % 2 == 0)
                    ans++;
                else s++;
            }
            ans += s + 1 >> 1;
        } else if (p == 3) {
            int s1 = 0, s2 = 0;
            for (int i = 1; i <= n; i++) {
                if (a[i] % 3 == 0) {
                    ans++;
                } else if (a[i] % 2 == 1) {
                    s1++;
                } else {
                    s2++;
                }
            }
            if (s1 > s2) {
                ans += s2 / 3;
                ans += (s1 - s2 + 2) / 3;
            } else {
                ans += s1 / 3;
                ans += (s2 - s1 + 2) / 3;
            }
        }
        cout << ans << endl;
    }

    return 0;
}