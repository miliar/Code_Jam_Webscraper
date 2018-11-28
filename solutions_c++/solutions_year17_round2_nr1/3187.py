#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

struct Horse {
    int64_t K;
    int64_t S;
};

struct {
    bool operator()(Horse a, Horse b)
    {
        return a.K < b.K;
    }
} horseLess;

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        int64_t D;
        int64_t N;
        std::cin >> D >> N;
        std::vector<Horse> h(N);
        for (int j = 0; j < N; ++j) {
            std::cin >> h[j].K >> h[j].S;
        }
        std::sort(h.begin(), h.end(), horseLess);
        double lastArrival = double(D - h.back().K) / h.back().S;
        for (auto it = h.rbegin(); it != h.rend(); ++it) {
            lastArrival = std::max(lastArrival, double(D - it->K) / it->S);
        }
        std::cout << "Case #" << (i + 1) << ": " << std::setprecision(15) << double(D) / lastArrival << std::endl;
    }
}
