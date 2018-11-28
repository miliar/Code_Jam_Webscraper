#include <bits/stdc++.h>

using namespace std;
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}

int n , p , cnt[4] , dp[105][105][105];

int DFS( int x , int y , int z ){
	if( ~dp[x][y][z] )
		return dp[x][y][z];
	int & ans = dp[x][y][z] = ( x + y + z + 3 ) / 4;
	for(int c1 = 0 ; c1 <= x && c1 <= 4 ; ++ c1)
		for(int c2 = 0 ; c2 <= y && c1 + 2 * c2 <= 4 ; ++ c2)
			for(int c3 = 0 ; c3 <= z && c1 + 2 * c2 + 3 * c3 <= 4 ; ++ c3)
				if( c1 + 2 * c2 + 3 * c3 == 4 )
					ans = max( ans , DFS( x - c1 , y - c2 , z - c3 ) + 1 );
	return ans;
}

int main( int argc , char * argv[] ){
	//freopen( "in.txt" , "r" , stdin );
	//freopen( "out.txt" , "w" , stdout );
	memset( dp , -1 , sizeof( dp ) );
	int T = read() , cas = 0;
	while( T -- ){
		n = read() , p = read();
		memset( cnt , 0 , sizeof( cnt ) );
		for(int i = 1 ; i <= n ; ++ i){
			int x = read();
			x %= p;
			++ cnt[x];
		}
		printf( "Case #%d: " , ++ cas );
		if( p == 2 ) printf( "%d\n" , cnt[0] + (cnt[1] + 1) / 2 );
		else if( p == 3 ){
			int ret = min( cnt[1] , cnt[2] );
			cnt[1] -= ret , cnt[2] -= ret;
			int ans = cnt[0] + ret + ( max( cnt[1] , cnt[2] ) + 2 ) / 3;
			printf( "%d\n" , ans );
		}else if( p == 4 )
			printf( "%d\n" , cnt[0] + DFS( cnt[1] , cnt[2] , cnt[3] ) );
	}
	return 0;
}