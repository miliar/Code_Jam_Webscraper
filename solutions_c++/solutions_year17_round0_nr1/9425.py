#include <iostream>
#include <iomanip>
#include <vector>

int main()
{
    size_t test_cases, k;

    std::cin >> test_cases;
    std::cin >> std::noskipws;

    for (size_t t = 0; t < test_cases; ++t) {
        std::vector<bool> pan;
        char c;

        std::cin >> c;
        std::cin >> c;

        while (c != ' ') {
            //std::cout << c << std::endl;

            if (c == '-') {
                pan.push_back(false);
            } else {
                pan.push_back(true);
            }
            std::cin >> c;
        }
        std::cin >> k;

        size_t flips = 0;

        for (size_t i = 0; i < pan.size() - k + 1; ++i) {
            if (! pan[i]) {
                ++flips;
                //std::cout << "Flip: " << i << std::endl;
                for (size_t j = 0; j < k; ++j) {
                    pan[i + j] = ! pan[i + j];
                }
            }
        }

        bool can_do = true;

        for (size_t i = 0; i < pan.size(); ++i) {
            if (! pan[i]) {
                can_do = false;
                break;
            }
        }

        std::cout << "Case #" << t + 1 << ": ";

        if (can_do) {
            std::cout << flips;
        } else {
            std::cout << "IMPOSSIBLE";
        }
        std::cout << std::endl;

        //std::cout << k << std::endl;
    }

    return 0;
}
