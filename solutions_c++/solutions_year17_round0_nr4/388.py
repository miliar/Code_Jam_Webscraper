#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <climits>
#include <assert.h>

using namespace std;


typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> int2;
typedef pair<float, float> float2;
typedef pair<ull, ull> ull2;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define del(s,x) do {__typeof((s).begin()) abcde=(s).find(x); if(abcde !=(s).end()) s.erase(abcde); } while(0);
#define del2(s,x) do {__typeof((s).begin()) abcde=find(all(s),x); if(abcde !=(s).end()) s.erase(abcde); } while(0);

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

#define add(iz,jz) do { G[iz].pb(jz); G[jz].pb(iz); W[iz].pb(1); W[jz].pb(0); } while(0);

#define BIG (1000000000) /* TODO: bien choisir !*/

int edmonds_karp_sparse(vector<vector<int> > &G, vector<vector<int> > &W, vector<vector<int> > &F, int s, int t, int maxflow) {
  int n = G.size();
  int u;

  /* Breadth-first search to find a shortest path from s to t */
  /* pred[v] is the predecessor of i in the shortest path from s to v */
  /* minpath[v] is the smallest edge weight on the shortest path from s to v */
  for(;;) {
    queue<int> q;
    vector<int> pred(n, -1);
    vector<int> minpath(n, BIG);
    q.push(s);
    pred[s] = -2;
    while(q.size() > 0 && pred[t] == -1) {
      u = q.front();
      q.pop();
      FOR(i,0,G[u].size()) {
	int v = G[u][i];
	if(W[u][i] > 0 && pred[v] == -1) {
	  pred[v] = u;
	  minpath[v] = min (minpath[u], W[u][i]);
	  q.push(v);
	}
      }
    }
    if(pred[t] == -1) break; /* If no path from s to t */
    maxflow += minpath[t];
    
    /* Update residual graph and flow
       along the path from s to t in F */
    for(int k = t; pred[k] != -2; k = pred[k]) {
      assert (pred[k] != -1);
      int i;
      for (i = 0; i < G[pred[k]].size(); i ++) 
	if (G[pred[k]][i] == k)
	  break;
      assert (i != G[pred[k]].size());
      F[pred[k]][i] += minpath[t];
      W[pred[k]][i] -= minpath[t];
      for (i = 0; i < G[k].size(); i ++) 
	if (G[k][i] == pred[k])
	  break;
      assert (i != G[k].size());
      assert (pred[k] >= 0 && pred[k] < n);
	
      F[k][i] -= minpath[t];
      W[k][i] += minpath[t];
    }
    if (maxflow >= BIG) break; /* max flow cannot be more than infinite */
  }
  return maxflow;
}

#define idxLineCol(i, j) (1 + (j))
#define idxDiag12(i, j) (((i) + (j) < (n)) ? (1 + (i)) : ((n) - (j)))
#define idxSourceLine(i) (i)
#define idxSourceDiag1(i, j) ((n) + (i) + (j))
#define idxColSink(j) 0
#define idxDiag2Sink(i,j) 0

int main() {
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    // Get the input
    int n, m;
    cin >> n >> m;
    char c; int ii, jj;
    vector<string> init(n, string(n,'.'));
    FOR(i,0,m) {
      cin >> c >> ii >> jj;
      init[ii - 1][jj - 1] = c;
    }
    /*cout << "Initial grid: " << endl;
    FOR(i,0,n) cout << init[i] << endl;
    cout << endl;*/

    // Build the graph on which flow algorithm will be applied
    int nbLine = n;
    int nbDiag = 2*n - 1;
    int nbV = 2 + 2*nbLine + 2*nbDiag;
    vector<vector<int> > G(nbV, vector<int>(0));
    vector<vector<int> > W(nbV, vector<int>(0));
    int s = nbV - 2;
    int t = nbV - 1;

    FOR(i,0,n) add(s, i); /* Link source to each "line" vertex */
    FOR(i,0,n) add(n + i, t); /* Link each "column" vertex to the sink */
    FOR(i,0,n) FOR(j,0,n) add(i, n + j); /* Link "line" and "column" vertices together */

    int baseDiag1 = 2*nbLine; /* Index of first diag1 vertex */
    int baseDiag2 = 2*nbLine + nbDiag; /* Index of first diag2 vertex */
    FOR(i,0,nbDiag) add(s, baseDiag1 + i); /* Link source to each "diag1" vertex */
    FOR(i,0,nbDiag) add(baseDiag2 + i, t); /* Link each "diag2" vertex to the sink */
    FOR(i,0,n) FOR(j,0,n) add(baseDiag1 + i + j, baseDiag2 + n - 1 + i - j); /* Link "diag1" and "diag2" vertices together */

    // Take initial grid into account: compute corresponding flow graph and residual graph
    int stylePoints = 0;
    vector<vector<int> > F(nbV, vector<int> (0));
    FOR(i,0,nbV) F[i] = vector<int> (G[i].size(), 0);
    FOR(i,0,n) FOR(j,0,n) {
      if ((init[i][j] == 'x') || (init[i][j] == 'o')) { // do the matching btwn corresponding line & col
	F[s][idxSourceLine(i)] = 1; F[i][idxLineCol(i,j)] = 1; F[n + j][idxColSink(j)] = 1; 
	W[s][idxSourceLine(i)] = 0; W[i][idxLineCol(i,j)] = 0; W[n + j][idxColSink(j)] = 0;
	stylePoints ++;
      }
      if ((init[i][j] == '+') || (init[i][j] == 'o')) { // do the matching between corresponding two diagonals
	F[s][idxSourceDiag1(i,j)] = 1; F[baseDiag1 + i + j][idxDiag12(i,j)] = 1; F[baseDiag2 + n - 1 + i - j][idxDiag2Sink(i,j)] = 1;
	W[s][idxSourceDiag1(i,j)] = 0; W[baseDiag1 + i + j][idxDiag12(i,j)] = 0; W[baseDiag2 + n - 1 + i - j][idxDiag2Sink(i,j)] = 0;
	stylePoints ++;
      }
    }

    /*cout << "Graph: " << endl;
    FOR(i,0,nbV) {
      cout << i << ": ";
      FOR(j,0,G[i].size()) cout << G[i][j] << " (" << W[i][j] << "), ";
      cout << endl;
      }*/

    // Find optimal with flow algorithm
    stylePoints = edmonds_karp_sparse(G, W, F, s, t, stylePoints);

    // Build final grid
    vector<string> sol(n, string(n,'.'));
    FOR(i,0,n) FOR(j,0,n) if (F[i][1+j] == 1) sol[i][j] = 'x';
    FOR(id,0,nbDiag) FOR(jd,0,F[baseDiag1 + id].size()-1) if (F[baseDiag1 + id][1+jd] == 1) {
      int i = ((id < n) ? jd : (id + jd - n + 1));
      int j = id - i;
      if (sol[i][j] == '.')
	sol[i][j] = '+';
      else
	sol[i][j] = 'o';
    }

    // Print final grid
    // cout << "Final grid: " << endl;
    //FOR(i,0,n) cout << sol[i] << endl;

    // Output differences between the init and final grid
    int diff = 0;
    FOR(i,0,n) FOR(j,0,n) if (init[i][j] != sol[i][j]) diff++;
    cout << "Case #" << test << ": " << stylePoints << " " << diff << endl;
    FOR(i,0,n) FOR(j,0,n) if (init[i][j] != sol[i][j]) cout << sol[i][j] << " " << i+1 << " " << j+1 << endl;    
  }
  return 0;
}
