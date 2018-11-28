#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        vector<int> a(n, 0);
        int f = 0;
        int c = 0;
        for (int i = 0; i <= n - k; i++) {
            if (i >= k) c -= a[i - k];
            if ((s[i] == '+' && c % 2 == 1) || (s[i] == '-' && c % 2 == 0)) {
                a[i] = 1;
                f++;
                c++;
            }
        }
        bool good = true;
        for (int i = n - k + 1; i < n; i++) {
            if (i >= k) c -= a[i - k];
            if ((s[i] == '+' && c % 2 == 1) || (s[i] == '-' && c % 2 == 0)) {
                good = false;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if (good) {
            cout << f;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}