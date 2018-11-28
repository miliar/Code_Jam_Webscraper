#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        uint64_t N;
        uint64_t K;
        std::cin >> N >> K;
        int level = std::floor(std::log2(K));
        uint64_t occupied(1);
        occupied = (occupied << (level)) - 1;
        uint64_t free = N - occupied;
        //std::cerr << "free / occupied: " << free << " / " << occupied << std::endl;
        uint64_t lastLevelSize = 1;
        lastLevelSize = (lastLevelSize << level);
        //std::cerr << "lastLevelSize: " << lastLevelSize << std::endl;
        uint64_t nLargeSegments = free % lastLevelSize;
        //std::cerr << "nLargeSegments: " << nLargeSegments << std::endl;
        uint64_t firstPositionInLastLevel = lastLevelSize;
        uint64_t positionInLastLevel = K - firstPositionInLastLevel;
        //std::cerr << "positionInLastLevel: " << positionInLastLevel << std::endl;
        uint64_t segmentLength;
        if (positionInLastLevel < nLargeSegments)
            segmentLength = free / lastLevelSize + 1;
        else
            segmentLength = free / lastLevelSize;
        //std::cerr << "segmentLength: " << segmentLength << std::endl;

        std::cout << "Case #" << (i + 1) << ": ";
        if (segmentLength % 2)
            std::cout << (segmentLength - 1) / 2 << " " << (segmentLength - 1) / 2 << std::endl;
        else
            std::cout << segmentLength / 2 << " " << segmentLength / 2 - 1 << std::endl;
    }
}
