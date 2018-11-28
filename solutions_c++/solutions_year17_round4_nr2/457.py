#include <bits/stdc++.h>

using namespace std;
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
const int maxn = 1000 + 50;
int n , c , m , cnt[maxn] , pos[maxn] , vis[maxn] , a[maxn] , wr[maxn];

int main( int argc , char * argv[] ){
	//freopen( "f1.in" , "r" , stdin );
	//freopen( "f1.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		n = read() , c = read() , m = read();
		memset( a , 0 , sizeof( a ) );
		memset( wr , 0 , sizeof( wr ) );
		for(int i = 1 ; i <= m ; ++ i){
			int p = read() , id = read();
			++ a[id];
			++ wr[p];
		}
		int ans = 0 ;
		for(int i = 1 ; i <= c ; ++ i) ans = max( ans , a[i] );
		int ret = 0;
		for(int i = 1 ; i <= n ; ++ i){
			ret += wr[i];
			ans = max( ans , ret / i + ( ret % i > 0 ) );
		}
		int ans2 = 0;
		for(int i = 1 ; i <= n ; ++ i)
			if( wr[i] > ans )
				ans2 += wr[i] - ans;
		printf( "Case #%d: %d %d\n" , ++ cas , ans , ans2 ) ;
	}
	return 0;
}