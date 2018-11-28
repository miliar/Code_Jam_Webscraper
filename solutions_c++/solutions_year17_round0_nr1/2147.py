#include <iostream>

using namespace std;

int main() {
    //freopen("/Users/philip/Downloads/A-large.in", "r", stdin);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        int m, k;
        cin >> s >> k;
        m = (int)s.size();
        int c = 0;
        bool f = 1;
        for (int j = 0; j < m; j++) {
            if (s[j] == '-') {
                if (j + k > m) {
                    f = 0;
                    break;
                }
                for (int l = j; l < j + k; l++) {
                    s[l] = (char)('+' + '-' - s[l]);
                }
                c++;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (f) {
            cout << c << '\n';
        }
        else {
            cout << "IMPOSSIBLE\n";
        }
    }
}
