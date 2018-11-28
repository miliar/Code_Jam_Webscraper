#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

uint64_t solve(std::vector<uint8_t>&& input)
{
    if (input.size() == 1) {
        return input[0];
    }

    auto it = input.begin();
    while (it != input.end() - 1) {
        if (*it > *(it + 1)) {
            while (it != input.begin() && *it == *(it - 1)) {
                --it;
            };

            (*it)--;
            std::transform(
                it + 1, input.end(), it + 1, [](uint8_t) { return 9; });
            break;
        }
        ++it;
    }

    uint64_t result = 0, exponent = input.size() - 1;
    for (auto&& x : input) {
        result += (x * static_cast<uint64_t>(std::pow(10, exponent--)));
        ;
    }

    return result;
}

int main(int argc, char** argv)
{
    if (argc < 2) {
        std::cout << "Not enough arguments: " << argv[0] << " <input file>"
                  << std::endl;
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    int numCases;

    inputFile >> numCases;

    int caseId = 0;
    while (++caseId <= numCases) {
        std::string S;
        inputFile >> S;

        std::vector<uint8_t> digits(S.size());
        std::transform(S.begin(), S.end(), digits.begin(),
            [](char s) { return uint64_t(s - '0'); });

        std::cout << "Case #" << caseId << ": " << solve(std::move(digits))
                  << std::endl;
    }

    return 0;
}
