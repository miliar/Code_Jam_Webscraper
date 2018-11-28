#include <iostream>
#include <vector>

using namespace std;


string find(string s) {
    string ans = "";
    int len = s.length();
  
    for (int i = 0; i < len; i++) {
        for (int d = 9; d >= 0; d--) {
            string suffix = "";
            char c = (char)('0' + d);
            suffix.insert(0, len - i, c);
            if ((ans + suffix) <= s) {
                ans += c;
                break;
            }
        }
    }
    int index;
    
    for (index = 0; index < len; index++) {
        if (ans[index] != '0') {
            break;
        }
    }
    return ans.substr(index);
}

int main() {
    int t;
    cin >> t;

    for (int kase = 1; kase <= t; kase++) {
        string s;
        cin >> s;
        string ans = find(s);
        cout << "Case #" << kase << ": " << ans << endl;
    }
}