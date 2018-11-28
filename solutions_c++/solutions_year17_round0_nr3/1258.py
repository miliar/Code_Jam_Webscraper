#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;
int64_t N, K;

void solve() {
  cin >> N >> K;
  int64_t x, y;
  int64_t val[2];
  int64_t cnt[2];
  int len = 1;
  val[0] = N;
  cnt[0] = 1;
  bool solved = false;
  while (!solved) {
    int64_t covered = 0;
    // for (int i = 0; i < len; ++i) {
    //   printf("[%lldx %lld] ", cnt[i], val[i]);
    // }
    // printf("\n");
    for (int i = 0; !solved && i < len; ++i) {
      K -= cnt[i];
      if (K <= 0) {
        x = (val[i] - 1)/2;
        y = val[i] - x - 1;
        solved = true;
      }
    }
    if (solved) break;
    vector<pair<int64_t,int64_t> > nextval;
    for (int i = 0; i < len; ++i) {
      int64_t u = (val[i]-1)/2;
      int64_t v = val[i]-1 - u;
      if (u != 0) {
        nextval.push_back(make_pair(u, cnt[i]));
      }
      if (v != 0) {
        nextval.push_back(make_pair(v, cnt[i]));
      }
    }
    sort(nextval.begin(), nextval.end());
    reverse(nextval.begin(), nextval.end());
    len = 0;
    for (int i = 0; i < nextval.size(); ++i) {
      if (len == 0 || nextval[i].first != nextval[i-1].first) {
        val[len] = nextval[i].first;
        cnt[len] = nextval[i].second;
        ++len;
      } else {
        cnt[len-1] += nextval[i].second;
      }
    }
  }
  printf(" %lld %lld", y, x);
}

int main(){
  int T;
  scanf("%d",&T);
  for (int TC=1;TC<=T;++TC) {
    printf("Case #%d:", TC);
    solve();
    printf("\n");
  }
  return 0;
}