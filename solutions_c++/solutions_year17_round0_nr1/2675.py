
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("C:\\Compete\\FB2016\\A-large.in");

    ofstream fout("C:\\Compete\\FB2016\\output.txt");

    int T;  fin >> T;
    for (int i = 0; i < T; i++)
    {
        string line; int K = 0;
        std::getline(fin, line,  ' ');
        fin >> K;

        int size = line.size();
        int nf = 0;
        for (int j = 0; j < size - K +1; j++)
        {
            if (line[j] == '-')
            {
                nf++;
                for (int m = 0; m < K; m++)
                {
                    if (line[j + m] == '-')
                    {
                        line[j + m] = '+';
                    }
                    else if (line[j + m] == '+')
                    {
                        line[j + m] = '-';
                    }
                }
            }
        }

        bool possible = true;
        for (int j = size - K + 1; j < line.size(); j++)
        {
            if (line[j] == '-')
            {
                possible = false;
                break;
            }
        }

        if (!possible)
        {
            fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        }
        else
        {
            fout << "Case #" << i+1 << ": " << nf << endl;
        }

    }
    return 0;
}