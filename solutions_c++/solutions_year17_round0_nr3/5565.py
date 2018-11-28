#include <bits/stdc++.h>
using namespace std;

long long value[1000];
int nxt[1000];
int curm = 0;

void print() {
  int cur = 0;
  while(cur != -1) {
    printf("%lld ", value[cur]);
    cur = nxt[cur];
  }
  puts("");
}

void split() {
  int mp = -1;
  long long ma = 0;
  int cur = 0;
  while(cur != -1) {
    if(value[cur] == 0) {
      cur = nxt[cur];
      continue;
    }
    if(value[cur] > ma) {
      ma = value[cur];
      mp = cur;
    }
    cur = nxt[cur];
  }
  long long l = (ma - 1) / 2, r = ma - l - 1;
  int node = curm++;
  value[mp] = l;
  value[node] = r;
  nxt[node] = nxt[mp];
  nxt[mp] = node;
  // print();
}

int main() {
  freopen("c0.in", "r", stdin);
  freopen("c0.out", "w", stdout);
  int kase;
  cin >> kase;
  for(int k = 0; k < kase; k++) {
    curm = 0;
    memset(nxt, -1, sizeof(nxt));
    long long N;
    int T;
    cin >> N >> T;
    value[curm++] = N;
    for(int j = 0; j < T - 1; j++) {
      split();
    }
    long long ma = 0;
    int cur = 0;
    while(cur != -1) {
      if(value[cur] == 0) {
        cur = nxt[cur];
        continue;
      }
      ma = max(ma, value[cur]);
      cur = nxt[cur];
    }
    printf("Case #%d: %lld %lld\n", k + 1, ma / 2, (ma - 1) / 2);
  }
  return 0;
}
