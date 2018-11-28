#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <memory>
#include <vector>
#include <array>

class Problem
{
    friend class Solver;

public:
    Problem()
    {
    }

    bool parse(std::istream& in)
    {
        std::string line;
        std::getline(in, line);
        size_t pos = line.find(' ');

        ac = std::stoi(line.substr(0, pos));
        aj = std::stoi(line.substr(pos+1));
        if (ac+aj > 2)
            return false;

        for (int i = 0 ; i < ac ; ++i)
        {
            std::getline(in, line);
            pos = line.find(' ');
            int start = std::stoi(line.substr(0, pos));
            int end = std::stoi(line.substr(pos+1));
            cd.emplace_back(start, end);
        }

        for (int i = 0 ; i < aj ; ++i)
        {
            std::getline(in, line);
            pos = line.find(' ');
            int start = std::stoi(line.substr(0, pos));
            int end = std::stoi(line.substr(pos+1));
            jk.emplace_back(start, end);
        }

        /** TODO **/
        return true;
    }

private:
    int ac;
    int aj;
    std::vector<std::pair<int, int>> cd;
    std::vector<std::pair<int, int>> jk;
};


class Solution
{
    friend class Solver;

public:
    Solution()
    {
    }

    void print(std::ostream& out) const
    {
        /** TODO **/
        out << " " << count;
    }

private:
    int count;
};


class Solver
{
public:
    Solver()
    {
    }

    void solve(Problem& problem, Solution& solution)
    {
        if (problem.ac <= 1 && problem.aj <= 1)
        {
            solution.count = 2;
            return;
        }

        if (problem.ac < problem.aj)
        {
            std::swap(problem.ac, problem.aj);
            std::swap(problem.cd, problem.jk);
        }

        auto& ac = problem.ac;
        auto& aj = problem.aj;
        auto& cd = problem.cd;
        auto& jk = problem.jk;

        std::sort(cd.begin(), cd.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b){return a.first < b.first;});
        std::sort(jk.begin(), jk.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b){return a.first < b.first;});

        if (problem.ac == 2 && problem.aj == 0)
        {
            int t1 = cd[0].second - cd[0].first;
            int t2 = cd[1].second - cd[1].first;
            int tt = cd[1].first - cd[0].second;
            std::cerr << t1 << ", " << t2 << ", " << tt << std::endl;

            if (tt >= 720 || t1 + t2 + tt <= 720)
                solution.count = 2;
            else
                solution.count = 4;
            return;
        }

        solution.count = problem.ac + problem.aj;
        /** TODO **/
    }
};


int main(int argc, char** argv)
{
    if (argc != 2)
    {
        std::cerr << "Expected one argument (input file)" << std::endl;
        return 1;
    }

    std::ifstream ifs(argv[1]);
    std::string line;
    std::getline(ifs, line);
    int count = std::stoi(line);
    std::cerr << "Found " << count << " test cases" << std::endl;

    for (int i = 0 ; i < count ; ++i)
    {
        Problem problem;
        if (!problem.parse(ifs))
            std::cerr << "Could not parse the problem!" << std::endl;

        Solution solution;
        Solver solver;
        solver.solve(problem, solution);

        std::cout << "Case #" << (i+1) << ":";
        solution.print(std::cout);
        std::cout << std::endl;
    }

    return 0;
}

