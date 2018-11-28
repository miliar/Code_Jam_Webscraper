#include <iostream>
using namespace std;

void convert(string& s, int pos, int len) {
    for (int i = pos; i < pos + len; i++) {
        if (s[i] == '-')
            s[i] = '+';
        else if (s[i] == '+')
            s[i] = '-';
    }
}

int main () {
    int t; cin >> t;
    int cnt = 0;
    while (t--) {
        cnt++;
        string s; 
        cin >> s;
        int k; cin >> k;
        int ans = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-' && (s.size() - i) >= k) {
                convert(s, i, k);
                ans++;
            }
        }
        bool ok = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-')
                ok = false;
        }

        cout << "Case #" << cnt << ": ";
        if (ok) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;

    }

    return 0;
}
