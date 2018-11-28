#include <bits/stdc++.h>
using namespace std;
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
const int maxn = 50 + 5;

char s[maxn];
int n;
long long dp[maxn][2][10];

inline void Modify( long long & x , long long y ){
	x = max( x , y );
}

int main( int argc , char * argv[] ){
//	freopen( "in.txt" , "r" , stdin );
//	freopen( "out.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		scanf( "%s" , s + 1 );
		n = strlen( s + 1 );
		memset( dp , -1 , sizeof( dp ) );
		dp[0][0][0] = 0;
		for(int i = 0 ; i < n ; ++ i)
			for(int f = 0 ; f < 2 ; ++ f)
				for(int pre = 0 ; pre < 10 ; ++ pre)
					if( ~dp[i][f][pre] ){
						int ed = f ? 9 : s[i + 1] - '0';
						for(int add = pre ; add <= ed ; ++ add)
							Modify( dp[i + 1][f | (add < ed)][add] , dp[i][f][pre] * 10LL + add );
					}
		long long ans = 0;
		for(int f = 0 ; f < 2 ; ++ f)
			for(int pre = 0 ; pre < 10 ; ++ pre)
				ans = max( ans , dp[n][f][pre] );
		printf( "Case #%d: %lld\n" , ++ cas , ans );
	}
	return 0;
}