#include <ios>
#include <iostream>
#include <iomanip>
#include <cstdio>

double maximum(double a, double b)
{
    return (a > b ? a : b);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    std::cin >> tc;
    double d, p, s, tm;
    int n;
    for (int t = 0; t < tc; t++)
    {
        std::cin >> d >> n;
        tm = -1;
        while (n--)
        {
            std::cin >> p >> s;
            if (tm < -0.5)
                tm = (d-p)/s;
            else
                tm = maximum(tm, (d-p)/s);
        }
        std::cout << "Case #" << t+1 << ": " << std::fixed << std::setprecision(9) << (d/tm) << '\n';
    }
}
