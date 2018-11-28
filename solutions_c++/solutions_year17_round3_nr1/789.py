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

        int n = std::stoi(line.substr(0, pos));
        k = std::stoi(line.substr(pos+1));

        for (int i = 0 ; i < n ; ++i)
        {
            std::getline(in, line);
            pos = line.find(' ');

            double r = std::stoi(line.substr(0, pos));
            double h = std::stoi(line.substr(pos+1));

            pancakes.emplace_back(r, h);
        }
        /** TODO **/
        return true;
    }

private:
    int k;
    std::vector<std::pair<double, double>> pancakes;
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
        out << " " << std::setprecision(20) << surface;
    }

private:
    double surface;
};


class Solver
{
public:
    Solver()
    {
    }

    void solve(Problem& problem, Solution& solution)
    {
        std::vector<std::pair<double, double>> surfaces;
        for (auto&& x : problem.pancakes)
        {
            constexpr double pi = 4 * std::atan(1);
            double r = x.first;
            double h = x.second;
            double side = 2 * pi * r * h;
            double top = pi * r * r;

            surfaces.emplace_back(side, top);
        }

        std::sort(surfaces.begin(), surfaces.end(), [](const std::pair<double, double>& lhs, const std::pair<double, double>& rhs) {return lhs.first > rhs.first;});
        double best = 0;

        for (int i = 0 ; i < surfaces.size() ; ++i)
        {
            double s = surfaces[i].first + surfaces[i].second;
            for (int j = 0, jj = 0 ; j+1 < problem.k ; ++j, ++jj)
            {
                if (jj == i)
                    ++jj;
                s += surfaces[jj].first;
            }

            if (s > best)
                best = s;
        }

        solution.surface = best;
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

