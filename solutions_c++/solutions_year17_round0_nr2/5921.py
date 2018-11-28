#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        long long n;
        cin >> n;
        int i = 18;
        int digits[18] = { 0 };
        while(n) {
            digits[--i] = n % 10;
            n /= 10;
        }
        i = 17;
        while(!is_sorted(digits, digits + 18, [] (int a, int b) { return a < b; })) {
            do {
                digits[i--] = 9;
                --digits[i];
            } while(digits[i] == -1);
        }
        n = digits[0];
        for(i = 0; i < 18; ++i) {
            n = 10 * n;
            n += digits[i];
        }
        cout << n << endl;
    }
    return 0;
}
