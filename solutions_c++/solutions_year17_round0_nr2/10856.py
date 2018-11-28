#include <iostream>
#include <stdint.h>
#include <string>

int main() {
        int testCases = 0;
        uint64_t input1;
        std::cin >> testCases;
        for ( int i = 1; i <= testCases; ++i ) {
                std::cin >> input1;

                std::string output1 = std::to_string(input1);
                while (input1 > 0) {
                        bool found = true;
                        for (size_t i = 0; i < output1.length() - 1; ++i) {
                                if (output1[i] > output1[i+1]) {
                                        found = false;
                                        break;
                                }
                        }

                        if (found) {
                                break;
                        }

                        --input1;
                        output1 = std::to_string(input1);
                }
                std::cout << "Case #" << i << ": " << output1 << std::endl;
        }

        return 0;
}
