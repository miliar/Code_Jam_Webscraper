#include <iostream>
#include <string>
#include <fstream>
#include <inttypes.h>

using namespace std;

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int64_t i, j, T, N, K, power_2[60], a, m, l;
    power_2[0] = 1;
    for (i = 1; i < 60; i++)
        power_2[i] = power_2[i - 1] * 2;
    filin >> T;
    for (i = 0; i < T; i++)
    {
        filin >> N >> K;
        filout << "Case #" << i + 1 << ": ";
        for (j = 0; j < 60; j++)
            if (K < power_2[j])
                break;
        a = j - 1;
        m = (N - (power_2[a] - 1)) / power_2[a];
        l = (N - (power_2[a] - 1)) % power_2[a];
        if (K - (power_2[a] - 1) <= l && l > 0 && (m % 2))
            filout << (m + 1) / 2 << " " << (m - 1) / 2 << endl;
        if (K - (power_2[a] - 1) <= l && l > 0 && !(m % 2))
            filout << m / 2 << " " << m / 2 << endl;
        if ((K - (power_2[a] - 1) > l || l == 0) && (m % 2))
            filout << (m - 1) / 2 << " " << (m - 1) / 2 << endl;
        if ((K - (power_2[a] - 1) > l || l == 0) && !(m % 2))
            filout << m / 2 << " " << (m - 2) / 2 <<  endl;
    }
    filin.close ();
    filout.close ();
    return 0;
}
