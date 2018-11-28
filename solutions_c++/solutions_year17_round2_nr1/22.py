/* My Template for the Google Code Jam.
 *
 * Compile: g++ -std=c++11 -lgmp -lgmpxx [-fopenmp]
 *  - I'm probably using some C++11 features.
 *  - I might use GMP (GNU Multiple Precision Arighmetic Library) so
 *    I'm including the library in the template even if they
 *    won't be used.
 *
 * This code is ugly but it works - otherwise you wouldn't be reading
 * it, right?
 */

#include <cassert>
//#define NDEBUG

#include <cstdlib>
#include <cstdint>
#include <cmath>

#include <iomanip>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <set>

#include <gmpxx.h>

using namespace std;
typedef size_t szt;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll> PLL;

typedef mpz_class mpz;

template<typename T>
void read_to_vector(size_t N, std::vector<T> &v) {
  for(size_t i=0; i<N; i++) {
    T tmp;
    std::cin >> tmp;
    v.push_back(tmp);
  }
}
template<typename T>
void print_vector(const std::vector<T> &v) {
  for(auto it = v.begin(); it<v.end(); it++) {
    if(it!=v.begin())
      std::cout << " ";
    std::cout << (*it);
  }
}

//Copy functions from TCR here.



//Solution:
struct Solver {
  stringstream output;

  ll d, n;
  vector<ll> k;
  vector<ll> s;

  void readinput() {
    cin >> d >> n;
    k.resize(n);
    s.resize(n);
    for (int i=0; i<n; i++) {
      cin >> k[i] >> s[i];
    }
  }

  double solve() {
    vector<double> t;
    for (int i=0; i<n; i++) {
      t.push_back((d - k[i]) * 1. / s[i]);
      //      output << "Test: "  << d << " " << k[i] << " " << s[i] << " " << t[i] << endl;
    }
    //    output << t[0];
    double maxt = t[0];
    for (double tt : t) {
      maxt = max(maxt, tt);
    }

    return d / maxt;
  }

};

//This is executed before any input is read.
void pre_compute() {
  
}

int main() {
  std::cout << std::setprecision(15);
  std::cin.tie(0);
  pre_compute();
  size_t T;
  std::cin >> T;
  vector<bool> finished(T+1, false);
  vector<Solver> solvers (T+1);
  int printed = 0;
  for (size_t i=1; i<=T; i++) {
    solvers[i].readinput();
    solvers[i].output << std::setprecision(15);
    solvers[i].output << std::fixed;
  }
#pragma omp parallel for schedule(dynamic,1)
  for(size_t i=1; i<=T; i++) {
    //CHOOSE A
    auto res = solvers[i].solve();
    solvers[i].output << "Case #" << i << ": " << res << "\n";

    //Print
#pragma omp critical
    {
      finished[i] = true;
      for (int j=printed+1; j<=T && finished[j]; j++) {
	cout << solvers[j].output.str();
	cout << std::flush;
	printed = j;
      }
    }

  }

  return 0;
}
