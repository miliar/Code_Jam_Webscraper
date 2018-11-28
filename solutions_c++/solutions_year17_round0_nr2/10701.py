#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>

#include <stdint.h>
#include <string.h>

int64_t solve(int64_t num) {
    int64_t result = 0;

    int d1 = 0, d2 = 0, count = 0;
    while (num >= 10) {
        d1 = num % 10;
        num /= 10;
        d2 = num % 10;

        if (d2 > d1) {
            result = std::pow(10, count+1)-1;
            num -= 1;
        }
        else {
            result += d1*std::pow(10, count);
        }
        count++;
    }

    if (num>0) {
        result += num*std::pow(10, count);
    }

    return result;
}

int main(int argc, char* argv[]) {
    std::ifstream inputFile;
    std::ofstream outputFile;

    if (argc > 1) {
        inputFile.open(argv[1]);
        outputFile.open(argv[1] + std::string(".out"));
    }
    else {
        std::string filename("test");
        inputFile.open(filename);
        outputFile.open(filename+".out");
    }

    unsigned int T = 0;

    inputFile >> T;

    if (inputFile.good()) {
        int64_t num;
        for (unsigned int i=0; i<T && !inputFile.eof(); ++i) {
            inputFile >> num;
            outputFile << "Case #" << i+1 << ": " << solve(num) << std::endl;
        }
    }

    inputFile.close();
    outputFile.close();
    return 0;
}
