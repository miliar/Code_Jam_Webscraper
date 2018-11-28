#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <fstream>

using namespace std;

int main()
{
    ofstream fout("lol.in");
    ifstream fin("kek.in");
    long long N, T;
    fin >> T;
    string s;
    for (long long i = 0; i < T; ++i)
    {
        fin >> s >> N;
        long long counter = 0, cool = s.find('-');
        while (cool < s.size() && counter <= s.size() - N + 1)
        {
            for (long long j = cool; j < s.size() && j < cool + N && cool + N <= s.size(); ++j)
            {
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
            }
            ++counter;
            cool = s.find('-');
        }
        if (cool > s.size())
            fout << "Case #" << i + 1 << ": " << counter << endl;
        else
            fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
    fin.close();
    fout.close();
}
