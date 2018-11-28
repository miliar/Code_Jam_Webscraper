#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int x, n, p, i[20], ans, v;

int main()
{
	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );
	//cout<<setprecision( 10 )<<fixed;
	int tt;
	cin>>tt;
	for( int aa = 1; aa <= tt; aa++ )
	{
		cout<<"Case #"<<aa<<": ";
		
		cin>>n>>p;
		for( int a = 0; a < 10; a++ )i[a] = 0;
		for( int a = 1; a <= n; a++ )
		{
			cin>>x;
			i[x%p]++;
		}
		if( p == 2 )
		{
			if( i[1]%2 )cout<<i[0] + (i[1]/2) + 1<<endl;
			else cout<<i[0] + (i[1]/2)<<endl;
			continue;
		}	
		if( p == 3 )
		{
			ans = 0;
			ans += i[0];
			v = min( i[1], i[2] );
			ans += v;
			i[1] -= v;
			i[2] -= v;
			ans += (i[1]/3);
			ans += (i[2]/3);
			i[1]%=3;
			i[2]%=3;
			if( i[1] || i[2] )ans++;
			cout<<ans<<endl;
		}
		if( p == 4 )
		{
			ans = 0;
			ans += i[0];
			ans += (i[2]/2);
			i[2]%=2;
			v = min( i[3], i[1] );
			ans += v;
			i[3] -= v, i[1] -= v;
			if( i[1] )
			{
				if( i[2] )
				{
					if( i[1] >= 2 )
					{
						i[1] -= 2;
						i[2] = 0;
						ans++;
					}
				}
				ans += (i[1]/4);
				i[1]%=4;
			}
			if( i[3] )
			{
				if( i[2] )
				{
					if( i[3] >= 2 )
					{
						i[3] -= 2;
						i[2] = 0;
						ans++;
					}
				}
				ans += (i[3]/4);
				i[3]%=4;
			}
			if( i[1] || i[2] || i[3] )ans++;
			cout<<ans<<endl;
		}
		
		
		
	}
	return 0;
}
 

