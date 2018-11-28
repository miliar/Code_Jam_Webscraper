#include<bits/stdc++.h>
using namespace std;
#define lli long long
#define mod 1000000007
#define inf 1000000007
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define lim 200007
#define pi 3.14159265358979323846

int t, n, k;
double ans, a, u, tmp;
vector< double > v;

int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int c = 0;
	double a;
	while( c++ < t )
	{
		cin>>n>>k>>u;
		v.clear();
		for( int i = 0; i < n; i++ )
		{
			cin>>a;
			v.pb( a );
		}
		v.pb( 1 );
		sort( v.begin(), v.end() );
		for( int i = 0; i < n; i++ )
		{
			tmp = 0;
			for( int j = 0; j <= i; j++ )
				tmp += v[ j ];
			if( ( i + 1 ) * v[ i + 1 ] - tmp <= u )
			{
				u -= ( ( i + 1 ) * v[ i + 1 ] - tmp );
				for( int j = 0; j <= i; j++ )
					v[ j ] = v[ i + 1 ];
			}
			else
			{
				for( int j = 0; j <= i; j++ )
					v[ j ] += u / ( i + 1 );
				break;
			}
		}
		ans = 1;
		for( int i = 0; i < n; i++ )
		{
			//cout<<v[ i ]<<endl;
			ans *= v[ i ];
		}
		//cout<<"Case #"<<c<<": "<<setprecision(10)<<ans<<endl;
		printf( "Case #%d: %.10f\n", c, ans );
	}
	return 0;
}
