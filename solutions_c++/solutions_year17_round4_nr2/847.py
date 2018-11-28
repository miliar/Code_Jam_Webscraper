#include"stdio.h"
#include"stdlib.h"
#include"math.h"
#include"string.h"
#include"set"
#include"map"
#include"queue"
#include"algorithm"
#define fi first
#define se second
#define IT iterator
#define INF 1000000007
#define INFL 4000000000000000007LL
#define MOD 1000000007LL
double const EPS = 1e-9;
double const PI  = acos(-1);
double const EXP = exp(1);
using namespace std;
typedef long long 		LL;
typedef pair<int, int>	II;
typedef vector<II>		VII;
typedef vector<int>		VI;
typedef set<int>		SI;
typedef vector<double> VD;
typedef vector<VD> VVD;
int Test_Cases, N, C, M, P, B;


double MinCostMatching(const VVD &cost, VI &Lmate, VI &Rmate) {
  int n = int(cost.size());

  // construct dual feasible solution
  VD u(n);
  VD v(n);
  for (int i = 0; i < n; i++) {
    u[i] = cost[i][0];
    for (int j = 1; j < n; j++) u[i] = min(u[i], cost[i][j]);
  }
  for (int j = 0; j < n; j++) {
    v[j] = cost[0][j] - u[0];
    for (int i = 1; i < n; i++) v[j] = min(v[j], cost[i][j] - u[i]);
  }
  
  // construct primal solution satisfying complementary slackness
  Lmate = VI(n, -1);
  Rmate = VI(n, -1);
  int mated = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (Rmate[j] != -1) continue;
      if (fabs(cost[i][j] - u[i] - v[j]) < 1e-10) {
	Lmate[i] = j;
	Rmate[j] = i;
	mated++;
	break;
      }
    }
  }
  
  VD dist(n);
  VI dad(n);
  VI seen(n);
  
  // repeat until primal solution is feasible
  while (mated < n) {
    
    // find an unmatched left node
    int s = 0;
    while (Lmate[s] != -1) s++;
    
    // initialize Dijkstra
    fill(dad.begin(), dad.end(), -1);
    fill(seen.begin(), seen.end(), 0);
    for (int k = 0; k < n; k++) 
      dist[k] = cost[s][k] - u[s] - v[k];
    
    int j = 0;
    while (true) {
      
      // find closest
      j = -1;
      for (int k = 0; k < n; k++) {
	if (seen[k]) continue;
	if (j == -1 || dist[k] < dist[j]) j = k;
      }
      seen[j] = 1;
      
      // termination condition
      if (Rmate[j] == -1) break;
      
      // relax neighbors
      const int i = Rmate[j];
      for (int k = 0; k < n; k++) {
	if (seen[k]) continue;
	const double new_dist = dist[j] + cost[i][k] - u[i] - v[k];
	if (dist[k] > new_dist) {
	  dist[k] = new_dist;
	  dad[k] = j;
	}
      }
    }
    
    // update dual variables
    for (int k = 0; k < n; k++) {
      if (k == j || !seen[k]) continue;
      const int i = Rmate[k];
      v[k] += dist[k] - dist[j];
      u[i] -= dist[k] - dist[j];
    }
    u[s] += dist[j];
    
    // augment along path
    while (dad[j] >= 0) {
      const int d = dad[j];
      Rmate[j] = Rmate[d];
      Lmate[Rmate[j]] = j;
      j = d;
    }
    Rmate[j] = s;
    Lmate[s] = j;
    
    mated++;
  }
  
  double value = 0;
  for (int i = 0; i < n; i++)
    value += cost[i][Lmate[i]];
  
  return value;
}
int CL[1005], CR[1005];
int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.txt", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.txt", "w", stdout);
	scanf("%d", &Test_Cases);
	for (int test = 1; test <= Test_Cases; test++) {
		scanf("%d%d%d", &N, &C, &M);
		VI PosL, PosR;
		for (int i = 0; i < M; i++) {
			scanf("%d%d", &P, &B);
			//if (test == 63) printf("%d %d\n", P, B);
			if (B == 1) PosL.push_back(P);
			else PosR.push_back(P);
		}
		/*if (test != 63) continue;
		int NL = PosL.size(), NR = PosR.size();
		int L1 = 0, R1 = 0;
		for (int i = 0; i < NL; i++) CL[PosL[i]]++;
		for (int i = 0; i < NR; i++) CR[PosR[i]]++;
		printf("[L] %d, ", NL);
		for (int i = 1; i <= 1000; i++) if (CL[i] > 0) printf("(%d,%d) ", i, CL[i]); printf("\n");
		printf("[R] %d, ", NR);
		for (int i = 1; i <= 1000; i++) if (CR[i] > 0) printf("(%d,%d) ", i, CR[i]); printf("\n");*/
		while (PosL.size() < PosR.size())
			PosL.push_back(0);
		while (PosL.size() > PosR.size())
			PosR.push_back(0);
			
		VVD cost;
		for (int i = 0; i < PosL.size(); i++) {
			VD cost_i;
			for (int j = 0; j < PosR.size(); j++) {
				if (PosL[i] == 0 || PosR[j] == 0)
					cost_i.push_back(1000);
				else if (PosL[i] == PosR[j])
					if (PosL[i] == 1)
						cost_i.push_back(1000);
					else
						cost_i.push_back(1);
				else 
					cost_i.push_back(0);
			}
			cost.push_back(cost_i);
		}
		VI Lmate, Rmate;
		int change = (int)MinCostMatching(cost, Lmate, Rmate);
		int ans = Lmate.size();
		for (int i = 0; i < Lmate.size(); i++) {
			int j = Lmate[i];
			if (PosL[i] == 0 || PosR[j] == 0)
				change -= 1000;
			else if (PosL[i] == 1 && PosR[j] == 1)
				change -= 1000, ans++;
		}
		printf("Case #%d: %d %d\n", test, ans, change);
	}
}
