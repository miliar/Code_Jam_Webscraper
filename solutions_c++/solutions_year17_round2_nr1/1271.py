#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>

class Problem
{
    friend class Solver;

public:
    Problem()
    {
    }

    bool parse(std::istream& in)
    {
        time = 0;

        std::string line;
        std::getline(in, line);
        size_t pos = line.find(' ');
        dest = std::stoi(line.substr(0, pos));
        int n = std::stoi(line.substr(pos+1));

        std::cerr << "n = " << n << std::endl;
        for (int y = 0 ; y < n ; ++y)
        {
            std::getline(in, line);
            pos = line.find(' ');
            double start = std::stoi(line.substr(0, pos));
            double speed = std::stoi(line.substr(pos+1));
            if (start < dest)
            {
                double t = (dest - start) / speed;
                if (t > time)
                    time = t;
            }
        }

        /** TODO **/
        return true;
    }

private:
    double dest;
    double time;
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
        out << " " << std::setprecision(15) << speed;
    }

private:
    double speed;
};


class Solver
{
public:
    Solver()
    {
    }

    void solve(Problem& problem, Solution& solution)
    {
        solution.speed = problem.dest / problem.time;
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

