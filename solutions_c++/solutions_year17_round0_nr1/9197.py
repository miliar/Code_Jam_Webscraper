#include <iostream>
#include <fstream>
#include <string>

void main() {
    std::ifstream input("input.txt");
    if (input.is_open()) {
        std::ofstream output("output.txt");
        if (output.is_open()) {
            int tCount = 0;
            input >> tCount;
            for (int i = 0; i < tCount; ++i) {
                std::string str = "";
                int flapSize = 0, flapCount = 0;
                input >> str;
                input >> flapSize;
                int iterCount = str.size() - flapSize + 1;
                for (int j = 0; j < iterCount; ++j) {
                    if (str.at(j) != '+') {
                        for (int k = 0; k < flapSize; ++k) {
                            if (str.at(k + j) == '-') str[k + j] = '+';
                            else str[k + j] = '-';
                        }
                        ++flapCount;
                    }
                }
                bool possible = true;
                for (int j = iterCount; j < str.size(); ++j) {
                    if (str.at(j) == '-') {
                        possible = false;
                        break;
                    }
                }
                if (possible) {
                    output << "Case #" << i + 1 << ": " << flapCount << std::endl;
                } else {
                    output << "Case #" << i + 1 << ": IMPOSSIBLE" << std::endl;
                }
            }
            output.flush();
            output.close();
        }
        input.close();
    }
}
