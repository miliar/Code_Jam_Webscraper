#include <iostream>
#include <set>


std::string solve(int n, int k) {
    std::set<int> used;
    used.insert(0);
    used.insert(n + 1);

    int mins, maxs;
    for (int i = 0; i < k; i++) {
        mins = -123123123;
        maxs = -123123123;
        int ind = 1;

        for (int j = 1; j <= n; j++) {
            if (used.find(j) != used.end()) {
                continue;
            }

            auto lit = --used.upper_bound(j);
            auto rit = used.upper_bound(j);
            int ls = j - *lit;
            int rs = *rit - j;
            int temp_min = std::min(ls, rs);
            int temp_max = std::max(ls, rs);

            if (mins < temp_min) {
                mins = temp_min;
                maxs = temp_max;
                ind = j;
            } else if (mins == temp_min && temp_max > maxs) {
                mins = temp_min;
                maxs = temp_max;
                ind = j;
            }
        }

        used.insert(ind);
    }

    return std::to_string(maxs - 1) + " " + std::to_string(mins - 1);
}


int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        int n, k;
        std::cin >> n >> k;
        std::cout << "Case #" << i + 1 << ": " << solve(n, k) << std::endl;
    }
    return 0;
}
