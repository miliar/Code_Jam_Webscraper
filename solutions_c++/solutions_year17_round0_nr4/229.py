/* My Template for the Google Code Jam.
 *
 * Compile: g++ -std=c++11 -lgmp -lgmpxx
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

#include <gmpxx.h>

using namespace std;
typedef size_t szt;

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int,int> PII;

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

int aug(int u, vector<vector<int> > & EL, vector<int> & PV, vector<int> & Vis, int id) {
    for (int v : EL[u]) {
        if (Vis[v]!=id) {
            Vis[v]=id;
            if(PV[v]==-1 || aug(PV[v],EL,PV,Vis,id)==1) {
                PV[v]=u;
                return 1;
            }
        }
    }
    return 0;
}

vector<int> bipMatch(vector<vector<int> > & EL, int UNum, int VNum) {
  vector<int> PV (VNum, -1);
  vector<int> Vis (VNum, 0);
  int id=1;
  for (int u = 0; u < UNum; u++) {
    id += aug(u,EL,PV,Vis,id);
  }
  //  return id-1;
  //  cout << "BAA";
  //  print_vector(PV);
  /*
  cout << "Bipmatch input: " << endl;
  for (auto v : EL) {
    cout << "EL: ";
    print_vector(v);
    cout << endl;
  }
  cout << "Bipmatch result: " << (id-1) << endl;
*/
  return PV;
}


//Solution:
struct Solver {
  stringstream output;

  int N, K;
  vector<PII> x;
  vector<PII> plus;

  void readinput() {
    cin >> N >> K;
    for (int i=0; i<K; i++) {
      char c;
      int ii, j;
      cin >> c >> ii >> j;
      ii--; j--;
      if (c=='x' || c=='o') { x.push_back(make_pair(ii,j)); }
      if (c=='+' || c=='o') { plus.push_back(make_pair(ii,j)); }
    }
  }

  vector<PII> get_newx() {
    vector<bool> usedi (N, 0);
    vector<bool> usedj (N, 0);
    for (auto p : x) {
      usedi[p.first] = true;
      usedj[p.second] = true;
    }

    vector<PII> res;

    int j=0;
    for (int i=0; i<N; i++) {
      if (usedi[i]) { continue; }
      while (usedj[j]) { j++; }
      res.push_back(make_pair(i, j));
      usedj[j] = true;
    }
    return res;
  }

  vector<PII> get_newplus() {
    vector<PII> res;

    vector<bool> useda (2*N, 0);
    vector<bool> usedb (2*N, 0);
    for (auto p : plus) {
      useda[p.first + p.second] = true;
      usedb[p.first - p.second + N - 1] = true;
    }

    vector<vector<int> > EL (2*N, vector<int>());
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
	if (!useda[i+j] && !usedb[N - 1 + i - j]) {
	  EL[i+j].push_back(N - 1 + i-j);
	}
      }
    }
    auto PV = bipMatch(EL, 2*N, 2*N);
    for (int a=0; a<2*N; a++) {
      if (PV[a] != -1) {
	int b = PV[a];
	
	int i = (a+b - N + 1)/2;
	int j = b-i; //A and B wrong way!!
	res.push_back(make_pair(i,j));
      }
    }
    return res;
  }

  void solve() {

    vector<vector<bool> > isx (N, vector<bool>(N, false));
    vector<vector<bool> > isplus (N, vector<bool>(N, false));
    vector<vector<char> > board (N, vector<char>(N, '.'));

    for (auto p : x) {
      isx[p.first][p.second] = true;
      board[p.first][p.second] = 'x';
    }
    for (auto p : plus) {
      isplus[p.first][p.second] = true;
      if (board[p.first][p.second] == 'x') {
	board[p.first][p.second] = 'o';
      } else {
	board[p.first][p.second] = '+';
      }
    }

    vector<PII> newx = get_newx();
    vector<PII> newplus = get_newplus();
    auto newboard = board;
    for (auto p : newx) {
      if (newboard[p.first][p.second] == '+') {
	newboard[p.first][p.second] = 'o';
      } else {
	newboard[p.first][p.second] = 'x';
      }
    }
    for (auto p : newplus) {
      if (newboard[p.first][p.second] == 'x') {
	newboard[p.first][p.second] = 'o';
      } else {
	newboard[p.first][p.second] = '+';
      }
    }

    ll count = 0;
    stringstream thisout;
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
	if (newboard[i][j] != board[i][j]) {
	  thisout << newboard[i][j] << " " << (i+1) << " " << (j+1) << endl;
	  count++;
	}
      }
    }

    output << (newx.size() + newplus.size() + x.size() + plus.size()) << " " << count << endl;
    output << thisout.str();

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
    solvers[i].output << "Case #" << i << ": ";
    solvers[i].solve();
    //    solvers[i].output << "\n"; //Either of these should be removed.

    finished[i] = true;

    //Print
#pragma omp critical
    for (int j=printed+1; j<=T && finished[j]; j++) {
      cout << solvers[j].output.str();
      cout << std::flush;
      printed = j;
    }

  }

  return 0;
}
