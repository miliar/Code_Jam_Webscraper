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
#include <iomanip>
#include <map>
#include <set>

#define PI 3.141592653589793238462643383279

using namespace std;

int main()
{
    string line;
    ifstream input("Input.in");
    ofstream output("Output.in");

    if (input.is_open() && output.is_open())
    {
        getline(input, line);
        long long t = atoll(line.c_str());

        for (long long i = 0; i<t; ++i)
        {
            getline(input, line);
            istringstream iss(line);

            vector<string> tokens{ istream_iterator<string>{iss}, istream_iterator<string>{} };
            long long n = atoll(tokens[0].c_str());
            long long k = atoll(tokens[1].c_str());
            
            std::multimap<double, double> pancakes;
            for (long long j = 0; j < n; ++j)
            {
                getline(input, line);
                istringstream iss(line);

                vector<string> ps{ istream_iterator<string>{iss}, istream_iterator<string>{} };
                double r = atof(ps[0].c_str());
                double h = atof(ps[1].c_str());

                pancakes.insert(std::pair<double, double>(r, h));
            }

            //For each pancake, calculate the max area if this pancake is at the bottom (PI * rbottom** + sum(heights)) 
            double max = 0;

            for (auto& it = pancakes.begin(); it != pancakes.end();++it)
            {
                double r = it->first;
                double s = PI * r * r + 2 * PI * r * it->second;

                //Find K-1 pancakes rk < r that maximise height
                std::multiset<double> pl;
                for (auto& it2 = pancakes.begin(); it2 != pancakes.end(); ++it2)
                    if (it != it2 && it2->first <= r)
                        pl.insert(2 * PI* it2->first * it2->second);
                
                if (pl.size() >= k - 1)
                {
                    long long left = k - 1;
                    for (auto& it2 = pl.rbegin(); it2 != pl.rend(); ++it2)
                    {
                        if (left > 0)
                        {
                            s += *it2;
                            --left;
                        }
                    }

                    if (s > max)
                        max = s;
                }
            }

            output << "Case #" << i + 1 << ": " << setprecision(9) << fixed << max << endl;
        }

        input.close();
        output.close();
    }

    return 0;
}

