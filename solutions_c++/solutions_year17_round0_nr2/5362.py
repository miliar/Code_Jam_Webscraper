#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

vector<int> get_digits(uint64_t N)
{
    vector<int> digits;
    uint64_t n = N;
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    reverse(digits.begin(), digits.end());
    return digits;
}

bool is_tidy(vector<int>& number) {
    int last_digit = 0;
    for (int d : number) {
        if (d < last_digit) {
            return false;
        }
        last_digit = d;
    }
    return true;
}

string solve(uint64_t N)
{
    auto number = get_digits(N);
    if (is_tidy(number)) {
        return to_string(N);
    }
    uint64_t res = 0;
    bool carried = false;
    for (int i = 0; i < number.size(); ++i) {
        res *= 10;
        if (carried) {
            res += 9;
            continue;
        }
        int d = number[i];
        int lower_index = 0;
        int bigger_index = 0;
        for (int j = i; j < number.size(); ++j) {
            if (lower_index == 0 && number[j] < d) {
                lower_index = j;
            }
            if (bigger_index == 0 && number[j] > d) {
                bigger_index = j;
            }
        }
        if (lower_index > 0 && (bigger_index == 0 || bigger_index > lower_index)) {
            d--;
            carried = true;
        }
        res += d;
    }
    return to_string(res);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        uint64_t N;
        cin >> N;
        cout << "Case #" << t << ": ";
        //cout << N << "->";
        cout << solve(N);
        cout << endl;
    }
}