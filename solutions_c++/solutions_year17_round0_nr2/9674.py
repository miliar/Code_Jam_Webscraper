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
                unsigned long long tidyNumber = 0;
                input >> tidyNumber;
                std::string tidyNumberStr = std::to_string(tidyNumber);
                int tidyNumberSize = tidyNumberStr.size() - 1;
                for (int j = 0; j < tidyNumberSize; ++j) {
                    if (tidyNumberStr.at(j) > tidyNumberStr.at(j + 1)) {
                        int index = j;
                        for (int k = j; k > 0; --k) {
                            if (tidyNumberStr.at(k) == tidyNumberStr.at(k - 1)) {
                                index = k - 1;
                            }
                        }
                        tidyNumberStr[index] = tidyNumberStr[index] - 1;
                        for (int k = index + 1; k < tidyNumberSize + 1; ++k) {
                            tidyNumberStr[k] = '9';
                        }
                        for (int k = 0; k < tidyNumberStr.size(); ++k) {
                            if (tidyNumberStr.at(k) == '0') {
                                tidyNumberStr.erase(k, 1);
                            } else {
                                break;
                            }
                        }
                        break;
                    }
                }
                output << "Case #" << i + 1 << ": " << tidyNumberStr << std::endl;
            }
            output.flush();
            output.close();
        }
        input.close();
    }
}
