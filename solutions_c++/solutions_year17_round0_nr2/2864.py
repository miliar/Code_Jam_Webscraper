#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <sstream>

using namespace std;


uint64_t max_tidy(uint64_t n) {
    string s = std::to_string(n);

    for (;;) {
        int first_wrong_digit = -1;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] > s[i + 1]) {
                first_wrong_digit = i;
                break;
            }
        }

        if (first_wrong_digit != -1) {
            s[first_wrong_digit] -= 1;
            for (int i = first_wrong_digit + 1; i < s.size(); i++) {
                s[i] = '9';
            }
        } else
            break;
    }

    return stoull(s);
}


int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        uint64_t n;
        cin >> n;
        cout << "Case #" << i + 1 << ": " << max_tidy(n) << endl;
    }

    return 0;
}
