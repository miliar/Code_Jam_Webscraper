#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main() {
    int nt;
    cin >> nt;
    char s[1010];
    int k;
    for (int t = 1; t <= nt; ++t) {
        cin >> s >> k;
        int nrev = 0;
        int count = 0;
        for (int p = 0; p <= strlen(s) - k; ++p) {
            if (s[p] == '-') {
                for (int i = p; i < p + k; ++i) {
                    if (i < strlen(s)) {
                        s[i] = (s[i] == '+') ? '-' : '+';
                    }
                }
                ++count;
            }
        }
        int mcount = 0;
        int impossible = 0;
        for (int p = 0; p < strlen(s); ++p) {
            if (s[p] == '-') {
                ++mcount;
            } else if (mcount > 0) {
                if (mcount < k) {
                    impossible = 1;
                    break;
                }
            }
            if (mcount == k) {
                ++count;
                mcount = 0;
            }
        }
        if (mcount > 0 && mcount < k) {
            impossible = 1;
        }
        cout << "Case #" << t << ": ";
        if (impossible) {
            cout << "IMPOSSIBLE";
        } else {
            cout << count;
        }
        cout << endl;
    }
    return 0;
}