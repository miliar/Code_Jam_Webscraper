#include <iostream>
#include <vector>
#include <limits>
#include <iomanip>

int main() {
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {

        double D, N;

        std::cin >> D >> N;

        std::vector<double> horse_pos(N);
        std::vector<double> horse_speed(N);
        for (int j = 0; j < N; ++j) {
            std::cin >> horse_pos[j];
            std::cin >> horse_speed[j];
        }

        double max_time = 0;
        for (int k = 0; k < N; ++k) {
            max_time = std::max(max_time, (D-horse_pos[k])/horse_speed[k]);
        }

        std::cout.precision(std::numeric_limits< double >::max_digits10);
        std::cout << "Case #" << i + 1 << ": " << std::fixed << D/max_time << "\n";
    }
    return 0;
}