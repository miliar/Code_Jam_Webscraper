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

#define MAXN 1005

char S[MAXN];
int K;

char flip(char c) {
  if (c == '-') return '+';
  if (c == '+') return '-';
  assert(false);
}

void apply(char * s, int len) {
  FOR(i,len) {
    assert(s[i]);
    s[i] = flip(s[i]);
  }
}

int main() {
  int TEST;

  scanf("%d",&TEST);
  FOR(test,TEST) {
    scanf("%s%d",&S[0],&K);
    int N = strlen(S);
    assert(K <= N);

    int ans = 0;
    for (int i = 0; i < N - K + 1; ++i) {
      if (S[i] == '-') {
        apply(S+i, K);
        ans++;
      }
    }

    bool good = true;
    FOR(i,N) if (S[i] != '+') good = false;
    printf("Case #%d: ", test+1);
    if (good) printf("%d\n", ans);
    else printf("IMPOSSIBLE\n");
  }
}






