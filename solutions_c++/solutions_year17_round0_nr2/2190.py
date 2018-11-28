#include <iostream>
#include <string>

using namespace std;

int main() {

    int n, len, opt[20];

    cin >> n;

    string s;

    for (int i = 0; i < n; i++) {
        cin >> s;
        len = s.size();
        for (int j = 0; j < len; j++) {
            opt[j] = s[j] - '0';
        }
        for (int j = 0; j < len - 1; j++) {
            if (opt[j] > opt[j + 1]) {
                int digit = j;
                opt[digit] -= 1;
                while (digit > 0 && opt[digit] < opt[digit - 1]) {
                    digit--;
                    opt[digit] -= 1;
                }
                for (int k = digit + 1; k < len; k++) {
                    opt[k] = 9;
                }
                break;
            }
        }

        cout << "Case #" << i + 1 << ": ";
        if (opt[0]) cout << opt[0];
        for (int j = 1; j < len; j++) {
            cout << opt[j];
        }
        cout << endl;

    }

    return 0;
}