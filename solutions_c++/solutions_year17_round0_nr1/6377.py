#include <algorithm>
#include <cassert>
#include <cstring>
#include <deque>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        std::string s;
        std::cin >> s;

        int k;
        std::cin >> k;

        int times = 0;
        for (int i = 0; i + k - 1 < s.size(); ++i) {
            if (s[i] == '-') {
                for (int j = 0; j < k; ++j) {
                    auto& w = s[i + j];
                    w = (w == '+' ? '-' : '+');
                }
                ++times;
            }
        }

        if (std::all_of(s.cbegin(), s.cend(),
            [](auto&& w) { return w == '+'; })) {
            std::cout << "Case #" << ti << ": " << times << std::endl;
        } else {
            std::cout << "Case #" << ti << ": IMPOSSIBLE" << std::endl;
        }
    }
}