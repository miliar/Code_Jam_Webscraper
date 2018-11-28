#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

static bool isTidy(int64_t n) {
    std::vector<int64_t> digits;
    int64_t tmp = n;
    while (tmp > 0) {
        digits.push_back(tmp % 10);
        tmp /= 10;
    }
    std::reverse(digits.begin(), digits.end());
    int nDigits = static_cast<int>(digits.size());
    bool tidy = true;
    for (int i = 1; i < nDigits; ++i) {
        if (!(digits.at(i - 1) <= digits.at(i))) {
            tidy = false;
            break;
        }
    }
    return tidy;
}

int main() {
    int nTests = 0;
    cin >> nTests;
    for (int t = 1; t <= nTests; ++t) {
        int64_t n = 0;
        cin >> n;
        std::vector<int64_t> digits;
        int64_t tmp = n;
        while (tmp > 0) {
            digits.push_back(tmp % 10);
            tmp /= 10;
        }
        std::reverse(digits.begin(), digits.end());
        int nDigits = static_cast<int>(digits.size());
        int64_t ans = 0;
        if (isTidy(n)) {
            ans = n;
        } else {
            int i = nDigits - 2;
            while (i >= 0) {
                if (digits.at(i) > digits.at(i + 1)) {
                    while (i >= 0 && digits.at(i) > digits.at(i + 1)) {
                        i -= 1;
                    }
                    digits.at(i + 1) -= 1;
                    for (int j = i + 2; j < nDigits; ++j) {
                        digits.at(j) = 9;
                    }
                } else {
                    --i;
                }
            }
            for (int j = 0; j < nDigits; ++j) {
                ans *= 10;
                ans += digits.at(j);
            }
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }

    return 0;
}
