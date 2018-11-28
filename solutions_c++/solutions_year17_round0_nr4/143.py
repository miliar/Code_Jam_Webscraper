#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int match_rc[210] , match_d[410] , visited[410] ;
int grid[110][110] , init[110][110] ;
int n , m ;
int adj[210][210] , adj_d[410][410] ;

bool dfs1(int x){
	visited[x] = 1;
	int v ;
	for(int i=1;i<=n;i++){
		v = ( (x <= 100) ? i+100 : i ) ;
		if( !adj[x][v] ) continue ;
		if( match_rc[v] ) continue ;
		match_rc[x] = v ;
		match_rc[v] = x ;
		return 1 ;
	}
	for(int i=1;i<=n;i++){
		v = ( (x <= 100) ? i+100 : i ) ;
		if( !adj[x][v] ) continue ;
		if( !visited[match_rc[v]] && dfs1( match_rc[v] ) ) {
			match_rc[x] = v ;
			match_rc[v] = x ;
			return 1 ;
		}
	}
	return 0 ;
}

bool dfs2(int x){
	visited[x] = 1;
	int v ;
	for(int i=1;i<=2*n;i++){
		v = i+200 ;
		if( !adj_d[x][v] || match_d[v] ) continue ;
		match_d[v] = x ;
		match_d[x] = v ;
		return 1 ;
	}
	for(int i=1;i<=2*n;i++){
		v = i+200 ;
		if(!adj_d[x][v]) continue ;
		if(!visited[match_d[v]] && dfs2(match_d[v]) ){
			match_d[v] = x; match_d[x] = v ;
			return 1  ;
		}
	}
	return 0 ;
}

int main(){
    freopen("D_large.in","r",stdin);
    freopen("D_large.out","w",stdout);
	int t , x , y ;
	char c ;
	scanf("%d",&t);
	for(int T = 1 ; T <= t ; T++){
		for(int i=1;i<=100;i++) for(int j=1;j<=100;j++) grid[i][j] = init[i][j] = 0 ;
		memset( adj , 0 , sizeof adj ) ; memset(adj_d , 0 , sizeof adj_d) ;
		memset( match_rc , 0 , sizeof match_rc ) ; memset(match_d , 0 , sizeof match_d) ;
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				adj[i][j+100] = adj[j+100][i] = 1 ;
				adj_d[i+j][i-j+n+200] = adj_d[i-j+n+200][i+j] = 1 ;
			}
		}
		for(int i=0;i<m;i++){
			cin >> c >> x >> y ;
			if( c == 'x' || c=='o' ){
				for(int j = 1 ; j <= n ; j++ ){
					adj[x][j+100] = adj[j+100][x] = 0 ;
					adj[j][y+100] = adj[y+100][j] = 0 ;
				}
				match_rc[x] = y+100 ;
				match_rc[y+100] = x ;
				init[x][y] |= 1 ;
			}
			if( c == '+' || c=='o' ){
				for(int j = 1 ; j <= 2*n ; j++ ){
					adj_d[x+y][j+200] = adj_d[j+200][x+y] = 0;
					adj_d[x-y+n+200][j] = adj_d[j][x-y+n+200] = 0;
				}
				match_d[x+y] = x-y +n + 200 ;
				match_d[x-y+n+200] = x+y ;
				init[x][y] |= 2 ;
			}
		}
		bool chk = 1 ;
		while(chk){
			chk = 0 ;
			memset(visited , 0 , sizeof visited);
			for(int i=1;i<=n;i++) if( !match_rc[i] && !visited[i] ) chk |= dfs1(i) ;
		}
		chk = 1 ;
		while(chk){
			chk = 0 ;
			memset(visited , 0 , sizeof visited);
			for( int i=2 ; i <= 2 * n ; i++ ) if( !match_d[i] && !visited[i] ) chk |= dfs2(i) ;
		}
		int ans = 0 , chng = 0 ;
		for(int i=1;i<=n;i++){
			if(!match_rc[i]) continue ;
			ans++ ;
		//	printf("row :: %d %d\n" , i ,match_rc[i] - 100) ;
			grid[i][match_rc[i] - 100] |= 1 ;
		}
		//printf("%d :: \n",ans) ;
		for(int i=1;i<=2*n;i++){
			if(!match_d[i]) continue ;
			ans++ ;
			x = i + match_d[i] - n - 200 ; y = i - match_d[i] + n + 200 ;
			x/=2 ; y/=2 ;
		//	printf("diag :: %d %d\n" , x ,y) ;
			grid[x][y] |= 2 ;
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(grid[i][j] != init[i][j]) chng++ ;
			//	printf("%d ",grid[i][j]);
			}
			//printf("\n") ;
		}
		/*for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				printf("%d ",init[i][j]);
			}
			printf("\n") ;
		}*/
		printf("Case #%d: %d %d\n",T,ans , chng) ;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(grid[i][j] != init[i][j]){
					if(grid[i][j] == 3) printf("o ") ;
					else if(grid[i][j] == 2 ) printf("+ ");
					else printf("x ");
					printf("%d %d\n",i,j) ;
				}
			}
		}
	}
	return 0;
}
