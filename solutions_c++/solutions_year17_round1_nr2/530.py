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
typedef pair<llong,llong> pairll;

#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))
#define memclear(ar) memset((ar), 0, sizeof(ar))
#define pb push_back

const int MAXN=55;
int n,m;
vector<vector<pairll>> ig;
llong ar[MAXN];
int idx[MAXN];

bool comp(const pairll& a, const pairll& b) {
  if (a.first == b.first) return a.second < b.second;
  return a.first < b.first;
}

int good(const pairll& a, const pairll& b) {
  if (a.second < b.first) return 1;
  else if (b.second < a.first) return -1;
  return 0;
}

bool check(const pairll& a) {
  return a.first <= a.second && a.first > 0 && a.second > 0;
}

bool finished() {
  FORZ(i,n) if (idx[i]>=m) return true;
  return false;
}

void solve() {
  cin>>n>>m;
  ig.clear();
  ig.resize(n);
  FORZ(i,n) scanf("%lld",ar+i);
  FORZ(i,n) {
    ig[i].resize(m);
    FORZ(j,m) {
      double x;
      scanf("%lf",&x);
      double xa=(x/(double)ar[i])/0.9, xb=(x/(double)ar[i])/1.1;
      ig[i][j]=pairll(ceil(xb),floor(xa));
    }
    sort(ig[i].begin(), ig[i].end(), comp);
  }
  int res=0;
  FORZ(i,n) idx[i]=0;
  while (!finished()) {
    bool bumped=false;
    FORZ(i,n) {
      if (!check(ig[i][idx[i]])) {
        idx[i]++;
        bumped=true;
      }
    }
    if (bumped) continue;
    llong mx=0;
    FORZ(i,n) {
      if (mx<ig[i][idx[i]].first) mx=ig[i][idx[i]].first;
    }
    pairll curr=ig[0][idx[0]];
    bool valid=true;
    FOR(i,1,n) {
      llong ff=max(curr.first, ig[i][idx[i]].first);
      llong ss=min(curr.second, ig[i][idx[i]].second);
      if (ff>ss) {
        valid=false;
        break;
      }
      curr=pairll(ff,ss);
    }
    if (valid) {
      FORZ(i,n) idx[i]++;
      res++;
    } else {
      FORZ(i,n) {
        if (ig[i][idx[i]].second<mx) idx[i]++;
      }
    }
  }
  printf("%d\n",res);
}

int main() {
#ifdef DEBUG
  freopen("../CodeforcesC/in.txt", "r", stdin);
  freopen("../CodeforcesC/out.txt", "w", stdout);
#endif

  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}
