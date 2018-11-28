#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;

typedef pair<ll,int> plli;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 35

char A[MAXN][MAXN];
map<char,int> low_r;
map<char,int> high_r;
map<char,int> low_c;
map<char,int> high_c;
set<char> lets;
int R,C;

bool is_valid(char c, int low_i, int high_i, int low_j, int high_j) {
  if (low_i < 0 || low_i >= R) return false;
  if (high_i < 0 || high_i >= R) return false;
  if (low_j < 0 || low_j >= C) return false;
  if (high_j < 0 || high_j >= C) return false;

  FORALL(i,low_i,high_i)
    FORALL(j,low_j,high_j)
      if (A[i][j] != '?' && A[i][j] != c)
        return false;
  return true;
}

void apply_rect(char let) {
  FORALL(i,low_r[let],high_r[let])
    FORALL(j, low_c[let],high_c[let])
      A[i][j] = let;
}

int main() {
  int TEST;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    low_r.clear(); high_r.clear(); low_c.clear(); high_c.clear();
    lets.clear();
    memset(A,0,sizeof(A));

    scanf("%d%d",&R,&C);
    FOR(i,R) scanf("%s",&A[i][0]);

    FOR(i,R) FOR(j,C) {
      char v = A[i][j];
      if (v == '?') continue;
      if (!low_r.count(v) || i < low_r[v]) low_r[v] = i;
      if (!high_r.count(v) || i > high_r[v]) high_r[v] = i;
      if (!low_c.count(v) || j < low_c[v]) low_c[v] = j;
      if (!high_c.count(v) || j > high_c[v]) high_c[v] = j;
      lets.insert(v);
    }

    for (const auto & let : lets) {
      apply_rect(let);
    }

    FOR(i,R) FOR(j,C) {
      if (A[i][j] == '?') continue;
      apply_rect(A[i][j]);
    }

    while(true) {
      bool found_q = false;
      FOR(i,R) FOR(j,C) if (A[i][j] == '?') found_q = true;
      if (!found_q) break;

      bool did_something = false;

      FOR(i,R) FOR(j,C) {
        if (A[i][j] == '?') continue;
        char let = A[i][j];
        while(is_valid(let, low_r[let], high_r[let], low_c[let], high_c[let] + 1)) high_c[let]++, did_something = true;
        while(is_valid(let, low_r[let], high_r[let], low_c[let] - 1, high_c[let])) low_c[let]--, did_something = true;
        while(is_valid(let, low_r[let] - 1, high_r[let], low_c[let], high_c[let])) low_r[let]--, did_something = true;
        while(is_valid(let, low_r[let], high_r[let] + 1, low_c[let], high_c[let])) high_r[let]++, did_something = true;
        
        
        apply_rect(let);
      }

      assert(did_something);
    }

    printf("Case #%d:\n", test+1);
    FOR(i,R) printf("%s\n",&A[i][0]);
  }
}



















