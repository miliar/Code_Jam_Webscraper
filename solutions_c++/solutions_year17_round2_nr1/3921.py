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
        ull D, N;
        std::cin >> D >> N;
        std::vector<std::pair<ull, ull>> KS(N);
        for (auto&& KSi : KS) {
            std::cin >> KSi.first >> KSi.second;
        }
        std::sort(KS.begin(), KS.end());
        int i;
        for (i = 0; i + 1 < N; ++i) {
            if (KS[i].second <= KS[i + 1].second) {
                break;
            }
            ld distance = KS[i + 1].first - KS[i].first;
            ld time = distance / (KS[i].second - KS[i + 1].second);
            ld point = KS[i].first + time * KS[i].second;
            if (point >= D) {
                break;
            }
        }
        ld distance = D - KS[i].first;
        ld time = distance / KS[i].second;
        std::cout << "Case #" << t << ": " << std::fixed << D / time << std::endl;
    }
    return 0;
}