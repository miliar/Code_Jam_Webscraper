#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");

    int N;

    fin >> N;

    for (int t = 0; t < N; t++)
    {
        std::string S;
        int K;
        bool impossible = false;
        fin >> S >> K;
        int i = 0;
        int result = 0;

        while(i < S.size())
        {
            if (S[i] == '+')
            {
                i++;
                continue;
            }

            if (i + K > S.size())
            {
                impossible = true;
                break;
            } else {
                result++;
                for (int r = 0; r < K; r++)
                {
                    S[i+r] = S[i+r] == '+' ? '-' : '+';
                }
            }
            i++;
        }

        fout << "Case #" << (t+1) << ": ";
        if (impossible)
        {
            fout << "IMPOSSIBLE" << endl;
        } else {
            fout << result << endl;
        }
    }

    return 0;
}