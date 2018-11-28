#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;
using ll = long long;

#define FU(i, a, b) for (auto i = (a); i < (b); ++i)
#define fu(i, b) FU(i, 0, b)
#define FD(i, a, b) for (auto i = (b) - 1; i >= (a); --i)
#define fd(i, b) FD(i, 0, b)
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb emplace_back

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        char s[10000];
        for (int i = 0; i < 10000; ++i)
            s[i] = '\0';
        int k;
        // cin >> s >> k;
        scanf("%s %d", s, &k);
        bool ok = true;
        int res = 0;
        for (int i = 0, e = strlen(s); i < e; ++i) {
            if (s[i] == '-') {
                ok = i <= e - k;
                ++res;
                for (int j = i; j < i + k; ++j) {
                    s[j] = s[j] == '-' ? '+' : '-';
                }
            }
        }
        cout << "Case #" << t << ": "
             << (ok ? to_string(res) : "IMPOSSIBLE") << endl;
    }
    return 0;
}
