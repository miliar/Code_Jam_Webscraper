#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int times = 0; times < T; times++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i < s.size() - k + 1; i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j++) {
                    if (s[i+j] == '-') {
                        s[i+j] = '+';
                    } else {
                        s[i+j] = '-';
                    }
                }
                ans++;
            }
        }
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                ans = -1;
                break;
            }
        }

        cout << "Case #" << times + 1 << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
