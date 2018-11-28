#include <bits/stdc++.h>

using namespace std;

const int MAX = 1e2 + 7;
char number [MAX];

int main () {
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);

    int t;
    cin >> t;

    for (int kase = 1; kase <= t; kase++) {
        cin >> number;
        int len = strlen (number);

        for (int i = len - 1; i >= 1; i--) {
            if (number [i] < number [i - 1]) {
                for (int j = i; j < len; j++) {
                    number [j] = '9';
                }
                if (number [i - 1] == '0') {
                    number [i - 1] = '9';
                    for (int j = i - 2; j >= 0; j--) {
                        if (number [j] == '0') number [j] = '9';
                        else number [j]--;
                    }
                } else number [i - 1]--;
            }
        }
        long long n = 0;
        for (int i = 0; i < len; i++) {
            n *= 10;
            n += (number [i] - '0');
        }

        printf ("Case #%d: %lld\n", kase, n);
    }

    return 0;
}
