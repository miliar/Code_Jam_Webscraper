#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);

    int t, i, j, caseCnt, startFlg, len;
    char a[32];

    cin >> t;

    caseCnt = 1;
    while(t--) {
        cin >> a;

        len = strlen(a);

        for (i=1; i<len; i++) {
            if (a[i] < a[i-1]) {
                for (j=i; j<len; j++) a[j] = '9';
                a[i-1] -= 1;
                i = 0; // 循环后i为1
            }
        }

        cout << "Case #" << caseCnt << ": ";
        startFlg = 0;
        for (i=0; i<len; i++) {
            if (startFlg == 0 && a[i] != '0') {
                startFlg = 1;
            }

            if (startFlg) {
                cout << a[i];
            }
        }
        cout << endl;

        caseCnt++;
    }

    return 0;
}
