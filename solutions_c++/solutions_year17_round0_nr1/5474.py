#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

#define fastio ios_base::sync_with_stdio(false);
#define fi first
#define se second

char str[15];
int memo[1<<10];
int vis[1<<10];

int T, len, m, k, y, step;

void bfs(){
	queue<ii> q;
	q.push(ii(m, 0));
	ii x;
	vis[m] = step;
	memo[m] = 0;
	
	while(!q.empty()){
		x = q.front();
		q.pop();
		
		for(int i = 0; i < len; ++i){
			if(i + k - 1 < len){
				y = x.fi;
								
				for(int j = i; j <= i + k - 1; ++j){
					y ^= (1 << j);
				}
				
				if(vis[y] != step){
					vis[y] = step;
					memo[y] = x.se + 1;
					q.push(ii(y, x.se + 1));
				}
			}
		}
	}
}

int main(){
	
	scanf("%d", &T);
	
	for(int t = 1; t <= T; ++t){
		scanf(" %s %d", str, &k);
		len = strlen(str), m = 0;
		
		for(int i = 0; i < len; ++i){
			if(str[i] == '+'){
				m |= (1 << (len-1-i));
			}
		}
		
		printf("Case #%d: ", t);
		if(m == ((1<<len)-1)) printf("0\n");
		else{
			step++;
			bfs();
		
			if(vis[(1<<len) - 1] == step) printf("%d\n", memo[(1<<len)-1]);
			else printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
