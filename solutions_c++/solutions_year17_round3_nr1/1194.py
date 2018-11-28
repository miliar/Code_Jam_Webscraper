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
long double tans, ans, tmp2, tmp3;
vector< pair<int,int> > v;
vector< long long > nv, nv2;
int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int a, b, c = 0;
	pair< int, int > tmp;
	vector< pair<int,int> >::reverse_iterator rit, trit;
	while( c++ < t )
	{
		cin>>n>>k;
		v.clear();
		nv.clear();
		for( int i = 0; i < n; i++ )
		{
			cin>>a>>b;
			tmp = mp( a, b );
			v.pb( tmp );
		}
		sort( v.begin(), v.end() );
		for( int i = 0; i < n; i++ )
		{
			tmp2 = v[ i ].first;
			tmp3 = v[ i ].second;
			nv.pb( tmp2 * tmp3 );
		}
		ans = 0;
		for( int j = n - 1; j >= k - 1; j-- )
		{
			tmp2 = v[ j ].first;
			tans = pi * tmp2 * tmp2;
			nv2 = nv;
			sort( nv2.begin(), nv2.begin() + j );
			for( int i = 0; i < k; i++ )
				tans += 2 * pi * nv2[ j - i ];
			if( ans < tans )
				ans = tans;
		}
		//cout<<"Case #"<<c<<": "<<setprecision(10)<<ans<<endl;
		printf( "Case #%d: %.10Lf\n", c, ans );
	}
	return 0;
}
