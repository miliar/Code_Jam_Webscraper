#include <bits/stdc++.h>
using namespace std;
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
const int maxn = 50 + 5;

map < long long , int > vis;
vector < long long > val;
long long cnt[2048];

void DFS( long long N ){
	if( vis[N] )
		return ;
	if( !N )
		return ;
	vis[N] = 1;
	val.emplace_back( N );
	DFS( (N + 1) / 2 - 1 );
	DFS( N - (N + 1) / 2 );
}

int main( int argc , char * argv[] ){
//	freopen( "in.txt" , "r" , stdin );
//	freopen( "out.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		long long N , K ;
		scanf( "%lld%lld" , & N , & K );
		vis.clear();
		val.clear();
		DFS( N );
		sort( val.begin() , val.end() );
		for(int i = 0 ; i < val.size() ; ++ i)
			vis[val[i]] = i;
		memset( cnt , 0 , sizeof( cnt ) );
		cnt[val.size() - 1] = 1;
		while( K ){
			int j;
			for(j = val.size() - 1 ; j >= 0 ; -- j)
				if( cnt[j] )
					break;
			if( cnt[j] >= K ){
				printf( "Case #%d: %lld %lld\n" , ++ cas , val[j] - (val[j] + 1) / 2 , (val[j] + 1) / 2 - 1 );
				break;
			}else{
				K -= cnt[j];
				cnt[ vis[ (val[j] + 1) / 2 - 1 ] ] += cnt[j];
				cnt[ vis[ val[j] - (val[j] + 1) / 2 ] ] += cnt[j];
				cnt[j] = 0;
			}
		}
	}
	return 0;
}