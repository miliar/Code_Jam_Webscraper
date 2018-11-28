#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iomanip>

using speed_t = double;
using distance_t = double;

struct horse {
    distance_t start_point;
    speed_t speed;

    horse(distance_t start_point, speed_t speed): start_point(start_point), speed(speed) {}
};

speed_t solve_once(const std::vector<horse>& horses, distance_t destination) {
    speed_t result_speed = std::numeric_limits<speed_t>::max();

    for (auto& h : horses) {
        speed_t s = destination * h.speed / (destination - h.start_point);
        if (s < result_speed) {
            result_speed = s;
        }
    }

    return result_speed;
}


int main() {
    std::ifstream in("A-large.in");
    std::ofstream out("A-large.out");

    if (!in || !out) {
        std::cerr << "Can't open files!" << std::endl;
        return 1;
    }

    size_t test_num;
    in >> test_num;
    for (size_t i = 0; i < test_num; ++i) {
        distance_t destination;
        size_t horses_num;
        in >> destination >> horses_num;

        std::vector<horse> horses;
        for (size_t j = 0; j < horses_num; ++j) {
            distance_t start_point;
            speed_t speed;
            in >> start_point >> speed;
            horses.emplace_back(start_point, speed);
        }

        auto answer = solve_once(horses, destination);

        out << "Case #" << i + 1 << ": " << std::setprecision(10) << answer << std::endl;
    }

    return 0;
}
