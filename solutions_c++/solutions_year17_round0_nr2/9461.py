#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <iomanip>
using namespace std;

#define INF 1e+9
#define mp make_pair
#define lint long long

lint pow10(int k) {
    lint res = 1;
    for (int i = 0; i < k; i++) {
        res *= 10;
    }
    return res;
}

lint in;

int digit(int k) {
    return (in / pow10(k)) % 10;
}

int main() {
    ios_base::sync_with_stdio(false);
    cout << setprecision(10) << fixed;
freopen("", "r", stdin);
freopen("", "w", stdout);
    int t;
    cin >> t;
    const int dig_max = 18;
    const int dig_min = 0;
    for (int i = 0; i < t; i++) {
        cin >> in;
        lint best = 0;
        for (int j = dig_max; j >= dig_min; j--) {
            if (j == dig_min)
                best = max(best, in);
            else {
                if (digit(j) == 0)
                    continue;
                if (j == dig_max || 
                     digit(j + 1) < digit(j)) {
                    lint p = pow10(j);
                    best = max(best, in - (in % p) - 1);
                }
                if (digit(j) > digit(j - 1))
                    break;
            }
        }
        cout << "Case #" << i + 1 << ": " << best << endl;
    }

}
