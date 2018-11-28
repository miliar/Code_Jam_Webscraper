//
//  stalls.cpp
//  codejam
//
//
#include <stdio.h>
#include <iostream>
#include <sstream>

std::string solveStalls(long long n, long long k)
{
    std::ostringstream os;
    const long long N = n;
    long long i = 1; long long accum = 0;
    while (i<k) {
        accum+=i; k-=i; n/=2; i=i<<1;
    }
    // Max number of slots at this level are i
    // Max empty n, Min empty is n-1
    // Left folks are in k, Left stalls are N-accum
    long long leftStalls = N - accum;
    long long numberLessThanN = i*n - leftStalls;
    if (k>(i-numberLessThanN)) { n = n-1; }
    os << n/2 << " ";
    os << ((n%2) ? n/2 : (n-1)/2);
    return os.str();
}

int main() {
    int tests = 0;
    std::cin >> tests;
    for (int i=1;i<=tests;i++) {
        long long n, k;
        std::cin >> n >> k;
        std::cout << "Case #" << i << ": " << solveStalls(n,k) << std::endl;
    }
    return 0;
}
