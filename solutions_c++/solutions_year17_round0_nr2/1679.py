#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
#define INF 18000000000000000

int N;

template <typename Tf, typename Ti>
Tf exponent(Tf x, Ti n) {
    Tf P = Tf(1);
    while (n > 0) {
        if ((n & 1) != 0)
            P = P * x;
        x = x * x;
        n >>= 1;
    }
    return P;
}

bool ok(ull k, int& power) {
    power = 0;
    int latest = 9;
    while (k > 0) {
        int digit = k % 10;
        if (digit > latest || digit == 0) return false;
        latest = digit;
        k /= 10;
        ++power;
    }
    return true;
}

ull solve(ull k) {
    int power = 0;
    while (!ok(k, power)) {
        //cout << k << " " << power << endl;
        ull exp = exponent(10ull, power);
        if (k % exp == 0) --k;
        else k -= exponent(10ull, power-1);
    }
    return k;
}

int main()
{
    cin >> N;
    for (int i = 1; i <= N; ++i) {
        ull K; cin >> K;
        cout << "Case #" << i << ": " << solve(K) << endl;
    }

    return 0;
}

