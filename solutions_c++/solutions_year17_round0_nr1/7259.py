#include <bits/stdc++.h>
using namespace std;
int main() {

    freopen("pancake.in", "r", stdin);
    freopen("pancake.out", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s;
        int k, cnt = 0;

        cin >> s >> k;
        cout << "Case #" << i << ": ";

        for (int j = 0; j < s.size(); j++) {

            if ((s[j] == '-') && (j+k-1 <= s.size()-1)) {
                for (int l = j; l <= (j+k-1); l++)
                    if (s[l] == '-') s[l] = '+'; else s[l] = '-';
                cnt++;
            }

        }

        for (int j = 0; j < s.size(); j++) {

            if (s[j] == '-') {
                cout << "IMPOSSIBLE" << endl;
                cnt = -1;
                break;
            }

        }

        if (cnt == -1) {
            continue;
        }

        cout << cnt << endl;
    }

    return 0;
}
