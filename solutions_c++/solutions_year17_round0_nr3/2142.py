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
map< long long, map< long long, long long > > m;

map< long long, long long > build( long long a )
{
	if( m.find( a ) == m.end() )
	{
		map< long long, long long > m1, m2;
		m1[ a ] = 1;
		if( a > 1 )
		{
			m2 = build( a / 2 );
			for( map< long long, long long >::iterator it = m2.begin(); it != m2.end(); it++ )
				if( m1.find( it->first ) == m1.end() )
					m1[ it->first ] = it->second;
				else
					m1[ it->first ] += it->second;
			if( a > 2 )
			{
				m2 = build( ( a + 1 ) / 2 - 1 );
				for( map< long long, long long >::iterator it = m2.begin(); it != m2.end(); it++ )
					if( m1.find( it->first ) == m1.end() )
						m1[ it->first ] = it->second;
					else
						m1[ it->first ] += it->second;
			}
		}
		m[ a ] = m1;
		//cout<<a<<endl;
	}
	return( m[ a ] );
}

int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int c = 0;
	long long n, k, ans, lans, rans;
	while( c++ < t )
	{
		cin>>n>>k;
		ans = 0;
		map< long long, long long > tmp = build( n );
		for( map< long long, long long >::reverse_iterator it = tmp.rbegin(); it != tmp.rend(); it++ )
		{
			ans += it->second;
			if( ans >= k )
			{
				ans = it->first;
				break;
			}
		}
		/*for( int i = 0; i < tmp.size(); i++ )
			cout<<i<<" "<<tmp[ i ]<<"\t";
		cout<<endl;*/
		lans = ans / 2;
		rans = ( ans + 1) / 2 - 1;
		cout<<"Case #"<<c<<": "<<lans<<" "<<rans<<endl;
	}
	return 0;
}
