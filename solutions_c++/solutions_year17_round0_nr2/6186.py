#include <iostream>
#include <string>
#include <cmath>

using namespace std;
using UL = unsigned long long;

UL b10(int n) {
    if (n == 0) return 1;
    return b10(n - 1) * 10;
}

bool adjust(UL& n) {
    int digit = 9;
    int nd = 0;
    UL t = n;
    while (t > 0) {
        int current_digit = t % 10;
        if (current_digit > digit) {
            // untidy
            break;
        } else {
            digit = current_digit;
            nd++;
            t = t / 10;
        }
    }
    if (t == 0) {
        return false;
    }
    n = t * b10(nd) - 1;
    return true;
}

void run(int T) {
    UL num;
    cin >> num;
    while (adjust(num));
    cout << "Case #" << T << ": " << num << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        run(i + 1);
    }

}
