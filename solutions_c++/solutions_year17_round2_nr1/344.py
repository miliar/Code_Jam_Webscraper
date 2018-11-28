#include <bits/stdc++.h>
const int mod = 1e9 + 7;
inline int mul( int x , int y ){ return 1LL * x * y % mod ;}
int power_mod( int x , int y ){int ret = 1;while( y ){if( y & 1 ) ret = mul( ret , x );y >>= 1;x = mul( x , x );}return ret;}
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
using namespace std;
const int maxn = 2e5 + 50;
const int inf = 2e9 + 1;


int main( int argc , char * argv[] ){
	//freopen( "in.txt" , "r" , stdin );
	//freopen( "out.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		int D = read() , N = read();
		double time = 0;
		for(int i = 1 ; i <= N ; ++ i){
			int x = read() , y = read();
			int dis = D - x;
			time = max( time , ( double ) dis / ( double ) y );
		}
		printf( "Case #%d: %.6lf\n" , ++ cas , ( double ) D / ( double ) time  );
	}
	return 0;
}