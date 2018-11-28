#include <iostream>
#include <string>
#include <vector>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::string S;
        int K;

        std::cin >> S >> K;
        int S_len = S.size();

        int F = 0;

        std::vector<bool> previos_flips(K, false); // remember edge of previous flips
        bool cur_swap = false;

        for (int i = 0; i < S_len; ++i) {
            bool sad = S[i] == '-';
            if (previos_flips[i % K]) {
                cur_swap = !cur_swap;
            }
            if (sad == cur_swap) {
                // fine
                previos_flips[i % K] = false;
            } else {
                // flip
                if (i > S_len - K) {
                    // out of range
                    F = -1;
                    break;
                }
                ++F;
                previos_flips[i % K] = true;
                cur_swap = !cur_swap;
            }
        }

        if (F < 0) {
            std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
        } else {
            std::cout << "Case #" << t << ": " << F << std::endl;
        }
    }
}
