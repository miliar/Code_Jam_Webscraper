#include <bits/stdc++.h>
#define D printf

using ll = long long;

ll digits[20];

ll ten(int pow) {
    ll res = 1;
    while (pow > 0) {
        pow--;
        res = res * 10;
    }
    return res;
}


int main() {
    FILE * inf = stdin;
    int nCas;
    fscanf(inf, "%i", &nCas);
    for (int cas = 0; cas < nCas; cas++) {
        ll num;
        fscanf(inf, "%lli", &num);
        while (1) {
            int nd = 0;
            ll tmp = num;
            while (tmp >= 10) {
                digits[nd] = tmp % 10;
                nd++;
                tmp = tmp / 10;
            }
            if (tmp != 0) {
                digits[nd] = tmp;
                nd++;
            }

            if (nd == 1) {
                printf("Case #%i: %lli\n", cas+1, num);
                break;
            }

            ll prev = 0;
            for (int i = nd-1; i >= 0; i--) {
                if (digits[i] < prev) {
                    // prev is the "problem digit".
                    // Decrement it and set the remainder to 9
                    digits[i+1]--;
                    for (int j = i; j >= 0; j--) {
                        digits[j] = 9;
                    }
                    break;
                }
                prev = digits[i];
            }

            ll newnum = 0;
            bool good = true;
            prev = 0;
            for (int i = nd-1; i >= 0; i--) {
                if (digits[i] < prev) {
                    good = false;
                }
                newnum *= 10;
                newnum += digits[i];
                prev = digits[i];
            }
            num = newnum;
            if (good) {
                printf("Case #%i: %lli\n", cas+1, num);
                break;
            }
        }
    }
    return 0;
}
