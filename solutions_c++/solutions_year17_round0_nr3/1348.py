#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

long long n, k, p, i, mini, maks, t;
vector< pair< long long, long long > > v;

int main()
{
	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );
	cin>>t;
	for( int a = 1; a <= t; a++ )
	{
		cin>>n>>k;
		v.clear();
		v.push_back( make_pair( n, 1 ) );
		p = 0;
		while( 1 )
		{
			n = v[p].first;
			i = v[p].second;
			if( n%2 )
			{
				if( v.back().first == (n-1)/2 )v.back().second += 2*i;
				else v.push_back( make_pair( (n-1)/2, 2*i ) );
				mini = (n-1)/2;
				maks = mini;
			}
			else
			{
				if( v.back().first == n/2 )v.back().second += i;
				else v.push_back( make_pair( n/2, i ) );
				v.push_back( make_pair( (n-2)/2, i ) );
				mini = (n-2)/2;
				maks = n/2;
			}	
			if( k <= i )
			{
				cout<<"Case #"<<a<<": "<<maks<<" "<<mini<<endl;
				break;
			}
			else k -= i;
			p++;
		}
	}	
	return 0;
}
 

