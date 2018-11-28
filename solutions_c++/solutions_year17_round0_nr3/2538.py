#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

long long finder(long long k)
{
    long long h, h2 = 1;
    for (h = -1; k != 0; ++h)
        k /= 2;
    while(h--)
        h2 *= 2;
    return h2;
}

long long miner(long long x)
{
    if (x % 2 == 0)
        return x / 2 - 1;
    else
        return (x - 1) / 2;
}

int main()
{
    ifstream fin;
    fin.open("C-large.in", ios::in);
    ofstream fout;
    fout.open("C-large_output.txt", ios::out);
    int t;
    long long n, k;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        fout << "Case #" << o << ": ";
        fin >> n >> k;
        long long pow2h = finder(k);
        if (k - pow2h <= (n - pow2h) % pow2h)
            fout << (n / pow2h) / 2 << " " << miner(n / pow2h) << endl;
        else
            fout << (n / pow2h - 1) / 2 << " " << miner(n / pow2h - 1) << endl;
    }
}

