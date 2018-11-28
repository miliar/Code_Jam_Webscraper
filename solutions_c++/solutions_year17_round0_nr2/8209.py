#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    unsigned long long n;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n;
        string s = to_string(n);
        int inter_value, inter_i;
        for (size_t k = 1, n = s.length(); k < n; k++) {
            if (s[k] < s[k-1]) {
                inter_value = s[k-1];
                inter_i = k-1;
                while (inter_i - 1 >= 0 && s[inter_i - 1] == inter_value) {
                    inter_i--;
                }
                s[inter_i]--;
                for (size_t j = inter_i + 1; j < n; j++) {
                    s[j] = '9';
                }
            }
        }
        cout << "Case #" << i << ": " << stoll(s, nullptr) << "\n";
    }
    return 0;
}
