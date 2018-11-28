#include <iostream>

std::string solve(std::string& n) {
    bool carry = false;

    for (int i = n.size() - 2; i >= 0; --i) {
        // std::cout << n << " " << carry << "\n";

        if (carry) {
            if (n[i] == '0') {
                n[i] = '9';
                continue;
            } else {
                carry = false;
                n[i] = n[i] - 1;
            }
        }

        if (n[i] <= n[i + 1]) {
            carry = false;
            continue;
        }

        if (n[i] == '0') {
            carry = true;
            n[i] = '9';
        } else {
            carry = false;
            n[i] = n[i] - 1;
        }

        for (int j = i + 1; j < n.size(); ++j)
            n[j] = '9';
    }

    // std::cout << n << "\n";

    if (n[0] == '0')
        return n.substr(1, n.size());
    return n;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    int tests_count;
    std::cin >> tests_count;

    for (int i = 1; i <= tests_count; ++i) {
        std::string n;

        std::cin >> n;
        std::cout << "Case #" << i << ": " << solve(n) << "\n";
    }
}
