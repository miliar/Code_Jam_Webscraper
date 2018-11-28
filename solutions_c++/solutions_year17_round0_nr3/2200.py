#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

unsigned level(unsigned long long k)
{
    unsigned l = 0;
    while(k > ((1ull << (l + 1)) - 1))
        ++l;
    return l;
}

unsigned long long largeSpace(unsigned long long n, unsigned l)
{
    return (n >> l);
}

unsigned long long smallSpace(unsigned long long n, unsigned l)
{
    for(unsigned i = 0;i < l; ++i)
        if((n & (1ull << i)) == 0)
            return largeSpace(n, l) - 1;
    return largeSpace(n, l);
}

unsigned long long numLargeSpaces(unsigned long long n, unsigned l)
{
    return (((1ull << l) - 1) & n) + 1;
}

pair<unsigned long long, unsigned long long> getMaxMinSpaces(unsigned long long n, unsigned long long k)
{
    const auto l = level(k);
    unsigned long long num_spaces_above = (1ull << l) - 1;
    const auto space = num_spaces_above + numLargeSpaces(n, l) >= k ? largeSpace(n, l) : smallSpace(n, l);
    return (space & 1) == 1 ? make_pair(space/2, space/2) : make_pair(space/2, space/2 - 1);
}

int main() 
{
    ifstream ifile("input.txt");
    ofstream ofile("output.txt");
    int t;
    ifile >> t;
    for(int i = 1; i <= t; ++i)
    {
        unsigned long long n, k;
        ifile >> n >> k;
        const auto spaces = getMaxMinSpaces(n, k);
        ofile << "Case #" << i << ": " << spaces.first << " " << spaces.second << endl;    
    }
	return 0;
}
