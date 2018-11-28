#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

double doStuff(std::vector<double>& Ps, double U)
{
    std::sort(Ps.begin(), Ps.end());

    Ps.push_back(1.);

    for (int i = 1; i < Ps.size(); ++i)
    {
        double diff = Ps[i] - Ps[i-1];
        double boost;
        if (U > diff * i)
        {
            boost = diff;
        }
        else
        {
            boost = U / i;
        }

        for (int j = 0; j < i; ++j)
        {
            Ps[j] += boost;
            U -= boost;
        }

        // std::cout << "U left: " << U << std::endl;
    }

    Ps.pop_back();


    double P = 1.;
    // std::cout << "Ps: ";
    for (auto p : Ps)
    {
        // std::cout << p << " ";
        P *= p;
    }
    // std::cout << std::endl;

    return P;
}

int main()
{
    int nTests;
    std::cin >> nTests;
    std::cout.precision(17);

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        int N, K;
        std::cin >> N >> K;

        double U;
        std::cin >> U;

        std::vector<double> Ps;
        for (int i = 0; i < N; ++i)
        {
            double p;
            std::cin >> p;
            Ps.push_back(p);
        }


        std::cout << "Case #" << iTest << ": " << doStuff(Ps, U) << std::endl;
    }

    return 0;
}