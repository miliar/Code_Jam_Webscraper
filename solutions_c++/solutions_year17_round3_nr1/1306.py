#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define PI (3.14159265359)

struct Pancake
{
    double H;
    double R;

    bool operator<(Pancake const& rhs) const
    {
        return R < rhs.R;
    }
};

double getArea(std::vector<Pancake>& ps)
{
    std::sort(ps.begin(), ps.end());
    double A = 0.;
    double currentR = 0.;

    // std::cout << "P: ";
    for (auto p : ps)
    {
        double aLast = currentR * currentR;
        double aThis = p.R * p.R;
        double aH = 2 * p.R * p.H;

        A += aThis - aLast + aH;

        // std::cout << A << ": " << p.R << " " << p.H << " --- " << aThis << " - " << aLast << " + " << aH;
        currentR = p.R;
    }

    // std::cout << std::endl;

    return A * PI;
}

double doStuff(std::vector<Pancake> in, std::vector<Pancake> cur, int const K)
{
    if (cur.size() == K)
    {
        return getArea(cur);
    }

    if (in.empty())
    {
        return -2.;
    }

    double maxArea = -1.;
    for (int i = 0; i < in.size(); ++i)
    {
        Pancake tmp = in[i];
        in[i] = in.back();
        in.pop_back();

        double a = doStuff(in, cur, K);
        maxArea = a > maxArea ? a : maxArea;
        
        cur.push_back(tmp);
        a = doStuff(in, cur, K);
        maxArea = a > maxArea ? a : maxArea;
    }

    return maxArea;
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

        std::vector<Pancake> pancakes;
        for (int i = 0; i < N; ++i)
        {
            int h, r;
            std::cin >> r >> h;
            Pancake p;
            p.H = (double)h;
            p.R = (double)r;

            pancakes.push_back(p);
        }

        std::vector<Pancake> empty;
        std::cout << "Case #" << iTest << ": " << doStuff(pancakes, empty, K) << std::endl;
    }

    return 0;
}