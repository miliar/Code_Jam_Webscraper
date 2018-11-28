#include <iostream>
#include <list>
#include <set>
#include <string>
#include <tuple>

using namespace std;

void PrintResult(uint64_t i, uint64_t flips)
{
    std::cout << "Case #" + to_string(i) << ": ";
    if (flips == UINT64_MAX)
        std::cout << "IMPOSSIBLE";
    else
        std::cout << to_string(flips);
    std::cout << std::endl;
}

std::string Flip(uint64_t index, uint64_t k, const std::string& row)
{
    std::string result;
    result.reserve(row.size());
    uint64_t highIndex = index + k;
    for (uint64_t i = 0; i < row.size(); ++i)
    {
        if (i >= index && i < highIndex)
            result += (row[i] == '+' ? '-' : '+');
        else
            result += row[i];
    }
    return result;
}

bool IsSolution(const std::string& row)
{
    for (size_t i = 0; i < row.size(); ++i)
    {
        if (row[i] != '+')
            return false;
    }
    return true;
}

void SolveTestCaseI(uint64_t i, const std::string& row, uint64_t k)
{
    std::set<std::string> testedCases;
    std::list<std::tuple<std::string, uint64_t>> queue;
    queue.push_back(std::make_tuple(row, 0));
    while (queue.size())
    {
        // do we have a result?
        if (IsSolution(std::get<0>(queue.front())))
        {
            PrintResult(i, std::get<1>(queue.front()));
            return;
        }
        // enqueue all the possible flips
        size_t numOfFlips = row.size() - k + 1;
        for (size_t i = 0; i < numOfFlips; ++i)
        {
            std::string flip = Flip(i, k, std::get<0>(queue.front()));
            if (testedCases.find(flip) != testedCases.end())
            {
                continue;
            }
            queue.push_back(std::make_tuple(std::move(flip), std::get<1>(queue.front()) + 1));
        }
        // prevent this one from being processed again
        testedCases.insert(std::get<0>(queue.front()));
        queue.pop_front();
    }
    PrintResult(i, UINT64_MAX);
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        std::string row;
        uint64_t k;
        std::cin >> row >> k;
        SolveTestCaseI(i, row, k);
    }
    return 0;
}
