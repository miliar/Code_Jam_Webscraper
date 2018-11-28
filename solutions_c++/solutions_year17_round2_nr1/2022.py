#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

struct horse_t {
    int64_t K;
    int S;

    friend bool operator<(const horse_t& a, const horse_t& b) {
        return a.K < b.K;
    }
};

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int64_t D; std::cin >> D;
        int N; std::cin >> N;
        std::vector<horse_t> horses(N);
        for (auto& horse : horses) {
            std::cin >> horse.K;
            std::cin >> horse.S;
        }
        std::sort(horses.begin(), horses.end());
        double speed = -1;
        while (!horses.empty()) {
            double t = double(D - horses.back().K) / horses.back().S;
            double s = D / t;
            if (speed < 0 || speed > s) {
                speed = s;
            }
            horses.pop_back();
        }
        printf("Case #%d: %.6lf\n", caseNum, speed);
    }
    return 0;
}
