#include <iostream>
#include <string>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for (int c = 1; c <= tc; ++c) {
        string str;
        int k;
        cin >> str >> k;
        int ans = 0;
        for (int i = 0; i + k <= str.size(); ++i) {
            if (str[i] == '-') {
                ++ans;
                for (int j = 0; j != k; ++j) {
                    if (str[i + j] == '-') {
                        str[i + j] = '+';
                    } else {
                        str[i + j] = '-';
                    }
                }
            }
        }
        for (int i = str.size() - k + 1; i != str.size(); ++i) {
            if (str[i] == '-') {
                ans = -1;
                break;
            } 
        }
        cout << "Case #" << c << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    } 
    return 0; 
}