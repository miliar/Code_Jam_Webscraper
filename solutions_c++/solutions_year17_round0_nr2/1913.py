#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        long long n;

        cin >> n;

        vector<uint8_t> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }

        reverse(digits.begin(), digits.end());

        int i = 0;
        for (i = 0; i + 1 < digits.size(); ++i) {
            if (digits[i] > digits[i + 1])
                break;
        }

        if (i + 1 < digits.size()) {
            int j = i;
            while (j >= 0 && digits[j] == digits[i])
                --j;
            if (j == -1) {
                n = digits[0] - 1;
                for (int k = 0; k < digits.size() - 1; ++k)
                    n = n * 10 + 9;
            }
            else {
                n = 0;
                for (int k = 0; k <= j; ++k)
                    n = n * 10 + digits[k];
                n = n * 10 + digits[i] - 1;
                for (int k = j + 2; k < digits.size(); ++k)
                    n = n * 10 + 9;
            }
        }
        else {
            n = 0;
            for (auto digit: digits)
                n = n * 10 + digit;
        }

        cout << "Case #" << t << ": ";

        cout << n;

        cout << '\n';
    }

    return 0;
}
