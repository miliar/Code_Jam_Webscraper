#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n,p,c[4];

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        cin >> n >> p;
        c[0] = c[1] = c[2] = c[3] = 0;
        for (int i = 0; i < n; i++) {
            int g;
            cin >> g;
            c[g % p]++;
        }

        int ans = c[0];
        if (p == 2) {
            ans += (c[1] + 1) / 2;
        }
        if (p == 3) {
            while (c[1] > 0 && c[2] > 0) {
                ans++;
                c[1]--;
                c[2]--;
            }
            ans += (c[1] + 2) / 3;
            ans += (c[2] + 2) / 3;
        }
        if (p == 4) {
            while (c[1] > 0 && c[3] > 0) {
                ans++;
                c[1]--;
                c[3]--;
            }
            int a = c[1] + c[3];
            int b = c[2];

            int ans1 = ans;
            ans1 += b / 2;
            b = b % 2;
            if (b && a > 1) {
                ans1++;
                b--;
                a -= 2;
            }
            ans1 += a / 4;
            if (b || a % 4) ans1++;

            a = c[1] + c[3];
            b = c[2];
            int ans2 = ans;
            while (a > 1 && b > 0) {
                ans2++;
                b--;
                a -= 2;
            }
            ans2 += b / 2;
            ans2 += a / 4;
            if (b % 2 || a % 4) ans2++;

            ans = max(ans1, ans2);
        }

        cout << "Case #" << TC << ": ";
        cout << ans << '\n';
    }
}
