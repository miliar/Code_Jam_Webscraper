#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int main() {
    int t, cas = 1;
    cin >> t;
    while (t--) {
        string n;
        cin >> n;
        string s = n;
        for (int i = n.size() - 1; i >= 1; --i) {
            if (s[i] < s[i - 1]) {
                s[i] = '9';
                s[i - 1] -= 1;
            }
        }
        bool change = false;
        for (int i = 0; i < n.size(); ++i) {
            if (change)
                s[i] = '9';
            if (s[i] == '9')
                change = true;
        }
        LL ans = stoll (s);
        cout << "Case #" << cas << ": " << ans << '\n';
        cas += 1;
    }
	return 0;
}

