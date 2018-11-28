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

#define MAXN 105
int dp[MAXN][MAXN][MAXN][MAXN];

int main() {
  int TEST,N,P,x;
  scanf("%d",&TEST);

  FOR(test,TEST) {
    memset(dp,-1,sizeof(dp));
    int cnt[4] = {0,0,0,0};
    scanf("%d%d",&N,&P);
    FOR(i,N) {
      scanf("%d",&x);
      cnt[x%P]++;
    }

    FORALL(a,0,cnt[0]) FORALL(b,0,cnt[1]) FORALL(c,0,cnt[2]) FORALL(d,0,cnt[3]) {
      dp[a][b][c][d] = 0;
      int a_used = cnt[0]-a;
      int b_used = cnt[1]-b;
      int c_used = cnt[2]-c;
      int d_used = cnt[3]-d;

      int used = (0*a_used + 1*b_used + 2*c_used + 3*d_used);
      int opened = ((used + P - 1) / P) * P;
      int cur_state = opened - used;
      int add_here = (cur_state == 0);
      if (a) dp[a][b][c][d] = max(dp[a][b][c][d], dp[a-1][b][c][d] + add_here);
      if (b) dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b-1][c][d] + add_here);
      if (c) dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b][c-1][d] + add_here);
      if (d) dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b][c][d-1] + add_here);

      //printf("dp(%d,%d,%d,%d; %d) = %d\n",a,b,c,d,cur_state,dp[a][b][c][d]);
    }

    printf("Case #%d: %d\n", test+1, dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]]);
  }
}



















