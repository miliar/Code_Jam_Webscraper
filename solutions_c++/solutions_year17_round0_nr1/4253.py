#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string s;
        int K;
        int ans = 0;
        cin >> s >> K;
        cout << "Case #" << i+1 << ": ";
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == '-') {
                if (j + K > s.size()) {
                    cout << "IMPOSSIBLE";
                    ans = -1;
                    break;
                }
                ans++;
                for (int k = 0; k < K; ++k) {
                    if (s[j+k] == '-')
                        s[j+k] = '+';
                    else
                        s[j+k] = '-';
                }
            }
        }
        if (ans >= 0)
            cout << ans;
        cout << '\n';
    }
    return 0;
}
