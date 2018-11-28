#include <iostream>

using namespace std;

bool is_tidy(int num) {
    int prev = 10;
    while (num > 0) {
        int cur = num % 10;
        if (cur > prev) {
            return false;
        }
        prev = cur;
        num /= 10;
    }
    return true;
}

int solve(int num) {
    while (!is_tidy(num)) {
        num--;
    }
    return num;
}

int main() {
    int t, num;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> num;
        int ans = solve(num);
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}