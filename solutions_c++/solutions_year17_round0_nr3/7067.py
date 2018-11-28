#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

int main() {
    std::ifstream file("input.txt");
    std::string str;
    std::getline(file, str);
    int testCase {0};
    while (std::getline(file, str))
    {
        if (str == "") {
            break;
        }
        ++testCase;
        std::stringstream iss(str);
        int N;
        iss >> N;
        int K;
        iss >> K;

        // std::cout << N << "  ";
        // std::cout << K << "\n";

        std::vector<bool> bathroomStalls(N+2, true);
        bathroomStalls.at(0) = false;
        bathroomStalls.at(N+1) = false;

        int minDist {0};
        int maxDist {0};
        // For each person entering check the distance and put them into correct stalls.
        for(int i = 0; i < K; ++i) {
            // Count distances between empty stalls (i.e. go through vector and put
            // distance between first two occupied stalls into vector, then next distance, etc.
            // put position of occupied stalls into second vector)
            std::vector<int> posGapEnd;
            std::vector<int> gapLengths;
            int gapLength {0};
            for(int posStall = 0; posStall < bathroomStalls.size(); ++posStall) {
                bool freeStall = bathroomStalls.at(posStall);
                if (!freeStall) {
                    // std::cout << "Found occupied stall at position " << posStall << ". Storing length " << gapLength << "\n";
                    posGapEnd.push_back(posStall);
                    gapLengths.push_back(gapLength);
                    gapLength = 0;
                } else {
                    ++gapLength;
                }
            }
            // Find largest gap and tag the position it starts at
            int largestGap {0};
            int startPosLargestGap {-1};
            int endPosLargestGap {-1};
            for(int gap = 0; gap < gapLengths.size(); ++gap) {
                if (gapLengths.at(gap) > largestGap) {
                    largestGap = gapLengths.at(gap);
                    startPosLargestGap = posGapEnd.at(gap-1);
                    endPosLargestGap = posGapEnd.at(gap);
                }
            }
            // std::cout << "Largest gap has size " << largestGap << ", starts at " << startPosLargestGap << " and ends at " << endPosLargestGap << "\n";
            int chosenStall {static_cast<int>(startPosLargestGap + std::ceil(largestGap/2.))};
            minDist = chosenStall - startPosLargestGap - 1;
            maxDist = endPosLargestGap - chosenStall - 1;
            // std::cout << "Using stall at " << chosenStall << "\n";
            bathroomStalls.at(chosenStall) = false;
        }
        std::cout << "Case #" << testCase << ": " << maxDist << " " << minDist << "\n";
    }
}
