#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int casen = 1; casen <= T; ++casen) {
        string s;
        int k;
        cin >> s >> k;
        int r = 0;
        for (int i = 0; i <= int(s.size()) - k; ++i) {
            if (s[i] == '-') {
                ++r;
                for (int j = 0; j < k; ++j) {
                    if (s[i+j] == '-') {
                        s[i+j] = '+';
                    } else {
                        s[i+j] = '-';
                    }
                }
            }
        }
        std::cout << "Case #" << casen << ": ";
        if (s != string(s.size(), '+')) {
            cout << "IMPOSSIBLE";
        } else {
            cout << r;
        }
        cout << endl;
    }
}
