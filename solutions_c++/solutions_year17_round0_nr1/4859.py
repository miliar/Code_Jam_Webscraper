#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;

    for (int tc_i = 0; tc_i < tc; tc_i++) {
        string s;
        int k;
        cin >> s >> k;

        int res = 0;
        bool good = true;

        for (int i = 0; i < ((int)s.size() - k + 1); i++) {
            if (s[i] == '+') {
                continue;
            }

            res++;

            for (int j = i; j < (i + k); j++) {
                s[j] = s[j] == '+' ? '-' : '+';
            }
        }

        for (int i = 0; good && (i < (int)s.size()); i++) {
            good = s[i] == '+';
        }

        cout << "Case #" << (tc_i + 1) << ": ";

        if (good) {
            cout << res;
        }
        else {
            cout << "IMPOSSIBLE";
        }

        cout << endl;
    }

    return 0;
}