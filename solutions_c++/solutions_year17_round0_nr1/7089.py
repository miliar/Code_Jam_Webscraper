#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <queue>

void pancake (std::string s, int k);


int main() {
    int t;
    std::string s;
    int k;
    std::cin >> t;

    for (int i = 1; i <= t; ++i) {
        std::cin >> s >> k;
        std::cout << "Case #" << i << ": ";
        pancake(s, k);
        std::cout << std::endl;
    }

    return 0;
}

void pancake (std::string s, int k) {
    int counter = 0;
    for (int i = 0; i <= s.length() - k; ++i) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; ++j) {
                s[j] = s[j] == '-' ? '+' : '-';
            }
            counter++;
        }
    }
    for (int i = s.length() - k; i < s.length(); ++i) {
        if (s[i] == '-') {
            std::cout << "IMPOSSIBLE";
            return;
        }
    }
    std::cout << counter;


}

