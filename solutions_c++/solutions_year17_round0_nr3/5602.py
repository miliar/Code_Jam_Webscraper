/* IMPORTS ************************************************************************************************************/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <stdlib.h>
#include <iterator>

/* DEFINES ************************************************************************************************************/

#define _uInt64 unsigned long long int

#define GUARD_STALL_COUNT (2)

/* HELPER FUNCTIONS ***************************************************************************************************/

/**
 * Generic function to get input from cin;
 *
 * @tparam T Input type.
 *
 * @return The value;
 */
template<typename T>
static T getNextInput()
{
    T value;
    std::cin >> value;
    return value;
};

/**
 * Functor to get the largest less than or equal element in the container.
 *
 * @return The largest less than  or equal element in a container.
 */
template <class ForwardIterator, class T>
ForwardIterator largestLessThanOrEqualTo (ForwardIterator first, ForwardIterator last, const T& value)
{
    ForwardIterator upperb = std::upper_bound(first, last, value);

    if(upperb == first)
        return ++last;

    if(upperb == last)
        return upperb;

    return --upperb;
}

/* PROBLEM DOMAIN STRUCT AND FUNCTIONS ********************************************************************************/

/**
 * Problem parameters.
 */
struct Parameters
{
    _uInt64 stallCount;
    _uInt64 peopleCount;
};

/**
 * Problem parameters.
 */
struct Stall
{
    _uInt64 LHS;
    _uInt64 RHS;
    _uInt64 max;
    _uInt64 min;
    _uInt64 index;
};

/**
 * Functor for comparing two stalls.
 */
struct StallCompare {
    bool operator() (const Stall& lhs, const Stall& rhs) const
    {
        if (lhs.max > rhs.max)
            return true;

        return lhs.max == rhs.max && lhs.LHS < rhs.LHS;
    }
};

/* APPLICATION ********************************************************************************************************/

/**
 * Program entry point.
 *
 * @param argc Argument count.
 * @param argv Argument values.
 */
int main(int argc, char** argv)
{
    int testCaseCount = getNextInput<int>();

    std::vector<Parameters> testCases;

    for (int i = 0; i < testCaseCount; ++i)
    {
        Parameters params = { getNextInput<_uInt64 >(), getNextInput<_uInt64 >() };
        testCases.push_back(params);
    }

    int count = 1;
    for (Parameters params : testCases)
    {
        std::set<_uInt64> occupiedStalls;
        occupiedStalls.insert(params.stallCount + GUARD_STALL_COUNT - 1);
        occupiedStalls.insert(0);

        Stall result = { 0 };
        for (_uInt64 i = 0; i < params.peopleCount; ++i)
        {
            std::multiset<Stall, StallCompare> possibleStalls;
            for (_uInt64 j = 1; j <= params.stallCount + 1; ++j)
            {
                if (occupiedStalls.find(j) != occupiedStalls.end())
                    continue;

                _uInt64 mostRight = (*occupiedStalls.upper_bound(j)) - j - 1;
                _uInt64 mostLeft  = (j - (*(largestLessThanOrEqualTo(occupiedStalls.begin(), occupiedStalls.end(), j))) - 1);

                Stall stall = { mostLeft, mostRight, std::max(mostLeft, mostRight), std::min(mostLeft, mostRight), j };

                if (possibleStalls.empty())
                {
                    possibleStalls.insert(stall);
                }
                else
                {
                    Stall currentStall = *possibleStalls.begin();

                    if (stall.min > currentStall.min)
                    {
                        possibleStalls.clear();
                        possibleStalls.insert(stall);
                    }
                    else if (stall.min == currentStall.min)
                    {
                        possibleStalls.insert(stall);
                    }
                }
            }

            result = *possibleStalls.begin();
            occupiedStalls.insert(result.index);
        }

        std::cout << "Case #" << count << ": " << result.max << " " << result.min << std::endl;
        ++count;
    }

    return 0;
}