/*
Verdict:
Algorithm:
*/

// Includes
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
using namespace std;

// #define DEBUG  //----------------------------------Comment Before Submitting!

// Debug Macros
#ifdef DEBUG
#define D(x) do { cerr << #x << ": " << x << '\n'; } while (0)
#define DD(x) do { cerr << x << '\n'; } while (0)
#define PROF(s) cerr << "Time so far: " << ((float)(s) - (float)(begin))/CLOCKS_PER_SEC << '\n'
#define PROF2(f,s) cerr << "Time so far: " << ((float)(s) - (float)(f))/CLOCKS_PER_SEC << '\n'
#else
#define D(x)
#define DD(x)
#define PROF(s)
#define PROF2(f,s)
#endif

// Debug Functions
template<typename K, typename V>
void cerr_map(map<K, V> m) {
#ifdef DEBUG
  for (auto it = m.begin(); it != m.end(); it++) {
    cerr << it->first << " -> " << it->second << endl;
  }
#endif
}


// Input Macros
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)

// Typedefs
typedef long long ll;
typedef unsigned long long ull;
typedef vector<pair<int, int>> VII;
typedef pair<int, int> PII;

// Global Constants
constexpr int INF = ~(1 << 31);
constexpr int NINF = 1 << 31;
//---------------------------------------------------------------------


int main() {
#ifdef DEBUG
  clock_t begin = clock();
#endif

  int T;
  SCD(T);
  for (int _t = 1; _t <= T; _t++) {
    int N, K;
    SCD(N);
    SCD(K);
    set<int> ostalls;
    ostalls.insert(0);
    ostalls.insert(N + 1);
    pair<int, int> answer;
    for (int k = 0; k < K; k++) {
      int mind = NINF;
      int maxd = NINF;
      int pos_insertion = -1;
      for (auto it = ostalls.begin(); it != ostalls.end(); it++) {
        if (next(it, 1) == ostalls.end()) break;
        int left = *it;
        int right = *next(it, 1);
        int pos = left + (right - left)/2;
        int LS = pos - left;
        int RS = right - pos;
        if (min(LS, RS) > mind) {
          mind = min(LS, RS);
          maxd = max(LS, RS);
          pos_insertion = pos;
        } else if (min(LS,RS) == mind && max(LS,RS) > maxd) {
          maxd = max(LS, RS);
          pos_insertion = pos;
        }
      }
      ostalls.insert(pos_insertion);
      if (k == K - 1) {
        answer.first = mind;
        answer.second = maxd;
      }
    }
    cout << "Case #" << _t << ": " << answer.second - 1 << " " << answer.first - 1 << "\n";
  }


  return 0;
}









































