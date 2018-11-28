#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>
#include <iomanip>
typedef std::pair<int64_t, int64_t> ii;

double D;
int N;
const int MAXN = 1024;
double K[MAXN], S[MAXN];

double solve()
{
    double T = -1;
    for (int i=0; i < N; i++)
    {
        double t = (D - K[i]) / S[i];
        T = std::max(T, t);
    }
    return D / T;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::cin >> D >> N;
        for (int j=0; j<N; j++) std::cin >> K[j] >> S[j];
        double ans = solve();
        std::cout << "Case #" << i << ": ";
        std::cout << std::fixed << std::setprecision(7) << ans << "\n";
    }
}
