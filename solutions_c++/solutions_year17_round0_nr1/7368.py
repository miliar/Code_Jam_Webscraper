#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

void flip(string& s, int pos, int k)
{
    for (int i = 0; i < k; ++i)
    {
        if (s[pos + i] == '-')
            s[pos + i] = '+';
        else
            s[pos + i] = '-';
    }
}

int main()
{
    //ifstream in("small-practice.in");
    ifstream in("large-practice.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";
    
        string s;
        int k;
        in >> s >> k;

        int flips = 0;
        int pos;

        for (pos = 0; pos + k <= s.length(); ++pos)
        {
            if (s[pos] == '-')
            {
                flip(s, pos, k);
                ++flips;
            }
        }

        if (find(s.begin() + (pos-1), s.end(), '-') != s.end())
            out << "IMPOSSIBLE";
        else
            out << flips;

        out << endl;
    }

    return 0;
}
