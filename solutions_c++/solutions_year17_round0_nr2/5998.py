#include <iostream>
#include <string>

using namespace std;

int t, n;
string s;

int main() {
    cin >> t;
    for (int c = 0; c ++< t;) {
        cout << "Case #" << c << ": ";
        cin >> s;
        n = s.length();
        int i = 0;
        while (i + 1 < n && s[i] <= s[i+1]) ++i;
        if (i < n - 1) {
            while (i > 0 && s[i-1] == s[i]) --i;
            --s[i];
            for (int j = i + 1; j < n; ++j) s[j] = '9';
            for (int j = i; j --> 0;) s[j] = min(s[j], s[j+1]);
        }
        bool l = 0;
        for (char c : s) if (l || c > '0') l = 1, cout << c;
        cout << '\n';
    }
    return 0;
}
