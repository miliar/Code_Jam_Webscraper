#include <cmath>
#include <iostream>
#include <vector>

typedef long double ld;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    ull T;
    std::cin >> T;
    std::cout.precision(9);

    for (ull t = 1; t <= T; ++t) {
        ull N, P;
        std::cin >> N >> P;
        std::vector<ull> G(N);
        for (auto&& Gi : G) {
            std::cin >> Gi;
        }
        if (P == 2) {
            long odds = std::count_if(G.begin(), G.end(), [] (ull Gi) {
                return Gi % 2 != 0;
            });
            std::cout << "Case #" << t << ": " << N - (odds / 2) << std::endl;
        } else if (P == 3) {
            long pluses = std::count_if(G.begin(), G.end(), [] (ull Gi) {
                return Gi % 3 == 1;
            });
            long minuses = std::count_if(G.begin(), G.end(), [] (ull Gi) {
                return Gi % 3 == 2;
            });
            long diff = std::abs(pluses - minuses);
            std::cout << "Case #" << t << ": " << N - (std::min(pluses, minuses) + diff / 3 * 2 + std::max(diff % 3 - 1, 0L)) << std::endl;
        }
//        std::cout << "Case #" << t << ": " << 0 << std::endl;
    }
    return 0;
}