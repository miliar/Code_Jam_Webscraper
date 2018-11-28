#include <bits/stdc++.h>
const int mod = 1e9 + 7;
inline int mul( int x , int y ){ return 1LL * x * y % mod ;}
int power_mod( int x , int y ){int ret = 1;while( y ){if( y & 1 ) ret = mul( ret , x );y >>= 1;x = mul( x , x );}return ret;}
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
using namespace std;
const int maxn = 2e5 + 50;
const int inf = 2e9 + 1;

int N , R , O , Y , G , B , V , num[3];

char trans( int x ){
	if( x == 0 )
		return 'R';
	else if( x == 1 )
		return 'Y';
	else
		return 'B';
}

int main( int argc , char * argv[] ){
//	freopen( "in.txt" , "r" , stdin );
//	freopen( "out2.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		cin >> N >> R >> O >> Y >> G >> B >> V;
		vector < char > ans;
		printf( "Case #%d: " , ++ cas );
		/*if( max( max( R , Y ) , B ) >= ( N + 1 ) / 2 ){
			printf( "IMPOSSIBLE\n" );
			continue;
		}*/
		for(int fst = 0 ; fst < 3 ; ++ fst){
			num[0] = R , num[1] = Y , num[2] = B;
			if( !num[fst] )
				continue;
			-- num[fst];
			vector < char > take;
			take.emplace_back( trans( fst ) );
			int pre = fst;
			for(int i = 1 ; i < N ; ++ i){
				int select = -1;
				for(int j = 0 ; j < 3 ; ++ j)
					if( j != pre && (select == -1 || num[j] > num[select]) )
						select = j;
				/*if( fst == 0 && i == 3 ){
					cout << "select is " << select << " pre is " << pre << endl;
					cout << "check is : ";
					for(auto it : take)
						cout << it;
					cout << endl;
				}*/
				if( select == -1 )
					break;
				if( !num[select] )
					break;
				-- num[select];
				pre = select;
				if( i == N - 1 && select == fst )
					break;
				take.emplace_back( trans( select ) );
			}
			if( take.size() == N )
				ans = take;
		}
		if( ans.size() != N ){
			puts( "IMPOSSIBLE" );
			continue;
		}
		//assert( ans.size() == N );
		for(auto it : ans) putchar( it ) ;
		puts( "" );
	}
	return 0;
}