#include <cassert>
#include <fstream>
#include <iostream>
#include <string>

using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;

int main(int argc, char* argv[])
{
    assert(argc == 3);
    ifstream in (argv[1]);
    ofstream out (argv[2]);
    int T = 0;

    in >> T;

    for (int i = 0; i < T; i++)
    {
        int K, count = 0;
        string str;

        out << "Case #" << i + 1 << ": ";
        in >> str >> K;
        unsigned long j = 0;
        for (j = 0; j < str.length() - K + 1; j++)
        {
            if (str[j] == '-')
            {
                count++;
                for (int k = 0; k < K; k++)
                    str[j + k] = str[j + k] == '+' ? '-' : '+';
            }
        }
        if (str.find("-") != string::npos)
            out << "IMPOSSIBLE" << endl;
        else
            out << count << endl;
    }
}

