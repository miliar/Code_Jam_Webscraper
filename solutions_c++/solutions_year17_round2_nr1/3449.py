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

int t;
long double d, n;
map< long double, long double > m;
vector<long double> v;

int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int c = 0;
	map< long double, long double >::reverse_iterator rit;
	long double a, b, tmp, tmp2, ans;
	while( c++ < t )
	{
		cin>>d>>n;
		m.clear();
		v.clear();
		for( int i = 0; i < n; i++ )
		{
			cin>>a>>b;
			m[ a ] = b;
		}
  		for( rit = m.rbegin(); rit != m.rend(); ++rit )
		{
			if( rit == m.rbegin() )
			{
				tmp = rit->first;
				v.pb( ( d - rit->first ) / rit->second );
			}
			else
			{
				tmp2 = ( tmp - rit->first ) / rit-> second;
				v.pb( max( v.back() - tmp2, ( d - tmp ) / rit->second ) + tmp2 );
				tmp = rit->first;
			}
		}
		ans = d / v.back();
		cout<<"Case #"<<c<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
