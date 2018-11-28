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

  ll N;
  ll P;
  vector<ll> G;

  void readinput() {
    cin >> N >> P;
    read_to_vector(N, G);
  }

  ll solve() {
    vector<ll> numbers (4, 0);
    for (auto g : G) {
      numbers[g%P] ++;
    }
    if (false && P==2) {
      ll good = numbers[0] + (numbers[1]+1)/2;
      return good;
    }
    if (false && P==3) {
      ll good = numbers[0];
      ll paired = min(numbers[1], numbers[2]);
      good += paired;
      numbers[1] -= paired;
      numbers[2] -= paired;
      good += (numbers[1]+2)/3 + (numbers[2]+2)/3;
      return good;
    }
    if (true || P==4) {
      int best[111][111][111];
      for (int i=0; i<111; i++) {
	for (int j=0; j<111; j++) {
	  for (int k=0; k<111; k++) {
	    best[i][j][k] = 0;
	  }
	}
      }
      best[0][0][0] = 0;
      for (int i=0; i<=numbers[1]; i++) {
	for (int j=0; j<=numbers[2]; j++) {
	  for (int k=0; k<=numbers[3]; k++) {
	    ll thisv = i*1 + j*2 + k*3;
	    thisv %= P;

	    //	    cout << "DEBUG: " << i << " " << j << " " << k << ": " << best[i][j][k] << " " << thisv << endl;
	    
	    if (thisv == 0) {
	      best[i+1][j][k] = max(best[i+1][j][k], best[i][j][k] + 1);
	      best[i][j+1][k] = max(best[i][j+1][k], best[i][j][k] + 1);
	      best[i][j][k+1] = max(best[i][j][k+1], best[i][j][k] + 1);
	    } else {
	      best[i+1][j][k] = max(best[i+1][j][k], best[i][j][k]);
	      best[i][j+1][k] = max(best[i][j+1][k], best[i][j][k]);
	      best[i][j][k+1] = max(best[i][j][k+1], best[i][j][k]);
	    }
	  }
	}
      }

      
      return numbers[0] + best[numbers[1]][numbers[2]][numbers[3]];

    }
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
