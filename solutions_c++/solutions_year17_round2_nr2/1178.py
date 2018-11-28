#include <fstream>
#include <iostream>
#include <string>
#include <memory>

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
        size_t start = 0;

        size_t pos = line.find(' ', start);
        N = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        R = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        O = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        Y = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        G = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        B = std::stoi(line.substr(start, pos));

        start = pos+1;
        pos = line.find(' ', start);
        V = std::stoi(line.substr(start, pos));

        /** TODO **/
        return true;
    }

private:
    int N, R, O, Y, G, B, V;
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
        out << " " << result;
        if (result == "IMPOSSIBLE")
            return;
        for (int i = 0 ; i < result.size() ; ++i)
            if (result[i] == result[(i+1) % result.size()])
            {
                std::cerr << "ERROR @ " << ((i+1) % result.size()) << " in " << result << std::endl;
            }
    }

private:
    std::string result;
};


class Solver
{
public:
    Solver()
    {
    }

    enum Colors {
        orange, violet, green, red, yellow, blue
    };

    bool compat(int j, bool r, bool y, bool b)
    {
        switch (j)
        {
        case red:
            return r;
        case yellow:
            return y;
        case blue:
            return b;
        case orange:
            return r && y;
        case violet:
            return r && b;
        case green:
            return y && b;
        }
        return false;
    }

    void solve(Problem& p, Solution& solution)
    {
        int N = p.N;
        int R = p.R;
        int O = p.O;
        int Y = p.Y;
        int G = p.G;
        int B = p.B;
        int V = p.V;

        int r = p.R + p.O + p.V;
        int y = p.Y + p.G + p.O;
        int b = p.B + p.G + p.V;

        if (2*r > N || 2*y > N || 2*b > N)
        {
            solution.result = "IMPOSSIBLE";
            return;
        }

        std::array<int, 6> count;
        count[red] = R;
        count[yellow] = Y;
        count[blue] = B;
        count[orange] = O;
        count[violet] = V;
        count[green] = G;

        bool sR = true;
        bool sY = true;
        bool sB = true;
        for (int i = 0 ; i < N ; ++i)
        {
            /* Greedy algorithm, favoring (O,V,G,R,Y,B) */
            int choice = 0;
            int max = 0;
            for (int j = 0 ; j < 6 ; ++j)
            {
                if (compat(j, sR, sY, sB))
                {
                    if (count[j] > max)
                    {
                        max = count[j];
                        choice = j;
                    }
                }
            }
            //std::cerr << "R=" << count[red] << " Y=" << count[yellow] << " B=" << count[blue] << " O=" << count[orange] << " V=" << count[violet] << " G=" << count[green] << " => choice = " << choice << std::endl;
            --count[choice];

            char c;
            sR = sY = sB = true;
            switch (choice)
            {
            case red:
                c = 'R';
                sR = false;
                break;
            case yellow:
                c = 'Y';
                sY = false;
                break;
            case blue:
                c = 'B';
                sB = false;
                break;
            case orange:
                c = 'O';
                sR = false;
                sY = false;
                break;
            case violet:
                c = 'V';
                sR = false;
                sB = false;
                break;
            case green:
                c = 'G';
                sB = false;
                sY = false;
                break;
            }

            solution.result.push_back(c);
        }

        // Fix loop
        auto& result = solution.result;
        if (result[0] == result[N-1])
        {
            result[N-1] = result[N-2];
            result[N-2] = result[0];
        }
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

