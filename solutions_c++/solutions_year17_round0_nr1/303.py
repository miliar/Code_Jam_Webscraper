#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 1005

char str[MAXN];
int x[MAXN];
int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int cs;
  cin >> cs;
  REP(csn, 1, cs + 1) {
    printf("Case #%d: ", csn);
    int k;
    scanf("%s%d", str, &k);
    int n = strlen(str);
    REP(i,0,n) x[i] = str[i] == '+';
    int ans = 0;
    REP(i,0,n-k+1) {
      if (!x[i]) {
        ans++;
        REP(j,i,i+k) x[j] = !x[j];
      }
    }
    REP(i,0,n) if (!x[i]) ans = -1;
    if (ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
  return 0;
}
