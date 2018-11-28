#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; ++i) {
        string s;
        cin >> s;
        for (int k = s.length() - 2; k >= 0; --k) {
            if (s[k] > s[k + 1]) {
                --s[k];
                for (int j = k + 1; j < s.length(); ++j) {
                    s[j] = '9';
                }
            }
        }
        while (s.length() > 1 && s[0] == '0') {
            s.erase(0, 1);
        }
        cout << "Case #" << i+1 << ": " << s << endl;
    }
    return 0;
}
