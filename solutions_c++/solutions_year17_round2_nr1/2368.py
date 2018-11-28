#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test < T + 1; ++test)
    {

        long long D, N;
        cin >> D >> N;
        double t = 0.0;
        for (long long j = 0; j < N; ++j)
        {
            long long K, S;
            cin >> K >> S;
            t = max(static_cast<double>(D - K) / static_cast<double>(S), t);
        }

        printf("Case #%d: %.15f\n", test, D / t);
//        std::cout << "Case #" << test << ": ";
    }

    return 0;
}
