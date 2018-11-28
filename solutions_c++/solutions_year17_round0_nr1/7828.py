#include <fstream>
#include <string>

using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("A-large.out");

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        int k, ans = 0;
        cin >> s >> k;
        cout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < s.length() - k + 1; ++j) {
            if (s[j] == '-') {
                for (int q = j; q < j + k; q++) {
                    if (s[q] == '-') {
                        s[q] = '+';
                    } else {
                        s[q] = '-';
                    }
                }
                ++ans;
            }
        }
        for (int j = 0; j < s.length(); ++j) {
            if (s[j] == '-') {
                s = "";
                cout << "IMPOSSIBLE" << endl;
                break;
            }
        }
        if (s != "") {
            cout << ans << endl;
        }
    }
    return 0;
}
