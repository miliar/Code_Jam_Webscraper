#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int q=0; q<t; q++) {
        string s;
        int k;
        cin >> s;
        cin >> k;
        cout << "Case #" << q+1 << ": ";
        if (k > s.length()) {
            int flag = 1;
            for (int i=0; i<s.length(); i++) {
                if (s[i] == '-') flag = 0;
            }
            if (flag == 0) {
                cout << "IMPOSSIBLE" << endl;
            } else {
                cout << 0 << endl;
            }
            continue;
        }

        int ans = 0;
        for (int i=0; i<s.length()-k+1; i++) {
            if (s[i] == '-') {
                for (int j=0; j<k; j++) {
                    s[i+j] = (s[i+j]=='+') ? '-' : '+';
                }
                ans++;
            }
        }
        int flag = 1;
        for (int i=s.length()-k+1; i<s.length(); i++) {
            if (s[i] == '-') {
                flag = 0;
                break;
            }
        }
        if (flag == 1) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
