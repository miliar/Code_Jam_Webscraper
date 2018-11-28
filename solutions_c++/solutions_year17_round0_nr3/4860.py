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
#include <bitset>
#include <map>

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
        n = atoll(line.c_str());

        for (long long i = 0; i<n; ++i)
        {
            getline(input, line);
            istringstream iss(line);

            vector<string> tokens{ istream_iterator<string>{iss}, istream_iterator<string>{} };
            long long n = atoll(tokens[0].c_str());
            long long k = atoll(tokens[1].c_str());

            map<long long, int> m;
            m[n] = 1;

            for (long long j = 0; j < k-1; ++j) {
                long long largest_gap = m.rbegin()->first;
                m[largest_gap / 2]++;
                m[(largest_gap - 1) / 2]++;
                m[largest_gap]--;
                if (m[largest_gap] == 0)
                    m.erase(largest_gap);
            }

            long long largest_gap = m.rbegin()->first;
            output << "Case #" << i+1 << ": " << largest_gap/2 << " " << (largest_gap - 1) / 2;
            output << endl;
        }

        input.close();
        output.close();
    }

    return 0;
}

