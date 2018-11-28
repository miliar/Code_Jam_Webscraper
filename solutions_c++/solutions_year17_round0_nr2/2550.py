#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;

bool isTidy (uint64_t num);

uint64_t uintPow10(int k)
{
    uint64_t res = 1;
    while (k>0)
    {
        res*=10;
        k--;
    }
    return res;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;

    fin >> T;

    for (int t = 0; t < T; t++)
    {
        uint64_t number;
        fin >> number;

        while (1)
        {
            auto numStr = to_string(number);
            int i;
            bool fail = false;
            for (i = 0; i < numStr.size() - 1; i++)
            {
                if (numStr[i] > numStr[i + 1])
                {
                    fail = true;
                    break;
                }
            }
            if (!fail)
                break;
            auto mStr = numStr.substr(i+1);
            stringstream ss(mStr);
            uint64_t m;
            ss >> m;
            number = number - m - 1;
        }

        fout << "Case #" << (t+1) << ": " << number << endl;
    }

    return 0;
}

