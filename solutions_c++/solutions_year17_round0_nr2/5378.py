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

/* PROBLEM DOMAIN FUNCTIONS *******************************************************************************************/

/**
 * Gets the next possible tidy in the sequence. (ignoring subrages that we know for sure cant be tidy).
 *
 * @param number The number to verify.
 *
 * @return The next tidy number.
 */
void
getLastTiddy(std::string& number)
{
    if (number.length() == 1)
        return;

    unsigned int lastIndex = number.length() - 1;
    for (int i = lastIndex; i >= 1; --i)
    {
        char current  = number[i];
        char previous = number[i - 1];

        if (current < previous)
        {
            std::memset(&number[i], '9', number.length() - i);
            number[i - 1] = static_cast<char>(previous - 1);
        }
    }
}

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

    std::vector<unsigned long long int> testCases;

    for (int testCaseIndex = 0; testCaseIndex < testCaseCount; ++testCaseIndex)
        testCases.push_back(getNextInput<unsigned long long int>());

    int caseCount = 1;
    for (unsigned long long int testCase : testCases)
    {
        std::string value = std::to_string(testCase);
        getLastTiddy(value);

        std::cout << "Case #" << caseCount << ": " << strtoull(value.c_str(), NULL, 10) << std::endl;
        ++caseCount;
    }

    return 0;
}