#include <bits/stdc++.h>

using namespace std;



int n, q;
int nodes[105];
double e[105];
double s[105];
double cost[105];
double edges[104][104];
double dist[104][104];
double dp[104][104];
bool vis[104][104];
double solve(int ss,int x){
    if(vis[ss][x])return dp[ss][x];
    if(x == n-1){
        return 0;
    }
    vis[ss][x] = true;
    double ret = 1e17;
    double c = cost[x];
    int j = nodes[x];
    if(dist[ss][j] <= e[ss]){
        ret = min(ret, solve(ss,j)+c/s[ss]);
    }
    if(c <= e[x]){
        ret = min(ret, solve(x,j)+c/s[x]);
    }
    return dp[ss][x] = ret;
}
int main() {
  freopen("inp.text","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  cout << fixed << setprecision(20);
  cin >> T;
  for(int t = 1 ; t <= T ; t ++){
    memset(vis,0, sizeof vis);
    cout << "Case #"<<t<<": ";
    cin >> n >> q;
    for(int i = 0 ; i < n ;  i ++){
        cin >> e[i] >> s[i];
    }
    for(int i = 0 ; i < n ;  i ++){
        nodes[i] = -1, cost[i] = 0;
        for(int j = 0 ; j < n ; j ++){
            cin >> edges[i][j];
            dist[i][j] = -1;
            if(edges[i][j] != -1)
                nodes[i] = j, cost[i] = edges[i][j];
        }
    }
    for(int i = 0 ; i < n ; i ++){
        double tmp = 0;
        int j = i;
        while(j != n-1){
            dist[i][j] = tmp;
            tmp += cost[j];
            j = nodes[j];
        }
        dist[i][j] = tmp;
    }
    int tmp;
    for(int i = 0 ; i < q;  i ++){
        cin >> tmp >> tmp;
    }
    cout << solve(0,0);
    cout << endl;
  }
  return 0;
}
