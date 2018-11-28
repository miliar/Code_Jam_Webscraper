#include <iostream>
using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        string str;
        bool flag = true;
        int k;
        int ans = 0;
        cin >> str >> k;
        for (int j = 0; j <= str.length() - k; j++) {
            if (str[j] == '-') {
                ans++;
                for (int l = j; l < j + k; l++) {
                    if (str[l] == '-') str[l] = '+';
                    else str[l] = '-';
                }
            }
        }
        cout << "Case #" << i << ": ";
        for (int j = str.length() - k + 1; j < str.length(); j++) {
            if (str[j] == '-') {
                cout << "IMPOSSIBLE" << endl;
                flag = false;
                break;
            }
        }
        if (flag) cout << ans << endl;
    }
}
