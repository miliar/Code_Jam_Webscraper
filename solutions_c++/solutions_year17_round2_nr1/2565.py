#include <iostream>
#include <fstream>
#include <algorithm>
#include <cinttypes>
#include <iomanip>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::ifstream input("A-large.in");
    std::ofstream output("output.txt");

    size_t T;
    input >> T;
    for (size_t t = 1; t <= T; ++t) {
        int D, N;
        input >> D >> N;
        double time = 0.0;
        for (size_t i = 0; i < N; ++i) {
            int K, S;
            input >> K >> S;
            time = std::max(time, (D - K + 0.0) / S);
        }
        output << "Case #" << t << ": ";
        output << std::fixed << std::setprecision(8) << D / time << std::endl;
    }

    return 0;
}
