#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

typedef long long ll;

int log10(ll num) {
    int res = 0;
    while (num > 0) {
        num /= 10;
        res += 1;
    }
    return res;
}

vector<int> get_digits(ll num) {
    vector<int> digits;

    while (num > 0) {
        digits.push_back(num % 10);
        num /= 10;
    }

    reverse(digits.begin(), digits.end());
    return digits;
}

bool check(ll num) {
    vector<int> digits = get_digits(num);
    return is_sorted(digits.begin(), digits.end());
}



ll solve(ll num) {
    if (check(num)) {
        return num;
    }
    // check if the number is smaller than 11...1
    ll allOnes = 0;
    int numOfDigits = log10(num);
    for (int i = 0; i < numOfDigits; ++i) {allOnes *= 10; allOnes += 1;}

    if (num < allOnes) {
        num = 0;
        for (int i = 1; i < numOfDigits; ++i) {num *= 10; num += 9;}
        return num;
    }


    while (!check(num)) {
        bool reduced = false;
        // find first inversion
        // reduce the number on the left and set the next number to 9
        vector<int> digits = get_digits(num);

        for (int i = 1; i < (int) digits.size(); ++i) {
            if (digits[i] < digits[i-1]) {
                if (!reduced) {
                    digits[i - 1] -= 1;
                    digits[i] = 9;
                    reduced = true;
                } else {
                    digits[i] = digits[i-1];
                }
            }
        }

        num = 0;
        for (auto d: digits) {
            num *= 10;
            num += d;
        }
    }

    return num;
}

ll brute(ll num) {
    while (!check(num)) {
        num -= 1;
    }

    return num;
}

int main(int argc, char** argv) {
    int n;  scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        ll num; scanf("%lld", &num);

        ll sol = solve(num);
        // ll sol = brute(num);
        printf("Case #%d: %lld\n", i + 1, sol);
    }

    return 0;
}
