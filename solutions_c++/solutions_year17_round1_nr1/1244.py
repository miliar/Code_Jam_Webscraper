#include <iostream>
#include <vector>

typedef unsigned long long ull;
typedef long long ll;

void fill(std::string& row) {
    char first_name = '?';
    char name = '?';
    for (auto&& c : row) {
        if (c != '?') {
            name = c;
            if (first_name == '?') {
                first_name = name;
            }
        }
        c = name;
    }
    for (auto&& c : row) {
        if (c != '?') {
            break;
        }
        c = first_name;
    }
}

void fill(std::vector<std::string>& cake) {
    std::string first_row("?");
    std::string row("?");
    for (auto&& r : cake) {
        if (r[0] != '?') {
            row = r;
            if (first_row == "?") {
                first_row = row;
            }
        }
        r = row;
    }
    for (auto&& r : cake) {
        if (r[0] != '?') {
            break;
        }
        r = first_row;
    }
}

int main() {
    ull t;
    std::cin >> t;
    for (ull n = 1; n <= t; ++n) {
        ull r, c;
        std::cin >> r >> c;
        std::vector<std::string> cake(r);
        for (auto&& row : cake) {
            std::cin >> row;
            fill(row);
        }
        fill(cake);
        std::cout << "Case #" << n << ":" << std::endl;
        for (auto&& row : cake) {
            std::cout << row << std::endl;
        }
    }
    return 0;
}