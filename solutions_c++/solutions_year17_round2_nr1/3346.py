#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>

double solve(uint64_t dest, std::vector<std::pair<int64_t, int64_t> > others)
{
    std::vector<double> times;
    times.resize(others.size());

    std::transform(others.begin(), others.end(), times.begin(),
        [dest](std::pair<int64_t, int64_t> o) {
            auto distLeft = dest - o.first;
            return distLeft / static_cast<double>(o.second);
        });


    double slowest = *(std::max_element(times.begin(), times.end()));
    return dest / slowest;
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
        int64_t D, N;
        inputFile >> D >> N;
        std::vector<std::pair<int64_t, int64_t> > horses;
        horses.reserve(N);
        while (N--) {
            int64_t K, S;
            inputFile >> K >> S;
            horses.push_back(std::make_pair(K, S));
        }

        std::cout << "Case #" << caseId << ": " << std::fixed << std::setprecision(6) << solve(D, horses)
                  << std::endl;
    }

    return 0;
}
