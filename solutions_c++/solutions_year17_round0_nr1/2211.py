#include <iostream>
#include <string>

using namespace std;

int main() {

    string s;
    int n, k, ans, len;
    bool opt[1010];

    cin >> n;

    for (int i = 0; i < n; i++) {
        ans = 0;
        cin >> s >> k;
        len = s.size();
        for (int j = 0; j < len; j++) {
            if (s[j] == '+') {
                opt[j] = true;
            }
            else {
                opt[j] = false;
            }
        }
        for (int j = 0; j <= len - k; j++) {
            if (!opt[j]) {
                ans++;
                for (int l = j; l < j + k; l++) {
                    opt[l] = not opt[l];
                }
            }
        }
        for (int j = len - k + 1; j < len; j++) {
            if (!opt[j]) {
                ans = -1;
                break;
            }
        }

        if (ans < 0) {
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << i + 1 << ": " << ans << endl;
        }

    }

    return 0;
}