#include <iostream>
#include <vector>
#include <cmath>

typedef long double ld;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    ull T;
    std::cin >> T;
    std::cout.precision(6);

    for (ull t = 1; t <= T; ++t) {
        ull N, R, O, Y, G, B, V;
        std::cin >> N >> R >> O >> Y >> G >> B >> V;
        std::cout << "Case #" << t << ": ";
        if (2 * O > B || 2 * G > R || 2 * V > Y) {
            std::cout << "IMPOSSIBLE" << std::endl;
            continue;
        }
        B -= 2 * O;
        R -= 2 * G;
        Y -= 2 * V;
        std::vector<std::string> max_group, mid_group, min_group;
        for (ull i = 0; i < B; ++i) {
            max_group.push_back("B");
        }
        for (ull i = 0; i < R; ++i) {
            mid_group.push_back("R");
        }
        for (ull i = 0; i < Y; ++i) {
            min_group.push_back("Y");
        }
        for (ull i = 0; i < O; ++i) {
            max_group.push_back("BOB");
        }
        for (ull i = 0; i < G; ++i) {
            mid_group.push_back("RGR");
        }
        for (ull i = 0; i < V; ++i) {
            min_group.push_back("YVY");
        }
        if (max_group.size() < mid_group.size()) {
            max_group.swap(mid_group);
        }
        if (mid_group.size() < min_group.size()) {
            mid_group.swap(min_group);
        }
        if (max_group.size() < mid_group.size()) {
            max_group.swap(mid_group);
        }
        if (max_group.size() > mid_group.size() + min_group.size()) {
            std::cout << "IMPOSSIBLE" << std::endl;
            continue;
        }
        while (!max_group.empty()) {
            std::cout << max_group.back();
            if (mid_group.size() + min_group.size() > max_group.size()) {
                std::cout << mid_group.back();
                mid_group.pop_back();
                std::cout << min_group.back();
                min_group.pop_back();
            } else {
                if (mid_group.size() > min_group.size()) {
                    std::cout << mid_group.back();
                    mid_group.pop_back();
                } else {
                    std::cout << min_group.back();
                    min_group.pop_back();
                }
            }
            max_group.pop_back();
        }
        std::cout << std::endl;
    }
    return 0;
}