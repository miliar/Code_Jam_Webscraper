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

void solve() {
  string s;
  cin >> s;
  int n,m;
  cin >> m;
  n = (int)s.length();
  int res=0;
  FORZ(i,n-m+1) {
    if (s[i]=='-') {
      FOR(j,i,m+i) {
        if (s[j]=='-') s[j]='+';
        else s[j]='-';
      }
      res++;
    }
    if (s[n-i-1]=='-') {
      for (int j=n-i-1; j>=n-i-m ;j--) {
        if (s[j]=='-') s[j]='+';
        else s[j]='-';
      }
      res++;
    }
  }
  bool good=true;
  FORZ(i,n) {
    if (s[i]=='-') {
      good=false;
      break;
    }
  }
  if (good) printf("%d\n",res);
  else printf("IMPOSSIBLE\n");
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
