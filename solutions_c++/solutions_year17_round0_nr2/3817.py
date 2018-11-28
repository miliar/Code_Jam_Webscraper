#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
        size_t testnum;
        cin >> testnum;
        for (size_t test {1}; test <= testnum; ++test) {
                string s;
                cin >> s;
                cout << "Case #" << test << ": ";
                size_t len {s.length()};
                vector<int> digits(len);
                for (size_t i {0}; i < len; ++i)
                        digits[i] = s[i] - '0';
                size_t k {0};
                while (k + 1 < len && digits[k] <= digits[k + 1])
                        ++k;
                if (k + 1 < len) {
                        for (size_t i {k + 1}; i < len; ++i)
                                digits[i] = 9;
                        digits[k] -= 1;
                        for (int i {k - 1}; i >= 0; --i) {
                                if (digits[i] > digits[i + 1]) {
                                        digits[i] -= 1;
                                        digits[i + 1] = 9;
                                }
                        }
                }
                size_t j {0};
                while (digits[j] == 0)
                        ++j;
                for (size_t i {j}; i < len; ++i)
                        cout << digits[i];
                cout << endl;
        }
        return 0;
}