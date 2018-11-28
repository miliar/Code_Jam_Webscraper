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

int N, C, M;
int place[1001];

int solve(int F)
{
  //fprintf(stderr, "Test de %d trains\n", F);
  int dispo = 0;
  int res = 0;
  //REP(i, 1, N) fprintf(stderr, "Rangee %d : %d\n", i, place[i]);
  REP(i, 1, N)
  {
    dispo += F;
    // On place la rangée i
    if(place[i] > dispo) return -1;
    if(place[i] > F) res += place[i]-F;
    dispo -= place[i];
  }
  //fprintf(stderr, "OK\n");
  return res;
}


int main()
{
	int T, a, b;
	int number[1001];
	int mini;
	scanf("%d", &T);
	
	REP(t, 1, T)
	{
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d.\n", t);
		
		scanf("%d %d %d", &N, &C, &M);
		
		mini = 0;
		REP(i, 1, C) number[i] = 0;
		REP(i, 1, N) place[i] = 0;
		
		REP(i, 0, M-1)
		{
		  scanf("%d %d", &a, &b);
		  number[b]++;
		  place[a]++;
		}
		
		REP(i, 1, C) mini = max(mini, number[i]);
		int X = mini, Y = M, F; // Y possible, X-1 impossible
		while(X < Y)
		{
		  fprintf(stderr, "[%d %d]\n", X, Y);
		  F = (X+Y)/2;
		  if(solve(F) >= 0) // Ok
		  {
		    //fprintf(stderr, "Ca marche\n");
		    Y = F;
		  }
		  else
		  {
		    //fprintf(stderr, "Ca marche pas\n");
		    X = F+1;
		  }
		}
		printf("%d %d\n", X, solve(X));
	}

  return 0;
}
