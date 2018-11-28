#include <iostream>
using namespace std;

void solve() {
    string s;
    cin >> s;
    if (s.size() == 1) {
        cout << s << "\n";
        return;
    }

    int r = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] < s[i - 1])
            break;
        r = i;
    }

    if (r + 1 == s.size()) {
        cout << s << "\n";
        return;
    }

    while (r > 0 && s[r] == s[r- 1]) {
        r--;
    }

    if (s[r] == '1') {
        int len = s.size() - 1;
        s = "";
        for (int i = 0; i < len; i++)
            s += "9";
    } else {
        s[r]--;
        for (int i = r + 1; i < s.size(); i++) {
            s[i] = '9';
        }
    }

    cout << s << "\n";
}

int main() {

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
