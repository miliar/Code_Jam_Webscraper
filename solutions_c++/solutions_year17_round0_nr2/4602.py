#include <cmath>
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
        string z;
        is >> z;

        for (size_t i(z.size() - 1); i != 0; --i)
        {
            if (z[i-1] > z[i]) {
                z[i-1] = z[i-1] - 1;
                for (size_t j(i); j != z.size(); ++j) z[j] = '9';
            }
        } 

        if (z[0] == '0') z = z.substr(1, z.size() - 1);
        cout << "Case #" << c << ": " << z << endl;
    }
}
