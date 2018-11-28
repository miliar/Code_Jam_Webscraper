#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; _++) {
        string s;
        cin >> s;
        int p = 0;
        while (p < s.size() - 1 && s[p] <= s[p + 1]) {
            p++;
        }
        if (p == s.size() - 1) {
            cout << "Case #" << _ << ": " << s << endl;
        } else {
            while (p > 0 && s[p] == s[p - 1]) {
                p--;
            }
            s[p]--;
            p++;
            for (int i = p; i < s.size(); i++) {
                s[i] = '9';
            }
            // remove leading zero's of s
            int pos = 0;
            while (s[pos] == '0') {
                pos++;
            }
            s = s.substr(pos);
            cout << "Case #" << _ << ": " << s << endl;
        }
        
    }
    return 0;
}