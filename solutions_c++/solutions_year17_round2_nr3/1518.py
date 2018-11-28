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

#define x first
#define y second
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

template <class T>
  inline T sq(T x){ return x * x; }

int dx[] = {1, -1, 0, 0, 1, 1, -1, -1}, dy[] = {0, 0, 1, -1, 1, -1, 1, -1};

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const ll MOD = 1000000007LL;
const double pi = acos(-1.0);
const int MAXN = 1e2 + 5;

int T, N, Q, test = 1;
double dp[MAXN], pre[MAXN], S[MAXN], D[MAXN][MAXN], E[MAXN];


int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &N, &Q);
    for(int i=1; i<=N; ++i) scanf("%lf %lf", &E[i], &S[i]);
    for(int i=1; i<=N; ++i)
      for(int j=1; j<=N; ++j){
        scanf("%lf", &D[i][j]);
        if(i + 1 == j) pre[j] = D[i][j] + pre[i];
      }
    dp[1] = 0;
    for(int i=2; i<=N; ++i){
      double res = LINF * 1.0;
      for(int j=1; j<i; ++j){
        double dist = pre[i] - pre[j];
        if(E[j] < dist) continue;
        res = min(res, dp[j] + dist / S[j]);
      }
      dp[i] = res;
    }
    scanf("%d %d", &E[1], &E[2]);
    printf("Case #%d: %.6f\n", test++, dp[N]);
  }
  return 0;
}