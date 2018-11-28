#include <fstream>
#include <algorithm>
#include <vector>
#include <assert.h>
#include <map>

#include <boost/range/algorithm/reverse.hpp>
#include <boost/range/algorithm/sort.hpp>

std::string process(size_t N, long R, long Y, long B)
{
    std::string res;

    std::vector<std::pair<char, long>> vals = {{'R', R}, {'Y', Y}, {'B', B}};

    boost::sort(vals, [] (auto a, auto b)
    {
        return a.second > b.second;
    });

    if (vals[0].second > N / 2)
        return "IMPOSSIBLE";

    size_t i = N - 2 * vals[0].second;
    if (i > vals[2].second)
        return "IMPOSSIBLE";

    while (i--)
    {
        for (auto & v: vals)
        {
            res.push_back(v.first);
            --v.second;
        }
    }

    for (size_t l = 0; l != vals[2].second; ++l)
    {
        res.push_back(vals[0].first);
        res.push_back(vals[2].first);
    }

    for (size_t l = 0; l != vals[1].second; ++l)
    {
        res.push_back(vals[0].first);
        res.push_back(vals[1].first);
    }

    return res;
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_b.txt");
    std::ofstream out("out_b.txt");

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t N;
        in >> N;

        size_t R, O, Y, G, B, V;
        in >> R >> O >> Y >> G >> B >> V;

        out << "Case #" << i + 1 << ": " << process(N, R, Y, B) << std::endl;
    }
}
