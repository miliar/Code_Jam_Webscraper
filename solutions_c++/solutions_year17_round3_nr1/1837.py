#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <iterator>
#include <limits>
#include <cmath>
#include <iomanip>
#include <list>
#include <set>
#include <fstream>

constexpr double math_pi = 3.1415926535897932384626433;

struct pancake {
    pancake(double rad, double h): radius(rad), height(h),
                                   m_top_area(rad * rad * math_pi),
                                   m_side_area(2 * math_pi * rad * h)
    {}

    double radius;
    double height;

    double top_area() {
        return m_top_area;
    }

    double side_area() {
        return m_side_area;
    }

private:
    double m_top_area;
    double m_side_area;
};

struct radius_comparator {
    bool operator() (const pancake& a, const pancake& b) {
        return a.radius > b.radius;
    }
};

double calc_area(std::vector<pancake>& cakes, std::set<size_t>& indices) {
    double answer = 0;

    for (auto it = indices.begin(); it != indices.end();) {
        auto current = it;
        auto next = ++it;
//        std::cout << *current << " " << *next << std::endl;
        answer += cakes[*current].side_area();
        if (next != indices.end()) {
            answer += cakes[*current].top_area() - cakes[*next].top_area();
        } else {
            answer += cakes[*current].top_area();
        }
    }

    return answer;
}

double solve(std::vector<pancake>& pancakes, size_t k) {
    // sorting by radius
    std::sort(pancakes.begin(), pancakes.end(), radius_comparator());

    // now need to choose k pancakes
    // choose first k at first
    std::set<size_t> indices;
    for (size_t i = 0; i < k; ++i) {
        indices.insert(i);
    }

    double current_answer = calc_area(pancakes, indices);
    for (size_t i = k; i < pancakes.size(); ++i) {
        indices.insert(i);
        double max = current_answer;
        size_t del_idx_max = std::numeric_limits<size_t>::max();
        for (auto it = indices.begin(); it != indices.end();) {
            size_t val = *it;
            if (val == i) {
                it++;
                continue;
            }
            it = indices.erase(it);
            double new_val = calc_area(pancakes, indices);
            if (new_val > max) {
                max = new_val;
                del_idx_max = val;
            }
            indices.insert(val);
        }

        if (max != current_answer) {
            indices.erase(del_idx_max);
            current_answer = max;
        } else {
            indices.erase(i);
        }
    }
    return current_answer;
}


int main() {
    size_t test_num;

    std::ofstream out("A-large.out");
    std::ifstream in("A-large.in");

    if (!in || !out) {
        std::cerr << "Can't open files!" << std::endl;
    }

    in >> test_num;
    for (size_t i = 0; i < test_num; ++i) {
        size_t n, k;
        in >> n >> k;
        std::vector<pancake> pancakes;
        pancakes.reserve(n);
        for (size_t j = 0; j < n; ++j) {
            double r, h;
            in >> r >> h;
            pancakes.emplace_back(r, h);
        }

        auto result = solve(pancakes, k);
        out << "Case #" << i + 1 << ": "
            << std::setprecision(10)
            << std::fixed
            << result << std::endl;
    }

    return 0;
}