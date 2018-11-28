#include <iostream>
#include <string>
using namespace std;

int main() {
    int n; cin >> n;
    for (int m = 1; m <= n; m++) {
        string s; cin >> s;
        char right = '9';
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] > right) {
                s[i]--;
                for (int j = i + 1; j < s.length(); j++) {
                    s[j] = '9';
                }
            }
            right = s[i];
        }
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != '0') {
                break;
            }
            start++;
        }
        cout << "Case #" << m << ": " << s.substr(start, s.length() - start) << endl;

    }
}
