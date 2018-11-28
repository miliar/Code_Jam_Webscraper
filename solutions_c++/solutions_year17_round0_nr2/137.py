#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        long long n;
        cin >> n;

        vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }

        int len = digits.size();
        for (int i = 0; i < len; ++ i) {
            if (i < len - 1 && digits[i] < digits[i + 1]) {
                -- digits[i + 1];
                for (int j = 0; j <= i; ++ j) digits[j] = 9;
            }
        }
        if (digits.back() <= 0) digits.pop_back();

        cout << "Case #" << t << ": ";
        for (int i = digits.size() - 1; i >= 0; -- i) cout << digits[i];
        cout << endl;
    }

    return 0;
}
