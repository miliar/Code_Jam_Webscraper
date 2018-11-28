#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    unsigned int t;
    long x;
    char buf[20];

    cin >> t;
    for (unsigned int k = 1; k <= t; k++) {
        cin >> x;
        int sz = sprintf(buf, "%ld", x);

        for (unsigned int i = sz - 1; i > 0; i--) {
            if (buf[i-1] > buf[i]) {
                buf[i] = '\0';

                long y;
                sscanf(buf, "%ld", &y);
                --y;
                sprintf(buf, "%0*ld", i, y);

                for (int j = i; j < sz; j++) buf[j] = '9';

            }
        }
        sscanf(buf, "%ld", &x);
        cout << "Case #" << k << ": " << x << endl;
    }

    return 0;
}
