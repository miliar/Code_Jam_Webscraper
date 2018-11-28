#include <bits/stdc++.h>

using namespace std;

char s[30];
int n, lg;

int main() {

    int i, j, k;

    cin >> n;
    for (i = 1; i <= n; i++) {

        cin >> s; lg = strlen(s);
        cout << "Case #" << i << ": ";

        if (lg == 1) {
            cout << s << '\n';
            continue;
        }

        for (j = lg - 1; j >= 2; j--)
            if (s[j] < s[j - 1]) {
                for (k = j; k < lg; k++)
                    s[k] = '9';
                s[j - 1]--;
            }

        if (s[0] > s[1]) {
            if (s[0] == '1') {
                for (j = 1; j < lg; j++)
                    cout << 9;
                cout << '\n';
                continue;
            }
            else {
                for (j = 1; j < lg; j++)
                    s[j] = '9';
                s[0]--;
            }
        }

        cout << s << '\n';
    }

    return 0;
}
