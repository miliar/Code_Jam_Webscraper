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

int ar[20];

void solve() {
  string s;
  cin>>s;
  int n=(int)s.length();
  for (int i=n-1; i>=1; i--) {
    if (s[i]<s[i-1]) {
      s[i]='9';
      s[i-1]--;
      FOR(j,i+1,n) s[j]='9';
    }
  }
  bool start=true;
  FORZ(i,n) {
    if (start&&s[i]=='0') continue;
    printf("%c",s[i]);
    start=false;
  }
  printf("\n");
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
