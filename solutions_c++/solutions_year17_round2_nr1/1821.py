#include <iostream>
#include <math.h>
#include <fstream>
#include <string>
#include <inttypes.h>
#include <iomanip>

using namespace std;

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int64_t i, j, T, N;
    double maxi, D, K[1000], S[1000], time[1000];
    filin >> T;
    for (i = 0; i < T; i++)
    {
            filout << "Case #" << i + 1 << ": ";
            filin >> D >> N;
            maxi = 0;
            for (j = 0; j < N; j++)
            {
                filin >> K[j] >> S[j];
                time[j] = (D - K[j]) / S[j];
                if (maxi < time[j])
                    maxi = time[j];
            }
            filout << std::fixed;
            filout << std::setprecision (6) << D / maxi;
            filout << endl;
    }
    filin.close ();
    filout.close ();
}
