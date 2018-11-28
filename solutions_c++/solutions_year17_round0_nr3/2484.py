#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main() {
    int T;
    long long n, k;
    long long l, r;
    int t;
    bool flag;

    cin >> T;
    for (int Ti = 0; Ti < T; ++Ti) {
        cin >> n >> k;
        while (k > 0) {
            t = k&1;
            k >>= 1;

            if ((n&1) == 1)
                l = r = (n-1) >> 1;
            else {
                l = (n >> 1) - 1;
                r = (n >> 1);
            }

            n = t? l:r;
        }

        cout << "Case #" << Ti+1 << ": " << r << " " << l << endl;
    }

    return 0;
}
