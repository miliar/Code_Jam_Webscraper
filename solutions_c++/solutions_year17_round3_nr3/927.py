#include <iostream>
#include <iomanip>
#include <algorithm>
const int MAX = 50;

int N;
int K;
double P[MAX];
double D;

void Solve(int T)
{
    std::cin >> N >> K;
    std::cin >> D;
    for (int i=0;i<N;++i)
        std::cin >> P[i];

    std::sort(P, P+N);

    double sum = 0;
    double maxSum = 0;
    int last = -1;
    for (int i=0;i<N;++i)
    {
        //std::clog << "i: " << P[i] * i - sum << " < " << D << std::endl;
        if (P[i] * i - sum > D)
            break;
        sum += P[i];
        last = i;
    }
    //std::clog << "last: " << last << std::endl;
    double level = std::min((sum+D) / (last+1), 1.0);
    for (int i=0;i<=last;++i)
        P[i] = level;
    double result = 1;
    for (int i=0;i<N;++i)
        result *= P[i];
    //for (int i=0;i<N;++i)
    //    std::clog << P[i] << std::endl;
    std::cout.precision(6);
    std::cout << "Case #" << T << ": " << std::fixed << result << "\n";
}

int main()
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
        Solve(i);
    return 0;
}