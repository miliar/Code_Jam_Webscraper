#include <iostream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <limits>
#include <cassert>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>


long solve()
{
    return 0;
}


void run_test_case()
{

    size_t N, P;
    std::cin >> N >> P;
    std::vector<size_t> G;
    for (size_t i = 0; i < N; ++i) {
        size_t g;
        std::cin >> g;
        G.push_back(g);
    }

    assert(P <= 4);

    std::vector<int> num(4, 0);

    for (size_t g : G) {
        num[g % P] += 1;
    }

    switch (P) {
        case 2:
            // 1+1, first always gets new pack
            num[0] += (num[1]+1) / 2;
            break;
        case 3:
            // 2+1, 1+2
            while (num[1] > 0 && num[2] > 0) {
                num[0] += 1;
                num[1] -= 1;
                num[2] -= 1;
            }
            // 1+1+1, 2+2+2
            while (num[1] > 0) {
                num[0] += 1;
                num[1] -= 3;
            }
            while (num[2] > 0) {
                num[0] += 1;
                num[2] -= 3;
            }
            break;
        case 4: // 1, 2, 3
            // 1+3, 2+2
            while (num[1] > 0 && num[3] > 0) {
                num[0] += 1;
                num[1] -= 1;
                num[3] -= 1;
            }
            while (num[2] >= 2) {
                num[0] += 1;
                num[2] -= 2;
            }
            // 1+1+2, 2+3+3
            if (num[2] > 0) {
                assert(num[2] == 1);
                assert(num[1] == 0 || num[3] == 0);
                if (num[1] >= 2) {
                    num[0] += 1;
                    num[1] -= 2;
                    num[2] -= 1;
                }
                if (num[3] >= 2) {
                    num[0] += 1;
                    num[3] -= 2;
                    num[2] -= 1;
                }
            }
            // 1+1+1+1, 3+3+3+3
            while (num[1] >= 4) {
                num[0] += 1;
                num[1] -= 4;
            }
            while (num[3] >= 4) {
                num[0] += 1;
                num[3] -= 4;
            }
            if (num[1]+num[2]+num[3] > 0) {
                num[0] += 1;
            }
            break;
    }

    std::cout << num[0];
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
