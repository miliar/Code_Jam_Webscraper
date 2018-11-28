#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        int k, ans = 0;
        cin >> s >> k;
        for (int i = 0, len = s.size(); i <= len-k; ++i)
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j)
                    if (s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                ++ans;
            }
        bool ok = true;
        for (int i = 0, len = s.size(); i < len; ++i)
            if (s[i] == '-') {
                ok = false;
                break;
            }
        cout << "Case #" << t << ": ";
        if (ok)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}