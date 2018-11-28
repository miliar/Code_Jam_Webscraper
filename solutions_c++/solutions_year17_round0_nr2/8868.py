#include <iostream>
#include <cstdlib>
#include <climits>
#include <fstream>
#include <vector>

typedef unsigned long long ullong;

long count_multiter (long n);
bool isTidy(ullong number);

int main() {
    std::ifstream infile("in.txt");
    if(infile)
    {
        ullong numCases;
        infile >> numCases;
        std::vector<ullong> testCases(numCases);
        for(ullong i = 0; i < numCases; i++)
        {
            ullong val;
            infile >> val;
            testCases[i] = val;
        }
        std::ofstream outfile("solution.txt");

        for(ullong i = 0; i < testCases.size(); i++)
        {
            for(ullong num = testCases[i]; num >= 0; num--)
            {
                if(isTidy(num))
                {
                    outfile << "Case #" << i+1 << ": " << num << std::endl;
                    break;
                }
            }
        }

        outfile.close();
        infile.close();
    }
    return 0;
}

bool isTidy(ullong number)
{
    ullong previousDigit = 0;
    bool first = true;
    while(number > 0)
    {
        bool decreasingOrEqual = number % 10 <= previousDigit;
        if(first) {
            first = false;
            decreasingOrEqual = true;
        }
        if(decreasingOrEqual)
        {
            previousDigit = number % 10;
            number = number / 10;
            if(number == 0)
            {
                return true;
            }
        }
        else
        {
            return false;
        }
    }
}

long count_multiter (long n)
{
    unsigned int num = abs(n);
    unsigned int x, i;
    for (x=10, i=1; ; x*=10, i++) {
        if (num < x)
            return i;
        if (x > LONG_MAX/10)
            return i+1;
    }
}