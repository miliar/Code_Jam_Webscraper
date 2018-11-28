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
        static std::string const impossible;
        std::string pancakes;
        int k;
        int result;
        bool solution_exists;
};

std::string const CaseSolver::impossible = "IMPOSSIBLE";

void CaseSolver::precompute() {
}

void CaseSolver::read(istream& is) {
    is >> pancakes >> k;
}

void CaseSolver::solve() {
    result = 0;
    solution_exists = true;
    std::queue<int> flips;
    bool flip = false;
    for (int i = 0; i < pancakes.size(); ++i) {
        if (!flips.empty() && flips.front() == i) {
            //std::cerr << "autoflip " << i << std::endl;
            flip = !flip;
            flips.pop();
        }
        if (flip ^ (pancakes[i] == '-')) {
            //std::cerr << "need flip " << i << std::endl;
            if (i + k <= pancakes.size()) {
                ++result;
                flips.push(i + k);
                flip = !flip;
            } else {
                result = -1;
                solution_exists = false;
                return;
            }
        }
    }
}

void CaseSolver::write(ostream& os) {
    if (solution_exists) {
        os << result;
    } else {
        os << impossible;
    }
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
