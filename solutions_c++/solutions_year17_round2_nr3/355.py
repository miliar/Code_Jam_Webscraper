#include <bits/stdc++.h>
const int mod = 1e9 + 7;
inline int mul( int x , int y ){ return 1LL * x * y % mod ;}
int power_mod( int x , int y ){int ret = 1;while( y ){if( y & 1 ) ret = mul( ret , x );y >>= 1;x = mul( x , x );}return ret;}
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
using namespace std;
const double eps = 1e-6;
const int maxn = 100 + 15;
long long dis[maxn][maxn];
int n , E[maxn] , S[maxn] , Q;
double dp[maxn];
priority_queue < pair < double , int > > pq;

void Dijkstra(){
	while( !pq.empty() ){
		pair < double , int > st = pq.top() ; pq.pop();
		double t = -st.first;
		int x = st.second;
		if( fabs( t - dp[x] ) > eps )
			continue;
		for(int i = 1 ; i <= n ; ++ i)
			if( dis[x][i] <= E[x] ){
				double newt = t + ( double ) dis[x][i] / ( double ) S[x];
				if( newt < dp[i] ){
					dp[i] = newt;
					pq.push( make_pair( - dp[i] , i ) );
				}
			}
	}
}

int main( int argc , char * argv[] ){
	//freopen( "in.txt" , "r" , stdin );
	//freopen( "out.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		n = read() , Q = read();
		for(int i = 1 ; i <= n ; ++ i)
			E[i] = read() , S[i] = read();
		for(int i = 1 ; i <= n ; ++ i)
			for(int j = 1 ; j <= n ; ++ j){
				int x = read();
				if( x == -1 )
					dis[i][j] = 1LL << 58;
				else
					dis[i][j] = x;
				if( i == j )
					dis[i][j] = 0;
			}
		for(int k = 1 ; k <= n ; ++ k)
			for(int i = 1 ; i <= n ; ++ i)
				for(int j = 1 ; j <= n ; ++ j)
					dis[i][j] = min( dis[i][j] , dis[i][k] + dis[k][j] );
		printf( "Case #%d:" , ++ cas );
		while( Q -- ){
			int st = read() , ed = read();
			for(int i = 1 ; i <= n ; ++ i)
				dp[i] = 1e18;
			dp[st] = 0;
			pq.push( make_pair( 0 , st ) );
			Dijkstra();
			printf( " %.6lf" , dp[ed] );
		}
		puts( "" );
	}
	return 0;
}