#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

void solve(std::vector<char>&& input, uint32_t N)
{
    int flips = 0;

    auto firstBlank = std::find(input.begin(), input.end(), '-');

    while (firstBlank != input.end()
        && std::distance(firstBlank, input.end()) >= N) {

        std::transform(firstBlank, firstBlank + N, firstBlank,
            [](char c) { return c == '-' ? '+' : '-'; });

        firstBlank = std::find(firstBlank + 1, input.end(), '-');
        ++flips;
    }

    if (firstBlank == input.end()) {
        std::cout << flips << std::endl;
    } else {
        std::cout << "IMPOSSIBLE" << std::endl;
    }
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
    // Skip the newline.
    inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    int caseId = 0;
    while (++caseId <= numCases) {
        std::string S;
        int N;
        inputFile >> S >> N;
        std::cout << "Case #" << caseId << ": ";
        solve(std::vector<char>(S.begin(), S.end()), N);
    }

    return 0;
}
