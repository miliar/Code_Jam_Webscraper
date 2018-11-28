#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

typedef unsigned long long int ulli;

int main() {
    int t;
    ulli n, k;
    cin >> t;
    for (int i = 1; i < t+1; ++i) {
        cin >> n >> k;
        ulli level = (ulli)log2(k);
        ulli m = 1 << level;
        ulli avg = (n - m + 1) / m;
        ulli rem = (n - m + 1) % m;
        ulli numStalls = (k-m >= rem) ? avg-1 : avg;
        ulli ls = numStalls/2;
        ulli rs = numStalls-ls;
        cout << "Case #" << i << ": " << rs << " " << ls << endl;
    }
    return 0;
}
