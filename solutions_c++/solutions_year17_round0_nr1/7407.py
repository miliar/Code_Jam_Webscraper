#include <iostream>

using namespace std;

int main() {
    int T; cin >> T;
    for (int test = 1; test <= T; ++test) {
        string s; int k;
        cin >> s >> k;
        
        int len = s.length();

        for (int i = 0; i < len; ++i) s[i] = (s[i] == '+') ? 1 : 0;
        
        int flips = 0;

        for (int i = 0; i <= len - k; ++i) {
            if (s[i] == 0) {
                ++flips;
                for (int j = i; j < i + k; ++j) s[j] = 1 - s[j];
            }
        }

        bool possible = true;

        for (int i = len - k + 1; i < len; ++i) {
            possible &= (s[i] == 1);
        }

        cout << "Case #" << test << ": ";
        if (possible) cout << flips << endl;
        else cout << "IMPOSSIBLE" << endl;
        
    }
    return 0;
}
