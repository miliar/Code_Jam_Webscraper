#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;

#define SZ(c) c.size()
#define ALL(c) c.begin(), c.end()
#define endl '\n'

const int N = 1e5 + 9;

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("outp.txt", "w", stdout);
#endif

    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                if (i + k > s.size()) {
                    ans = -1;
                    break;
                }

                for (int j = i; j < i + k; ++j)
                    s[j] = (s[j] == '-' ? '+' : '-');

                ++ans;
            }
        }

        cout << "Case #" << c << ": ";

        if (ans == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;

    }
    return 0;
}
