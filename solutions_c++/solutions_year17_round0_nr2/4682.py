// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> split(long long n)
{
    vector<int> v;
    while (n > 0) {
        v.push_back(n % 10);
        n /= 10;
    }
    return v;
}

void make_tidy(vector<int>& s)
{
    for (int i = s.size() - 1; i > 0; --i) {
        if (s[i] > s[i - 1]) {
            for (int j = 0; j < i; ++j)
                s[j] = 9;
            s[i]--;
            make_tidy(s);
            return;
        }
    }
}

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
            long long k = atoll(line.c_str());
            vector<int> s = split(k);
            make_tidy(s);
            int j = s.size() - 1;
            while (s[j] == 0 && j > 0)
                --j;
            output << "Case #" << i + 1 << ": ";
            for (int l = j; l >= 0; --l) {
                output << s[l];
            }
            output << endl;
        }

        input.close();
        output.close();
    }

    //system("pause");
    return 0;
}

