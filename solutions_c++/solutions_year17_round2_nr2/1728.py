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
#include <unordered_set>

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

V(int) colorC(6);
V(char) colorMap = {'R', 'O', 'Y', 'G', 'B', 'V'};
V(V(int)) adj = { {2,3,4}, {4}, {0, 4, 5}, {0}, {0,1,2}, {2} };
int starti;
int N;
string path;
unordered_set<int> rr = {0, 1, 5}, bb = {3,4,5}, yy = {1,2,3};

int key() {
  int r = 0;
  for (auto& e: colorC) {
    r = r * 1001 + e;
  }
  return r;
}

bool rec(int i, int color, vector<unordered_set<int>>& mm) {
  pr(i, path);
  pv(colorC)
  if (i == N) {
    pr(i, color, starti);
    for (auto& ad: adj[color]) {
      if (ad == starti) {
        return true;
      }
    }
    return false;
  }
  int k = key();
  if (mm[i].count(k)) return false;
  bool r = false;
  for (auto& ad: adj[color]) {
    if (colorC[ad] == 0) continue;
    colorC[ad]--;
    path.push_back(colorMap[ad]);
    if (rec(i + 1, ad, mm)) {
      return true;
    }
    colorC[ad]++;
    path.pop_back();
  }
  mm[i].insert(k);
  return false;
}

void NP() {
  cout << "IMPOSSIBLE" << endl;
}

bool check(V(int)& r, int i ) {
  for (auto j: V(int){i-1, i+1}) {
    if (j < 0) j = r.size() - 1;
    if (j == r.size()) j = 0;
    if (r[j] == r[i]) return false;
  }
  return true;
}

void ans() {
  int N = RI;
  unordered_map<char, int> cm;
  int rc = 0, bc = 0, yc = 0;
  for (int i = 0; i < 6; i++) {
    colorC[i] = RI;
    if (rr.count(i)) rc+= colorC[i];
    if (bb.count(i)) bc+= colorC[i];
    if (yy.count(i)) yc+= colorC[i];
  }
  pr(rc, bc, yc);
  vector<pair<int, int>> all = { {rc, 0}, {bc, 4}, {yc, 2}};
  sort(all.begin(), all.end());
  pr(all[0].first);
  V(int) r(N, -1);
  int i = 0, k = 2;
  int count = 0;
  pr(i, k, count);
  while (true) {
    if (i >= N) { i = 1;}
    int color = all[k].second;
    pr(k, color);
    if (colorC[color] > 0) {
      r[i] = color;
      colorC[color]--;
      i += 2;
      count++;
      if (count == N) break;
    } else {
      k--;
    }
  }

  pv(r);
  string path;
  for (int i = 0; i < N; i++) {
    if (!check(r, i)) {
      NP();
      return;
    }
    path.push_back(colorMap[r[i]]);
  }
  cout << path << endl;

}


void ans2() {
  N = RI;
  for (int i = 0; i < 6; i++) {
    colorC[i] = RI;
    if (colorC[i] > 0) {
      starti = i;
    }
  }
  vector<unordered_set<int>> mm(N);
  path.clear();
  pr(N);
  pv(colorC);
  pr(starti);
  path.push_back(colorMap[starti]);
  colorC[starti]--;
  bool r = rec(1, starti, mm);
  if (!r) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << path << endl;
  }

}


int main() {
    int T = RI;
    for (int i = 1; i <= T; i++) {
      cout << "Case #" << i << ": ";
      ans();
    }
    return 0;
}
