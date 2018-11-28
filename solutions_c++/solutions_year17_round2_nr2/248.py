#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

vector< char > ans, ansik;
int n, r, o, y, g, b, v, mr, my, mb, blad, tt;

bool check()
{
	ansik.push_back( ansik[0] );
	int ok = 0;
	for( int a = 0; a+1 < ansik.size(); a++ )
	{
		if( ansik[a] == 'R' && ansik[a+1] == 'Y' )ok++;
		if( ansik[a] == 'R' && ansik[a+1] == 'B' )ok++;
		if( ansik[a] == 'R' && ansik[a+1] == 'G' )ok++;
		
		if( ansik[a] == 'Y' && ansik[a+1] == 'R' )ok++;
		if( ansik[a] == 'Y' && ansik[a+1] == 'B' )ok++;
		if( ansik[a] == 'Y' && ansik[a+1] == 'V' )ok++;
		
		if( ansik[a] == 'B' && ansik[a+1] == 'Y' )ok++;
		if( ansik[a] == 'B' && ansik[a+1] == 'R' )ok++;
		if( ansik[a] == 'B' && ansik[a+1] == 'O' )ok++;
		
		if( ansik[a] == 'V' && ansik[a+1] == 'Y' )ok++;
		if( ansik[a] == 'O' && ansik[a+1] == 'B' )ok++;
		if( ansik[a] == 'G' && ansik[a+1] == 'R' )ok++;
	}
	if( ok == ansik.size() - 1 )return 1;
	else return 0;
}
int main()
{
	cin>>tt;
	for( int ii = 1; ii <= tt; ii++ )
	{
		ans.clear();
		ansik.clear();
		mb = mr = my = 0;
		blad = 0;
		cout<<"Case #"<<ii<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		
		if( y == v && y+v == n )
		{
			for( int a = 1; a <= y; a++ )cout<<"YV";
			cout<<endl;
			continue;
		}
		if( r == g && r+g == n )
		{
			for( int a = 1; a <= r; a++ )cout<<"RG";
			cout<<endl;
			continue;
		}
		if( b == o && b+o == n )
		{
			for( int a = 1; a <= y; a++ )cout<<"BO";
			cout<<endl;
			continue;
		}
		
		if( g && r < g+1 )blad = 1;
		else r -= g;
		
		if( o && b < o+1 )blad = 1;
		else b -= o;
		
		if( v && y < v+1 )blad = 1;
		else y -= v;
		if( blad )
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		//cout<<r<<" "<<b<<" "<<y<<endl;
		int jest = 0;
		int cr = r, cb = b, cy = y;
		for( int c = 1; c <= 3; c++ )
		{
			ans.clear();
			ansik.clear();
			r = cr;
			y = cy;
			b = cb;
			if( c == 1 )
			{
				if( !r )continue; 
				ans.push_back( 'R' ), r--;
			}
			if( c == 2 )
			{
				if( !y )continue;
				ans.push_back( 'Y' ), y--;
			}
			if( c == 3 )
			{
				if( !b )continue;
				ans.push_back( 'B' ), b--;
			}
			//for( int a = 0; a < ans.size(); a++ )cout<<ans[a];
			//cout<<endl;
			while( r + y + b > 0 )
			{
				//cout<<r<<" "<<b<<" "<<y<<endl;
				if( ans.back() == 'Y' )
				{
					if( !r && !b )ans.push_back( 'Y' ), y--;
					else if( r >= b )ans.push_back( 'R' ), r--;
					else ans.push_back( 'B' ), b--;
				}
				else if( ans.back() == 'R' )
				{
					if( !b && !y )ans.push_back( 'R' ), r--;
					else if( y >= b )ans.push_back( 'Y' ), y--;
					else ans.push_back( 'B' ), b--;
				}
				else if( ans.back() == 'B' )
				{
					if( !r && !y )ans.push_back( 'B' ), b--;
					else if( r >= y )ans.push_back( 'R' ), r--;
					else ans.push_back( 'Y' ), y--;
				}
				//for( int a = 0; a < ans.size(); a++ )cout<<ans[a];
			//cout<<endl;
			}
			//cout<<endl;
			mr = mb = my = 0;
			for( int a = 0; a < ans.size(); a++ )
			{
				ansik.push_back( ans[a] );
				if( ans[a] == 'R' && !mr )
				{
					mr = 1;
					//ansik.push_back( 'R' );
					for( int bb = 1; bb <= g; bb++ )ansik.push_back( 'G' ), ansik.push_back( 'R' );
				}
				if( ans[a] == 'Y' && !my )
				{
					my = 1;
					//ansik.push_back( 'Y' );
					for( int bb = 1; bb <= v; bb++ )ansik.push_back( 'V' ), ansik.push_back( 'Y' );
				}
				if( ans[a] == 'B' && !mb )
				{
					mb = 1;
					//ansik.push_back( 'B' );
					for( int bb = 1; bb <= o; bb++ )ansik.push_back( 'O' ), ansik.push_back( 'B' );
				}
				
			}
			//for( int a = 0; a < ansik.size(); a++ )cout<<ansik[a];
			//cout<<endl;
			if( check() )
			{
				for( int a = 0; a+1 < ansik.size(); a++ )cout<<ansik[a];
				jest = 1;
				break;
			}
			else
			{
				ansik.pop_back();
				swap( ansik[ansik.size()-1], ansik[ansik.size()-2] );
				if( check() )
				{
					for( int a = 0; a+1 < ansik.size(); a++ )cout<<ansik[a];
					jest = 1;
				}
				break;
			}
		}
		if( !jest )cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	
	return 0;
}
 

