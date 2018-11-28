#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

void solve() {
    string s;
    cin >> s;
    int fall = -1;
    for (int i = 0; i < s.size() - 1; ++i) {
        if (s[i] > s[i + 1]) {
            fall = i;
            break;
        }
    }
    if (fall == -1) {
        cout << s << endl;
        return;
    }
    int rise = -1;
    for (int i = 0; i < fall; ++i) {
        if (s[i] < s[i + 1]) {
            rise = i;
        }
    }
    if (rise == -1) {
        if (s[0] == '1') {
            cout << string(s.size() - 1, '9') << endl;
            return;
        } else {
            rise = -1;
        }
    }
    s[rise + 1] -= 1;
    for (int i = rise + 2; i < s.size(); ++i) {
        s[i] = '9';
    }
    cout << s << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
