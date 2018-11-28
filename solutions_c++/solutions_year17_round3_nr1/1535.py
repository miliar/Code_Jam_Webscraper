#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <functional>
#include <time.h>
#include <ctype.h>
#include <stack>
#include <bitset>
#include <iostream>

using namespace std;

#define r first
#define h second
#define mp make_pair
#define pb push_back
#define INF (2000000000)
#define LINF (1000000000000000000LL)
#define lowbit(x) (x&(-x))
#define gc getchar

inline int geti(){
  register int c = gc(), x = 0;
  for(; c<'0' || c>'9'; c=gc());
  for(; c>='0' && c<='9'; c=gc())
    x = (x<<1) + (x<<3) + c -'0';
  return x;
}

int dx[] = {1, -1, 0, 0, 1, 1, -1, -1}, dy[] = {0, 0, 1, -1, 1, -1, 1, -1};

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const ll MOD = 1000000007LL;
const double pi = acos(-1.0);
const int MAXN = 1e3 + 5;

int T, N, K, test = 1;
pdd A[MAXN];
double dp[MAXN][MAXN];

double sq(double x){ return x * x; }

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    memset(dp, 0, sizeof(dp));
    scanf("%d %d", &N, &K);
    for(int i=1; i<=N; ++i) scanf("%lf %lf", &A[i].r, &A[i].h);
    sort(A + 1, A + N + 1);
    reverse(A + 1, A + N + 1);
    for(int i=1; i<=N; ++i){
      dp[i][1] = max(pi * sq(A[i].r) + 2 * pi * A[i].r * A[i].h, dp[i - 1][1]);
      for(int k=2; k<=K; ++k){
        double cur = dp[i - 1][k - 1] + 2 * pi * A[i].r * A[i].h;
        dp[i][k] = max(dp[i - 1][k], cur);
      }
    }
    printf("Case #%d: %.9lf\n", test++, dp[N][K]);
  }
  return 0;
}