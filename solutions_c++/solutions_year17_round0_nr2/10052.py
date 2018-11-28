#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <typename T>
T read(istream& is);

vector<int> to_digits(string const& str);
vector<int> find_tidy_number(vector<int> digits);

int main() {
    auto cases = read<size_t>(cin);

    for (auto i = 0u; i < cases; ++i) {
        auto const digits = to_digits(read<string>(cin));

        auto const tidy_number = find_tidy_number(digits);

        cout << "Case #" << i + 1 << ": ";
        for (auto const i : tidy_number) cout << i;
        cout << '\n';
    }
}

template <typename T>
T read(istream& is) {
    T t; is >> t;
    return t;
}

vector<int> to_digits(string const& str) {
    auto result = vector<int>{};

    result.reserve(str.size());

    for (auto const c : str) result.push_back(c - '0');

    return result;
}

size_t to_number(vector<int> const& digits) {
    auto result = size_t{0};

    for (auto digit : digits) {
        result *= 10;
        result += digit;
    }

    return result;
}

vector<int> find_tidy_number(vector<int> digits) {
    reverse(begin(digits), end(digits));

    for (auto i = 0u; i < digits.size() - 1; ++i) {
        auto& current = digits[i];
        auto& next    = digits[i + 1];

        if (next > current) {
            current = 9;
            next -= 1;

            // All digits prior are now 9.
            for (auto j = 0u; j < i; ++j) digits[j] = 9;
        }
    }

    // Remove leading zeroes.
    while (digits.back() == 0) digits.pop_back();

    reverse(begin(digits), end(digits));

    return digits;
}
