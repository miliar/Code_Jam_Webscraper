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

#define k first
#define u second
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
const int MAXN = 1e3 + 5;

int N, D, T, test = 1, K[MAXN], U[MAXN];
pii A[MAXN];

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    printf("Case #%d: ", test++);
    scanf("%d %d", &D, &N);
    for(int i=1; i<=N; ++i) scanf("%d %d", &A[i].k, &A[i].u);
    sort(A + 1, A + N + 1);
    for(int i=1; i<=N; ++i) K[i] = A[i].k, U[i] = A[i].u;
    if(N == 1 || U[1] <= U[2]){
      double t = 1.0 * (D - K[1]) / U[1];
      printf("%.6f\n", D / t);
    }
    else{
      double tc = 1.0 * (K[2] - K[1]) / (U[1] - U[2]);
      double x = 1.0 * tc * U[1] + K[1];
      if(x > D){
        double t = 1.0 * (D - K[1]) / U[1];
        printf("%.6f\n", D / t);
      }
      else{
        double t = tc + 1.0 * (D - x) / U[2];
        printf("%.6f\n", D / t);
      }
    }
  }
  return 0;
}