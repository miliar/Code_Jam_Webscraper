#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        string ans;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            for (int digit = '9'; digit >= '0'; digit--) {
                string cp = ans;
                for (int j = i; j < n; j++) {
                    cp += (char) digit;
                }
                if (cp <= s) {
                    ans += digit;
                    break;
                }
            }
        }
        cout << "Case #" << t << ": " << (ans[0] == '0' ? ans.substr(1) :  ans) << endl;
    }
    return 0;
}