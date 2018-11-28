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
        ll n, k;
        ll left, right;
};

void CaseSolver::precompute() {
}

void CaseSolver::read(istream& is) {
    is >> n >> k;
}

void CaseSolver::solve() {
    while (k > 0) {
        left = (n - 1) / 2;
        right = n / 2;
        if (k == 1) {
            break;
        }
        --k;
        if (k % 2 == 1) {
            n = right;
            k = (k + 1) / 2;
        } else {
            n = left;
            k = k / 2;
        }
    }
}

void CaseSolver::write(ostream& os) {
    os << right << " " << left;
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
