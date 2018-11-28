#include <iostream>
#include <string>

using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        string s; cin >> s;
        int a[20], b[20];
        int n = s.size();
        for (int i = 0; i < n; i++) { 
            a[i] = (int)s[i]-'0';
        }
        int r = 0;
        while (r < n-1) {
            if (a[r] <= a[r+1]) {
                r++;
            }
            else break;
        }
        if (r == n-1) {
            for (int i = 0; i < n; i++) b[i] = a[i];
        }
        else {
            int minus = 0;
            for (int i = 0; i < r; i++) {
                if (a[i] < a[i+1]) {
                    minus = i+1;
                }
            }
            for (int i = 0; i < n; i++) {
                if (i < minus) b[i] = a[i];
                else if (i == minus) b[i] = a[i]-1;
                else b[i] = 9;
            }
        }
        cout << "Case #" << t << ": ";
        for (int i = 0; i < n; i++) {
            if (b[i] != 0) {
                cout << b[i];
            }
        }
        cout << '\n';
    }
    return 0;
}  