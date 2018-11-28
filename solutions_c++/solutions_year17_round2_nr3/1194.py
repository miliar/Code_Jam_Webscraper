#include<bits/stdc++.h>
using namespace std;
int n, d[105][105], e[105], s[105];
const int eps = 0.000001;
long double dp[105][105];
priority_queue<pair<double,pair<int,pair<int,int> > > > qq;

int dfs(int a, int b, int sp, int zywot){
  qq.push(make_pair(-1.0, make_pair(b, make_pair(sp, zywot))));
  
  while(qq.size()){
	pair<double,pair<int,pair<int,int> > > p = qq.top();
	qq.pop();
	b = p.second.first;
	sp = p.second.second.first;
	zywot = p.second.second.second;
	if ( -p.first != dp[a][b] ) continue;
	
	for(int i = 1; i <= n; i ++ ) {
	  if ( d[b][i] == -1 or i == a ) continue;
	  if ( d[b][i] <= zywot ){
		double ndp = dp[a][b] + d[b][i] * 1.0 / sp;
		if ( dp[a][i] == 0 or dp[a][i] - ndp < eps ){
		  dp[a][i] = ndp;
// 		  printf("dp[%d][%d] = %lf\n", a,i,ndp);
		  qq.push(make_pair(-dp[a][i], make_pair(i, make_pair(sp, zywot-d[b][i]))));
		}
	  }
	}
  }
}
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++){
	int q;
	scanf("%d %d", &n, &q);
	for(int i = 1; i <= n; i ++) scanf("%d %d", &e[i], &s[i]);
	for(int i = 1; i <= n; i ++) 
	  for(int j = 1; j <= n; j ++) {
		scanf("%d", &d[i][j]);
		dp[i][j] = 0;
	  }
	  
	for(int i = 1; i <= n; i ++) {
	  dp[i][i] = 1;
	  dfs(i,i,s[i],e[i]);
	}
	for(int i = 1; i <= n; i ++){
	  for(int j = 1; j <= n; j ++ ) {
		dp[i][j] -= 1;
// 		printf("%lf ", dp[i][j]);
	  }
// 	  puts("");
	}
	for(int i = 1; i <= n; i ++)
	  for(int j = 1; j <= n; j ++ ) 
		for(int k = 1; k <= n; k ++ ){
		  if ( dp[j][i] == -1) continue;
		  if ( dp[i][k] == -1 ) continue;
// 		  printf("%d -- (%d) -- %d\n", j, i, k );
// 		  printf("old %lf new %lf\n", d[j][k], d[j][i] + d[i][k]);
		  if ( dp[j][k] - (dp[j][i] + dp[i][k]) > eps or dp[j][k] == -1.0 ) dp[j][k] = dp[j][i] + dp[i][k];
		}
		
	printf("Case #%d: ", t);		  
	while(q--){
	  int a, b;
	  scanf("%d %d", &a, &b);
	  printf("%.7Lf ", dp[a][b]);
	}
	puts("");
  }
  return 0;
}