#include <vector>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
#include <cassert>
using namespace std;

typedef long long llong;
typedef pair<int,int> pairii;
typedef pair<llong,llong> pairll;

#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))
#define memclear(ar) memset((ar), 0, sizeof(ar))
#define pb push_back

int r,c;
vector<string> st;

bool check() {
  FORZ(i,r) FORZ(j,c) if (st[i][j]=='?') return false;
  return true;
}

bool checkrow(int i) {
  FORZ(j,c) if (st[i][j]=='?') return false;
  return true;
}

bool badrow(int i) {
  FORZ(j,c) if (st[i][j]!='?') return false;
  return true;
}

void solve() {
  cin>>r>>c;
  st.clear();
  st.resize(r);
  FORZ(i,r) cin>>st[i];
  while (!check()) {
    FORZ(i,r) {
      if (badrow(i)) {
        if (i>0) {
          FORZ(j,c) {
            st[i][j]=st[i-1][j];
          }
        }
      }
      if (badrow(i)) {
        if (i<r-1) {
          FORZ(j,c) {
            st[i][j]=st[i+1][j];
          }
        }
      }
      if (!checkrow(i)) {
        FORZ(j,c) {
          if (st[i][j]!='?') {
            for(int k=j-1; k>=0; k--) {
              if (st[i][k]=='?') st[i][k]=st[i][j];
              else break;
            }
            for (int k=j+1; k<c; k++) {
              if (st[i][k]=='?') st[i][k]=st[i][j];
              else break;
            }
          }
        }
      }
    }
  }
  FORZ(i,r) cout<<st[i]<<"\n";
}

int main() {
#ifdef DEBUG
  freopen("../CodeforcesA/in.txt", "r", stdin);
  freopen("../CodeforcesA/out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d:\n", i);
    solve();
  }
  
  return 0;
}
