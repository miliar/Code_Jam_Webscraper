#include <bits/stdc++.h>
using namespace std;

long long solve(long long n) {
    assert(n > 0);
    vector<int> digits;
    for (long long tmp = n; tmp > 0; tmp /= 10) {
        digits.push_back(tmp % 10);
    }
    for (int i = digits.size() - 2; i >= 0; --i) {
        if (digits[i] < digits[i + 1]) {
            for (int j = i; j >= 0; --j) {
                digits[j] = 9;
            }
            ++i;
            while (true) {
                if (digits[i] == 0) {
                    digits[i] = 9;
                    ++i;
                } else {
                    --digits[i];
                    break;
                }
            }
            ++i;
        }
    }

    long long ans = 0;
    for (int i = digits.size() - 1; i >= 0; --i) {
        ans = digits[i] + ans * 10;
    }
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        long long n;
        scanf("%lld", &n);
        long long ans = solve(n);
        printf("Case #%d: %lld", (i + 1), ans);
        if (i + 1 < t) {
            printf("\n");
        }
    }
    return 0;
}