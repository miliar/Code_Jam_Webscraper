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

int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int tmp, c = 0;
	int tmp2[ 20 ];
	long long n, ans;
	while( c++ < t )
	{
		cin>>n;
		ans = 0;
		tmp = 0;
		for( long long int i = n; i > 0; i /= 10 )
			tmp2[ tmp++ ] = i % 10;
		for( int i = tmp - 1; i > 0; i-- )
		{
			if( tmp2[ i ] > tmp2[ i - 1 ] )
			{
				while( i + 1 < tmp && tmp2[ i ] == tmp2[ i + 1 ] )
					i++;
				tmp2[ i ] -= 1;
				while( --i >= 0 )
					tmp2[ i ] = 9;
				break;
			}
		}
		for( int i = tmp - 1; i >= 0; i-- )
			ans = ans * 10 + tmp2[ i ];
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
