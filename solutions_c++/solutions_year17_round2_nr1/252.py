#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int tt, n, ptr, which;
long double pos, speed, mini, inf = 1e18, ans, len, tim, maks;
pair< long double, long double > tab[1010];
int main()
{
	cin>>tt;
	cout<<setprecision( 10 )<<fixed;
	for( int ii = 1; ii <= tt; ii++ )
	{
		maks = 0;
		cin>>len>>n;
		for( int a = 1; a <= n; a++ )
		{
			cin>>tab[a].first>>tab[a].second;
			maks = max( maks, ( len - tab[a].first ) / tab[a].second );
		}
		cout<<"Case #"<<ii<<": "<<len/maks<<endl;
		//sort( tab + 1, tab + n + 1 );
		//pos = tab[1].first;
		//speed = tab[1].second;
		//ptr = 1;
		//which = -1;
		//ans = 0;
		//while( 1 )
		//{
			//mini = inf;
			//which = -1;
			//for( int a = ptr+1; a <= n; a++ )
			//{
				//if( tab[a].second < speed )
				//{
					//tim = ( tab[a].first - pos ) / ( speed - tab[a].second );
					//if( tim < mini )
					//{
						//mini = tim;
						//which = a;
					//}
				//} 
			//}
			//if( which == -1 )
			//{
				//ans += (len - pos)/speed;
				////cout<<len<<" "<<ans<<endl;
				//cout<<"Case #"<<ii<<": "<<len/ans<<endl;
				//break;
			//}
			//else
			//{
				//ans += mini;
				//ptr = which;
				//pos += speed * mini;
				//speed = tab[ptr].second;
				
			//}
		//}
	}
	
	return 0;
}
 

