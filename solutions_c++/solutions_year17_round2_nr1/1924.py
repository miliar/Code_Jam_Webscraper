#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <unordered_map>

#include <stdlib.h>     /* srand, rand */
#include <time.h>

#define FOR(i,a,b)               for(int i=(a);i<(b);i++)
#define REP(i, n)  FOR(i, 0, n)
#define VNAME(x) #x
#define MEMS(a, b) memset(a, b, sizeof(a))
#define SCS(t) scanf("%s",t)
#ifdef MAKEFILE_DEBUG
#define DEBUG 1
#else
#define DEBUG 0
#endif
#define pv(v) { if (DEBUG) {cout << #v << ": [ "; for (auto& e:v) { cout << e << " ";} cout << "]"<<endl;} }
#define pr(...) { if (DEBUG) {functionHelper0(#__VA_ARGS__, __VA_ARGS__); }}
#define sumV(v) { std::accumulate(v.begin(), v.end(), 0)}
#define V(type) vector< type >
#define VV(type) vector< V(type) >
#define PI 3.14159265358979323846
// base case for template recursion when one argument remains
template <typename Arg1>
void functionHelper0(const char* name, Arg1&& arg1) { std::cout << name << " = " << arg1 << std::endl; }

// recursive variadic template for multiple arguments
template <typename Arg1, typename... Args>
void functionHelper0(const char* names, Arg1&& arg1, Args&&... args) { const char* comma = strchr(names + 1, ','); std::cout.write(names, comma - names) << " = " << arg1; functionHelper0(comma, args...); }

// Read input
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
template <typename T> inline T readInt() { T n=0,s=1; char p=getchar(); if(p=='-') s=-1; while((p<'0'||p>'9')&&p!=EOF&&p!='-') p=getchar(); if(p=='-') s=-1,p=getchar(); while(p>='0'&&p<='9') { n = (n<< 3) + (n<< 1) + (p - '0'); p=getchar(); } return n*s; } 
#define RI readInt<int>()

template<typename Out>
void split(const std::string &s, char delim, Out result) { std::stringstream ss; ss.str(s); std::string item; while (std::getline(ss, item, delim)) { *(result++) = item; } }

std::vector<std::string> split(const std::string &s, char delim) { std::vector<std::string> elems; split(s, delim, std::back_inserter(elems)); return elems; }

using namespace std;


void ans() {
  int D = RI, N= RI;
  double r = -1;
  for (int i = 0; i < N; i++) {
    int K= RI, S = RI;
    double v = double(D) * S / (D - K);
    if (r == -1) r = v;
    else r = min(r, v);
  }
  printf("%.6f\n", r);

}

int main() {
    int T = RI;
    for (int i = 1; i <= T; i++) {
      cout << "Case #" << i << ": ";
      ans();
    }
    return 0;
}
