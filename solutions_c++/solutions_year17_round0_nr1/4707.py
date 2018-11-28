// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
    string line;
    ifstream input("Input.txt");
    ofstream output("Output.txt");
    long long n;

    if (input.is_open() && output.is_open())
    {
        getline(input, line);
        n = atoi(line.c_str());

        for (long long i=0;i<n;++i)
        {
            getline(input, line);
            istringstream iss(line);

            vector<string> tokens{istream_iterator<string>{iss}, istream_iterator<string>{}};
            int k = atoi(tokens[1].c_str());
            std::string pancakes = tokens[0];

            int o = 0;
            for (int j = 0; j < pancakes.length() && o >=0; ++j) {
                if (pancakes[j] == '-') {
                    //flip starting from position j
                    if (j > pancakes.length() - k)
                        o = -1;
                    else {
                        ++o;
                        for (int l = 0; l < k; ++l)
                            pancakes[j + l] = pancakes[j + l] == '-' ? '+' : '-';
                    }
                }
            }
            output << "Case #" << i + 1 << ": ";
            if (o == -1)
                output << "IMPOSSIBLE";
            else
                output << o;
            output << endl;
        }

        input.close();
        output.close();
    }

    //system("pause");
    return 0;
}

