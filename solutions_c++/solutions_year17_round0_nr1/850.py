#include <bits/stdc++.h>

using namespace std;

const int oo = 1e6;

int main() {
    ifstream cin ("A-large.in");
    ofstream cout ("pancake.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++) {
        cout << "Case #" << ttest << ": ";

        string s;
        cin >> s;
        int k;
        cin >> k;

        int ans = 0;
        for (int i = 0; i + k - 1 < s.length(); i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = i; j <= i + k - 1; j++) {
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') ans = oo;
        }

        if (ans == oo) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
    }
}
