// CodeJame2017.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <inttypes.h>
#include <stdint.h>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define DB false

void stall(int64_t N, int64_t k)
{
    if (N == k)
    {
        printf("0 0");
        return;
    }

    // map stall space size to count
    std::map<int64_t, int64_t> stalls;
    std::set<int64_t> stallSizes;

    stalls[N] = 1;
    stallSizes.insert(N);

    for (int64_t i = 0; i < k - 1; i++)
    {
        int64_t maxSize = *stallSizes.rbegin();
        stalls[maxSize] -= 1;
        if (stalls[maxSize] == 0)
        {
            stallSizes.erase(maxSize);
            stalls.erase(maxSize);
        }
        
        // occupy the stall
        int64_t occupiedSize = maxSize - 1;
        int64_t leftSize = occupiedSize / 2;
        int64_t rightSize = occupiedSize / 2 + (occupiedSize % 2);
        
        stalls[leftSize] += 1;
        stallSizes.insert(leftSize);

        stalls[rightSize] += 1;
        stallSizes.insert(rightSize);
    }

    int64_t maxSize = *stallSizes.rbegin();
    int64_t occupiedSize = maxSize - 1;
    int64_t leftSize = occupiedSize / 2;
    int64_t rightSize = occupiedSize / 2 + (occupiedSize % 2);

    printf("%" PRId64 " %" PRId64, rightSize, leftSize);
}


int main()
{
    std::ifstream input("3.in");

    int cases = 0;
    input >> cases;

    std::string line;
    std::getline(input, line);

    for (int caseNumber = 0; caseNumber < cases; caseNumber++)
    {
        printf("Case #%d: ", caseNumber + 1);

        int64_t N, K;
        input >> N >> K;

        stall(N, K);

        printf("\n");
    }

    DB && getchar();


    return 0;
}

