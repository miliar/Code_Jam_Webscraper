#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
//#define NDEBUG
#ifdef NDEBUG
  #define DEBUG( x )
#else
  #define DEBUG( x )  x
#endif
using namespace std;
typedef long long int ll;
typedef long double ld;

class CaseSolver {
    public:
        void static precompute();
        void read(istream& is);
        void solve();
        void write(ostream& os);
    private:
        ll n;
        ll result = 0;
        static int constexpr max_digits = 18;
        static int constexpr base = 10;
};

void CaseSolver::precompute() {
}

void CaseSolver::read(istream& is) {
    is >> n;
}

void CaseSolver::solve() {
    std::vector<int> digits;
    int mini = base;
    ll mul = 1;
    while (n > 0) {
        ll const digit = n % base;
        n /= base;
        digits.push_back(digit);
        if (digit <= mini) {
            result += digit * mul;
            mini = digit;
        } else {
            result = digit * mul - 1;
            mini = digit - 1;
        }
        mul *= base;
    }
}

void CaseSolver::write(ostream& os) {
    os << result;
}


int main() {
    CaseSolver::precompute();
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        CaseSolver caseSolver;
        caseSolver.read(cin);
        caseSolver.solve();
        cout << "Case #" << testCase << ": ";
        caseSolver.write(cout);
        cout << "\n";
	}
}
