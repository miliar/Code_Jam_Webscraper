#include <iostream>
#include <cmath>
#include <string>

using namespace std;
using ll = long long;

bool is_tidy(ll n) {
        if (n < 10) return true;
        if (n % 10 < (n / 10) % 10) return false;
        return is_tidy(n / 10);
}


int main() {
        int T; cin >> T;
        for (int i = 1; i <= T; i++) {
                cout << "Case #" << i << ": ";
                string digits; cin >> digits;
                ll original = stoll(string(digits));

                while (!is_tidy(stoll(digits))) {
                        for (auto i = digits.length() - 1; i > 0; i--) {
                                digits[i] = '9';
                                if (digits[i - 1] == '0' && i > 0) {
                                        digits[i - 1] = '9';
                                } else if (digits[0] >= '1') {
                                        digits[i - 1] -= 1;
                                } else {
                                        digits[i - 1] = '1';
                                }

                                if (is_tidy(stoll(digits)) && stoll(digits) < original) break;
                        }
                }

                int j = 0;
                while (digits[j] == '0') j++;
                for (int k = j; k < digits.length(); k++) {
                        cout << digits[k];
                }
                cout << endl;
        }
}
