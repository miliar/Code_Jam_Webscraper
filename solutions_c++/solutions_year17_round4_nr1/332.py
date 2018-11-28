#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

int memo[105][105][105][4];

int dp(int n1, int n2, int n3, int comb)
{
  if(memo[n1][n2][n3][comb] >= 0) return memo[n1][n2][n3][comb];
  int best = 0, poss;
  if(n1 + n2 + n3 == 0) return 0;
  if(n1 > 0)
  {
    poss = 0;
    if(comb == 0) poss++;
    poss += dp(n1-1, n2, n3, (comb+1)%4);
    best = max(best, poss);
  }
  if(n2 > 0)
  {
    poss = 0;
    if(comb == 0) poss++;
    poss += dp(n1, n2-1, n3, (comb+2)%4);
    best = max(best, poss);
  }
  if(n3 > 0)
  {
    poss = 0;
    if(comb == 0) poss++;
    poss += dp(n1, n2, n3-1, (comb+3)%4);
    best = max(best, poss);
  }
  return memo[n1][n2][n3][comb] = best;
}

int main()
{
	int T, N, P;
	int g[105];
	scanf("%d", &T);
	
	REP(t, 1, T)
	{
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d.\n", t);
		
		scanf("%d %d", &N, &P);
		
		REP(i, 0, N-1) scanf("%d", &g[i]);
		
		if(P == 2)
		{
		  int even = 0, odd = 0;
		  REP(i, 0, N-1)
		  {
		    if(g[i] % 2 == 0) even++;
		    else odd++;
		  }
		  printf("%d\n", even + (odd+1)/2);
		}
		else if(P == 3)
		{
		  int combien[3];
		  combien[0] = 0;
		  combien[1] = 0;
		  combien[2] = 0;
		  REP(i, 0, N-1) combien[g[i]%3]++;
		  int rep = 0;
		  rep += combien[0];
		  
		  int mini = min(combien[1], combien[2]);
		  rep += mini;
		  int rest = max(combien[1], combien[2])-mini;
		  rep += (rest+2)/3;
		  printf("%d\n", rep);
		  /*
		  REP(i, 0, 101) REP(j, 0, 101) REP(l, 0, 3) memo3[i][j][l] = -1;
		  rep += dp3(combien[1], combien[2], 0);
		  printf("%d\n", rep);
		  */
		}
		else if(P == 4)
		{
		  int combien[4];
		  combien[0] = 0;
		  combien[1] = 0;
		  combien[2] = 0;
		  combien[3] = 0;
		  REP(i, 0, N-1) combien[g[i]%4]++;
		  int rep = 0;
		  rep += combien[0];
		  REP(i, 0, 101) REP(j, 0, 101) REP(k, 0, 101) REP(l, 0, 3) memo[i][j][k][l] = -1;
		  rep += dp(combien[1], combien[2], combien[3], 0);
		  printf("%d\n", rep);
		}
		
	}

  return 0;
}
