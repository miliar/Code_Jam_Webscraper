#include<cstring>
#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int n, p;
int cache[101][101][101][101][4];

int go(vector<int> cnt, int total, int leftover) {
  if(total == 0) return 0;
  int& ret = cache[cnt[0]][cnt[1]][cnt[2]][cnt[3]][leftover];
  if(ret != -1) return ret;
  ret = 0;
  for(int g = 0; g < 4; ++g) {
    if(cnt[g]) {
      cnt[g]--;
      int cand = (leftover == 0 ? 1 : 0) + go(cnt, total-1, (leftover + g) % p);
      ret = max(ret, cand);
      cnt[g]++;
    }
  }
  return ret;
}

int main() {
  int cases;
  cin >> cases;
  for(int cc = 0; cc < cases; ++cc) {
    memset(cache, -1, sizeof cache);
    cin >> n >> p;
    vector<int> cnt(4);
    for(int i = 0; i < n; ++i) {
      int members;
      cin >> members;
      cnt[members%p]++;
    }
    printf("Case #%d: %d\n", cc+1, go(cnt, n, 0));
  }
}
