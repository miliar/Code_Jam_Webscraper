#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

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
        n = std::stoi(line.substr(0, pos));
        int q = std::stoi(line.substr(pos+1));

        for (int i = 0 ; i < n ; ++i)
        {
            std::getline(in, line);
            pos = line.find(' ');
            horses.emplace_back(std::stoi(line.substr(0, pos)), std::stoi(line.substr(pos+1)));
        }

        for (int i = 0 ; i < n ; ++i)
        {
            std::getline(in, line);
            size_t start = 0;
            dist.emplace_back();

            for (int j = 0 ; j < n ; ++j)
            {
                pos = line.find(' ', start);
                dist.back().emplace_back(std::stoi(line.substr(start, pos)));
                start = pos + 1;
            }
        }

        for (int i = 0 ; i < q ; ++i)
        {
            std::getline(in, line);
            pos = line.find(' ');
            queries.emplace_back(std::stoi(line.substr(0, pos)), std::stoi(line.substr(pos+1)));
        }

        /** TODO **/
        return true;
    }

private:
    int n;
    // distance, speed
    std::vector<std::pair<double, double>> horses;
    std::vector<std::vector<double>> dist;
    std::vector<std::pair<int, int>> queries;
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
        for (auto t : times)
            out << " " << std::setprecision(15) << t;
    }

private:
    std::vector<double> times;
};


class Solver
{
public:
    Solver()
    {
    }

    void getmat(Problem& p)
    {
        auto n = p.n;
        auto& dist = p.dist;
        auto& horses = p.horses;

        for (int i = 0 ; i < n ; ++i)
        {
            horsetimes.emplace_back(n, -1);
            std::vector<double>& mat = horsetimes[i];

            std::vector<std::pair<int, double>> queue;
            queue.emplace_back(i, 0);

            double maxdist = horses[i].first;
            double speed = horses[i].second;
            double timeout = maxdist / speed;

            while (!queue.empty())
            {
                auto x = queue.back();
                queue.pop_back();

                if (mat[x.first] < 0 || x.second < mat[x.first])
                {
                    mat[x.first] = x.second;
                    for (int j = 0 ; j < n ; ++j)
                    {
                        if (dist[x.first][j] >= 0)
                        {
                            double t = x.second + dist[x.first][j] / speed;
                            if (t <= timeout && (mat[j] < 0 || t < mat[j]))
                                queue.emplace_back(j, t);
                        }
                    }
                }

                std::sort(queue.begin(), queue.end(), [](const std::pair<int, double>& lhs, const std::pair<int, double>& rhs) {return lhs.second > rhs.second;});
            }

            mat[i] = -1;

            /*
            std::cerr << "Times for horse " << i << " (speed = " << speed << ", dist = " << maxdist << ") :" << std::endl;
            for (int j = 0 ; j < n ; ++j)
                std::cerr << "[" << j << "] = " << mat[j] << std::endl;
            */
        }
        /** TODO **/
    }

    void solve(Problem& problem, Solution& solution)
    {
        getmat(problem);

        auto n = problem.n;

        for (auto q : problem.queries)
        {
            int start = q.first - 1;
            int end = q.second - 1;

            std::vector<double> mat(n, -1);

            std::vector<std::pair<int, double>> queue;
            queue.emplace_back(start, 0);

            while (!queue.empty())
            {
                auto x = queue.back();
                queue.pop_back();

                if (mat[x.first] < 0 || x.second < mat[x.first])
                {
                    mat[x.first] = x.second;
                    for (int j = 0 ; j < n ; ++j)
                    {
                        if (horsetimes[x.first][j] >= 0)
                        {
                            double t = x.second + horsetimes[x.first][j];
                            if (mat[j] < 0 || t < mat[j])
                                queue.emplace_back(j, t);
                        }
                    }
                }

                std::sort(queue.begin(), queue.end(), [](const std::pair<int, double>& lhs, const std::pair<int, double>& rhs) {return lhs.second > rhs.second;});
            }

            std::cerr << "Times for query " << start << " -> " << end << ":" << std::endl;
            for (int j = 0 ; j < n ; ++j)
                std::cerr << "[" << j << "] = " << std::setprecision(15) << mat[j] << std::endl;

            solution.times.emplace_back(mat[end]);
        }
        /** TODO **/
    }

    std::vector<std::vector<double>> horsetimes;
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

