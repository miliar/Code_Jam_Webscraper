#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

long long t, n, cp, blad, pot, ans, mini, sum, i, tab[100];

int main()
{
	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );
	cin>>t;
	for( int tt = 1; tt <= t; tt++ )
	{
		cin>>n;
		sum = n;
		while( 1 )
		{
			pot = 1;
			cp = sum;
			i = 0;
			blad = 0;
			while( cp )
			{
				tab[++i] = cp%10;
				cp /= 10;
			}
			for( int a = i; a >= 2; a-- )
			{
				if( tab[a] > tab[a-1] )
				{
					blad = 1;
					tab[a]--;
					for( int b = a-1; b >= 1; b-- )tab[b] = 9;
				}
			}
			sum = 0;
			for( int a = 1; a <= i; a++ )sum += pot*tab[a], pot *= 10;
			for( int a = 0; a <= 20; a++ )tab[a] = 0;
			if( !blad )break;
		}
		cout<<"Case #"<<tt<<": "<<sum<<endl;
	}	
	return 0;
}
 

