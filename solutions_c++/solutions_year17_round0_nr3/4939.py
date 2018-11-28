#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        size_t N, K;
        cin >> N >> K;
        bool even;
        map<size_t, size_t> ms; // num of empty stalls, count of such sequences
        ms[N] = 1;
        do
        {
            auto it = --(ms.end()); // max sequence of empty stalls
            N = it->first;
            if (--(it->second) == 0)
                ms.erase(it);

            even = N % 2;
            N >>= 1; // N/2, get the middle stall
            ms[N] += 1;
            ms[even? N : N-1] += 1;
        } while (--K);

        cout << "Case #" << t << ": "
             << N << ' ' << (even? N : N - 1) << '\n';
    }
 }
