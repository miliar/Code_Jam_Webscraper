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
        if (k != n)
            return false;
        std::cerr << "k = " << k << "; n = " << n << std::endl;

        std::getline(in, line);
        units = std::stod(line);
        std::cerr << "units = " << units << std::endl;

        std::getline(in, line);
        size_t start = 0;
        for (int i = 0 ; i < n ; ++i)
        {
            pos = line.find(' ', start);
            probs.push_back(std::stod(line.substr(start, pos-start)));
            start = pos + 1;
        }

        /** TODO **/
        return true;
    }

private:
    int k;
    double units;
    std::vector<double> probs;
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
        out << " " << std::setprecision(20) << prob;
    }

private:
    double prob;
};


class Solver
{
public:
    Solver()
    {
    }

    void solve(Problem& problem, Solution& solution)
    {
        auto& p = problem.probs;
        std::sort(p.begin(), p.end(), [](double a, double b){return a > b;});

        std::vector<std::pair<double, int>> weights;
        for (int i = 0 ; i < p.size() ; ++i)
        {
            if (i > 0 && p[i] == p[i-1])
                ++weights.back().second;
            else
                weights.emplace_back(p[i], 1);
        }

        for (auto& x : weights)
            std::cerr << "weights: " << x.first << " " << x.second << std::endl;

        double u = problem.units;
        while (u > 0.0)
        {
            std::cerr << "u = " << u << std::endl;
            int sz = weights.size();
            auto x = weights.back();

            double prev = 1.0;
            if (sz > 1)
                prev = weights[sz-2].first;
            else if (x.first == 1.0)
                break;

            double d = prev - x.first;
            double diff = d * x.second;
            if (diff > u)
            {
                d = u / x.second;
                diff = u;
            }

            u -= diff;
            weights.back().first += d;

            if (sz > 1 && u > 0)
            {
                weights.pop_back();
                weights.back().second += x.second;
            }
        }

        for (auto& x : weights)
            std::cerr << "weights: " << x.first << " " << x.second << std::endl;

        double result = 1.0;
        for (auto& x : weights)
            for (int i = 0 ; i < x.second ; ++i)
                result *= x.first;
        solution.prob = result;
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

