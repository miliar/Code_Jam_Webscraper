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
    std::string pancakeRow;
    _uInt64     flipperSize;
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
        Parameters params = { getNextInput<std::string >(), getNextInput<_uInt64 >() };
        testCases.push_back(params);
    }

    int count = 1;
    for (Parameters params : testCases)
    {
        int flipCount = 0;
        std::string result;

        for (_uInt64 i = 0; i < params.pancakeRow.size(); ++i)
        {
            if ((i + params.flipperSize) > params.pancakeRow.size())
                break;

            if (params.pancakeRow[i] != '+')
            {
                for (_uInt64 j = 0; j < params.flipperSize; ++j)
                    params.pancakeRow[i + j] = params.pancakeRow[i + j] == '+' ? '-' : '+';

                ++flipCount;
            }
        }

       if (params.pancakeRow.find('-') != std::string::npos)
       {
           result = "IMPOSSIBLE";
       }
       else
       {
           result = std::to_string(flipCount);
       }

        std::cout << "Case #" << count << ": " << result << std::endl;

        ++count;
    }

    return 0;
}