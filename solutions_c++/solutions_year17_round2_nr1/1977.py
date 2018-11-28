#include <iostream>
#include <string>
#include <vector>

struct Horse
{
    double pos;
    double speed;
};

double doStuff(std::vector<Horse> horses, double D)
{
    double max_time = 0.;

    for (auto h : horses)
    {
        double dist_left = D - h.pos;
        double time = dist_left / h.speed;
        if (time > max_time)
        {
            max_time = time;
        }
    }

    return D / max_time;
}

int main()
{
    int nTests;
    std::cin >> nTests;
    std::cout.precision(17);

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        int D, N;
        std::cin >> D >> N;

        std::vector<Horse> horses;
        for (int i = 0; i < N; ++i)
        {
            long long p, s;
            std::cin >> p >> s;
            Horse h = {(double)p, (double)s};
            horses.push_back(h);
        }

        std::cout << "Case #" << iTest << ": ";
        std::cout << doStuff(horses, (double)D) << std::endl;
    }

    return 0;
}