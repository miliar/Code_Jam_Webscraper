#include <iostream>
#include <fstream>

using namespace std;

ifstream in("B-large.in");
ofstream out("B-large.out");

//#define out cout

int main() {
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        unsigned long long n;
        in >> n;
        unsigned long long order = 1;
        for (int i = 0, prev = 10; n / order != 0; ++i) {
            int cur = n / order % 10;
            if (cur > prev) n -= n % order + 1;
            prev = n / order % 10;
            order *= 10;
        }
        out << "Case #" << i + 1 << ": " << n << '\n';
    }
    return 0;
}
