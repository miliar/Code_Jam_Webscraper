#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <fstream>

constexpr size_t max_size = 1000;

std::ostream& operator<<(std::ostream& out, const std::vector<bool>& vec) {
    std::for_each(vec.begin(), vec.end(), [&out](bool e){ out << (int) e; });
    return out;
}

void solve_once(std::vector<bool>& cookie_row, size_t flip_range_len, size_t case_idx, std::ofstream& out) {
//    std::cout << cookie_row << std::endl;

    auto next_zero_it = std::find(cookie_row.begin(), cookie_row.end(), 0);
    for (size_t steps = 0; true; ++steps) {
        if (next_zero_it == cookie_row.end()) {
            out << "Case #" << case_idx << ": " << steps << std::endl;
            return;
        }

        if (std::distance(next_zero_it, cookie_row.end()) < flip_range_len) {
            out << "Case #" << case_idx << ": " << "IMPOSSIBLE" << std::endl;
            return;
        }

        std::transform(next_zero_it, next_zero_it + flip_range_len, next_zero_it, [](bool e) {
            return !e;
        });

//        std::cout << "FLIP from " << next_zero_it - cookie_row.begin() << std::endl;
//        std::cout << cookie_row << std::endl;

        next_zero_it = std::find(next_zero_it, cookie_row.end(), 0);
    }

}

int main() {
    std::ifstream in("A-large.in");
    std::ofstream out("A-large.out");

    if (!in || !out) {
        std::cerr << "Can't open file!" << std::endl;
        return 1;
    }

    size_t test_num;
    std::string cookie_row_str;
    size_t range_len;

    in >> test_num;
    std::vector<bool> cookie_row;
    cookie_row.reserve(max_size);
    for (size_t i = 0; i < test_num; ++i) {
        in >> cookie_row_str >> range_len;

        cookie_row.clear();
        for (const auto& c : cookie_row_str) {
            if (c == '+') {
                cookie_row.push_back(true);
            } else {
                cookie_row.push_back(false);
            }
        }

        solve_once(cookie_row, range_len, i + 1, out);
    }
}
