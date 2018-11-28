// https://code.google.com/codejam/contest/3264486/dashboard#s=p1
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
#include <memory>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;

inline bool is_tidy(unsigned long long n) {
    bool tidy = true;
    while (n >= 10) {
        if ((n % 10) < ((n/10) % 10))
            tidy = false;
        n /= 10;
    }
    return tidy;
}

int main() {
    int t; cin >> t;

    for (int i = 0; i < t; ++i) {
        unsigned long long n; cin >> n;

        cout << "Case #" << i+1 << ": ";

        while (n > 0) {
            //cout << n << endl;
            if (is_tidy(n)) {
                cout << n;
                break;
            }
            --n;
        }

        cout << endl;
    }

    return 0;
}
