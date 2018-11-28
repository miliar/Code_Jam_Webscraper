#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <deque>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200              
#define sz(a) (int)a.size()
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;

int t, n, q;
ll e[N], s[N], d[N][N], sum[N];
double dp[N];
int u[N], v[N], used[N];



int main () {
    //freopen("in", "r", stdin);
     cin >> t;
     int cs = 0;
     while (t--) {
               cs++;
          cout << "Case #"<<cs<<": ";
          cin >> n >> q;
          for (int i = 1; i <= n; i++)
          	cin >> e[i] >> s[i];
          for (int i = 1; i <= n; i++)
          	for (int j = 1; j <= n; j++)  {
          		cin >> d[i][j];
          		if (i==j) d[i][j] = 0;
          		if (d[i][j] == -1) d[i][j] = 1e17;;	
          	}
          for (int k = 1; k <= n; k++)
          	for (int i = 1; i <= n; i++)
          		for (int j = 1; j <= n; j++)
          			 d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

          for (int i =1; i <= q; i++)
          	cin >> u[i] >> v[i];


      	for (int it = 1; it <= q; it++) {
      	 	for (int i = 1; i <= n; i++)
      	 		dp[i] = 1e17;
      	 	dp[u[it]] = 0;
     		memset(used, 0, sizeof used);
      	 	for (int tt = 1; tt <= n; tt++) {
      	 	 	int vv = -1;
      	 	 	for (int i = 1; i <= n; i++)
      	 	 		if (!used[i] && (vv == -1 || dp[i] < dp[vv])) vv = i;
      	 	 	used[vv] = 1;
      	 	 	for (int i = 1; i <= n; i++)
      	 	 		if (d[vv][i] <= e[vv])
      	 	 			dp[i] = min(dp[i], dp[vv] + d[vv][i]*1.0/s[vv]);
      	 	}
      	 	printf("%.7f ", dp[v[it]]);
      	}
      	printf("\n");


     }
     return 0;
}