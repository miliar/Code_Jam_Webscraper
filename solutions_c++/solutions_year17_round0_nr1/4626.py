#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>
#include <unistd.h>

using namespace std;

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases + 1; ++c)
    {
        string s;
        size_t k;
        is >> s >> k;

        size_t n(0);
        for (size_t i(0); i != s.size() - k; ++i)
        {
            if (s[i] == '+') continue;
            ++n;

            for (size_t j(i); j != i + k; ++j) s[j] = s[j] == '-' ? '+' : '-'; 
        } 

        if (s.substr(s.size() - k, k) == string(k, '+'))
          cout << "Case #" << c << ": " << n << endl;
        else if (s.substr(s.size() - k, k) == string(k, '-'))
          cout << "Case #" << c << ": " << n+1 << endl;
        else
          cout << "Case #" << c << ": IMPOSSIBLE" << endl;
    }
}
