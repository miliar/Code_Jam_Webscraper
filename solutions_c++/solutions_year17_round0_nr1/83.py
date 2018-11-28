#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#define MAXN 1010

using namespace std;

string s;
int k;
int a[MAXN];

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        cin >> s >> k;
        int n = s.size();
        memset(a,0,sizeof(a));

        bool ok = 1;
        int ans = 0, flips = 0;
        for (int i = 0; i <= n; i++) {
            flips ^= a[i];
            int x = s[i] == '-';
            if (x ^ flips) {
                if (i + k > n) {
                    ok = 0;
                    break;
                }
                ans++;
                flips ^= 1;
                a[i+k] ^= 1;
            }
        }

        cout << "Case #" << TC << ": ";
        if (ok) cout << ans << '\n';
        else cout << "IMPOSSIBLE\n";
    }
}
