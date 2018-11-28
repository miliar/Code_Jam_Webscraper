#include <iostream>
#include <fstream>
using namespace std;
ifstream ka("C-large.in");
ofstream ki("output.out");

int t;
long long n, k;

int main()
{
    ka >> t;
    for(int caz = 1; caz <= t; caz++)
    {
        ka >> n >> k;
        int i = 0;
        for(; (1LL << i) <= k; i++);
        i--;
        //cout << i << " ";
        n = (n - k + (1LL << i)) / (1LL << i);
        //cout << n << '\n';
        ki << "Case #" << caz << ": " << n / 2 << " " << (n - 1) / 2 << '\n';
    }
}
