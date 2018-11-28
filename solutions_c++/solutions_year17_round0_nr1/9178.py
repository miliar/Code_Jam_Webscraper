#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        string s; cin >> s;
        int sz; cin >> sz;
        int j = 0;
        int flip = 0;
        while (j <= s.length() - sz) {
            if (s[j] == '+') j += 1;
            else {
                flip += 1;
                for (int k = j; k < j + sz; k++) {
                    s[k] = s[k] == '+' ? '-' : '+';
                }
            }
        }

        bool check = true;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-') {
                check = false;
                break;
            }
        }

        if (check) {
            cout << "Case #" << i << ": " << flip << endl;
        } else {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
