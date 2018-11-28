#include <iostream>
#include <string>

int solve(std::string pancakes, int flipSize) {
    int flips = 0;

    //std::cout << " " << pancakes;
    for (int i = 0; i + flipSize <= pancakes.size(); ++i) {
        if (pancakes.substr(i).at(0) == '-') {
            flips++;
            for (int j = 0; j < flipSize; ++j) {
                pancakes[i + j] = (pancakes[i + j] == '+' ? '-' : '+');
            }
            //std::cout << " " << pancakes;
        }
    }

    for (int i = 0; i < pancakes.length(); ++i) {
        if (pancakes.at(i) == '-') {
            return -1;
        }
    }

    return flips;
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        std::cout << "Case #" << i + 1 << ": ";

        std::string pancakes;
        int flipSize;

        std::cin >> pancakes >> flipSize;

        int ret = solve(pancakes, flipSize);

        if (ret == -1) {
            std::cout << "IMPOSSIBLE";
        } else {
            std::cout << ret;
        }

        std::cout << std::endl;
    }
    return 0;
}
