#include <iostream>
#include <vector>
using namespace std;

typedef long long int64;

int64 ten_power[19];
int64 eleven_power[19];

int64 bt(int64 n, int last_digit, int digit_pos, int64 my_number) {
    if (digit_pos == -1) {
        return my_number;
    }

    for (int current_digit = last_digit; current_digit < 9; current_digit += 1) {
        if (eleven_power[digit_pos] * (current_digit + 1) + my_number > n) {
            return bt(n, current_digit, digit_pos - 1, my_number + ten_power[digit_pos] * current_digit);
        }
    }
    
    return bt(n, 9, digit_pos - 1, my_number + ten_power[digit_pos] * 9);
}

int main() {
    ten_power[0] = eleven_power[0] = 1;
    for (int i = 1; i < 19; i += 1) {
        ten_power[i] = ten_power[i - 1] * 10;
        eleven_power[i] = eleven_power[i - 1] + ten_power[i];
    }

    int T; cin >> T;
    for (int t = 1; t <= T; t += 1) {
        int64 n; cin >> n;
        cout << "Case #" << t << ": " << bt(n, 0, 18, 0) << '\n';
    }
}
