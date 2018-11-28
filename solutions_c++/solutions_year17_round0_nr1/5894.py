#include <bits/stdc++.h>

using namespace std;

int main() {
        ios_base::sync_with_stdio(false);
        int tests;
        cin >> tests;
        for(int tc = 1; tc <= tests; ++tc) {
                string s; int k;
                cin >> s >> k;
                int count = 0, n = s.length();
                for(int i = 0; i + k <= n; ++i) {
                        if(s[i] == '-') {
                                for(int j = 0; j < k; ++j) {
                                        s[i + j] = s[i + j] == '+' ? '-' : '+';
                                }
                                ++count;
                        }
                }
                for(int i = 0; s[i]; ++i) {
                        if(s[i] == '-') {
                                count = -1;
                        }
                }
                if(~count) {
                        cout << "Case #" << tc << ": " << count << endl;
                } else {
                        cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
                }
        }
        return 0;
}
