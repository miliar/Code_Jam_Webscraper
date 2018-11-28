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
        size_t n,k;
        is >> n >> k;

        multiset<size_t> spaces;
        spaces.insert(n);

        size_t min,max;
        for (size_t i(0); i != k; ++i)
        {
            auto it = spaces.end();
            --it;
            size_t largest = *it;
            spaces.erase(it);
            max = largest/2;
            if (largest % 2 == 0) min = max - 1;
            else min = max;
            spaces.insert(max);
            spaces.insert(min);
        } 

        cout << "Case #" << c << ": " << max << " " << min << endl;
    }
}
