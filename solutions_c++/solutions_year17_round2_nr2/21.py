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

  ll N, R, O, Y, G, B, V;

  void readinput() {
    cin >> N >> R >> O >> Y >> G >> B >> V;
  }

  void add (string & s0, int i, string sadd, int count) {
    if (count == 0) { return; }
    string res;
    res = s0.substr(0, i);
    for (int k = 0; k<count; k++) {
      res += sadd;
    }
    res += s0.substr(i, s0.size()-i);

    s0 = res;
  }

  string solve() {
    ll Y0 = Y;
    ll R0 = R;
    ll B0 = B;

    //Special case: Only of two species?
    ll sum = Y+V+R+G+B+O;
    if (Y == V && Y+V == sum ) {
      string res;
      add(res, 0, "YV", Y);
      return res;
    } 
    if (B == O && B+O == sum ) {
      string res;
      add(res, 0, "BO", O);
      return res;
    } 
    if (R == G && R+G == sum ) {
      string res;
      add(res, 0, "RG", G);
      return res;
    } 


    //TODO TODO
    Y -= V;
    R -= G;
    B -= O;
    if ((Y<1 && V>0) || (R<1 && G>0) || (B <1 && O>0)) { return "IMPOSSIBLE"; }

    if (R > Y+B) { return "IMPOSSIBLE"; }
    if (Y > R+B) { return "IMPOSSIBLE"; }
    if (B > Y+R) { return "IMPOSSIBLE"; }

    string res;
    while (Y>0 || R>0 || B>0) {
      char prev = '0';
      if (res.size()>0) { prev = res[res.size()-1]; }

      vector<pair<int, char> > ps;
      ps.push_back(make_pair(prev=='Y' ? 0 : -Y, 'Y'));
      ps.push_back(make_pair(prev=='B' ? 0 : -B, 'B'));
      ps.push_back(make_pair(prev=='R' ? 0 : -R, 'R'));
      sort(ps.begin(), ps.end());
      char c = ps[0].second;
      if (c == 'Y') { Y--; }
      if (c == 'R') { R--; }
      if (c == 'B') { B--; }
      res += c;
      //      cout << "Add: " << res << endl;;
    }


    if (res[res.size()-1] == res[0]) {
      swap(res[res.size()-1], res[res.size()-2]);
    }

    //Add rest
    add(res, res.find('Y'), "YV", V);
    add(res, res.find('B'), "BO", O);
    add(res, res.find('R'), "RG", G);

    assert(res.size() == N);
    assert(count(res.begin(), res.end(), 'Y') == Y0);
    assert(count(res.begin(), res.end(), 'R') == R0);
    assert(count(res.begin(), res.end(), 'B') == B0);
    assert(count(res.begin(), res.end(), 'O') == O);
    assert(count(res.begin(), res.end(), 'V') == V);
    assert(count(res.begin(), res.end(), 'G') == G);

    return res;
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
  //#pragma omp parallel for schedule(dynamic,1)
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
