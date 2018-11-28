#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <limits>
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
        int d, n;
        is >> d >> n;
        double ss(std::numeric_limits<double>::max());

        for (size_t i(0); i != n; ++i)
        {
            int k, s;
            is >> k >> s;
            ss = std::min(ss, d/(static_cast<double>(d-k)/s));
        } 

        cout << "Case #" << c << ": " << fixed << ss << endl;
    }
}
