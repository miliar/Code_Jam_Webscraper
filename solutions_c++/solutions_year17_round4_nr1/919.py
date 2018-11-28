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

const int MAXN=105;
int ar[MAXN],n,p,cnt[5];

void solve() {
  scanf("%d%d",&n,&p);
  FORZ(i,n) scanf("%d",ar+i);
  int res=0;
  memclear(cnt);
  FORZ(i,n) {
    ar[i]%=p;
    cnt[ar[i]]++;
  }
  if (p==2) {
    res=cnt[0]+ceil(cnt[1]/2.0);
  } else if (p==3) {
    int pr=min(cnt[1],cnt[2]);
    int rem=max(cnt[1]-pr, cnt[2]-pr);
    res=cnt[0]+pr+ceil(rem/3.0);
  } else {
    int pr2=cnt[2]/2;
    int pr13=min(cnt[1],cnt[3]);
    int c2=cnt[2]%2, c13=max(cnt[1]-pr13, cnt[3]-pr13);
    res=cnt[0]+pr2+pr13;
    if (c2==1 && c13>=2) {
      c13-=2;
      res += 1+ceil(c13/4.0);
    } else if (c2==0) {
      res += ceil(c13/4.0);
    } else {
      res++;
    }
  }
  printf("%d\n",res);
}

int main() {
#ifdef DEBUG
  freopen("../CodeforcesA/in.txt", "r", stdin);
  freopen("../CodeforcesA/out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
