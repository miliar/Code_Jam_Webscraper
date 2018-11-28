#include <iostream>
#include <iomanip>

int N,D;

void Solve(int T)
{
    std::cin >> D >> N;
    double t = 0;
    double x,v;
    for (int i=0;i<N;++i)
    {
        std::cin >> x >> v;
        t = std::max(t, (D-x)/v);
    }
    double speed = D / t;
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Case #" << T << ": " << speed << "\n";
}

int main(int argc, char **argv)
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
        Solve(i);
    return 0;
}