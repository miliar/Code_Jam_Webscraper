#include <bits/stdc++.h>
using namespace std;

char a[64][64];

int main()
{
	int tc, cc = 0;
	for( cin >> tc ; tc -- ; )
	{
		int n, m;
		cin >> n >> m;
		for( int i = 0 ; i < n ; i ++ )
			for( int j = 0 ; j < m ; j ++ )
				cin >> a[i][j];
		for( int i = 0 ; i < n ; i ++ )
			for( int j = 0 ; j < m ; j ++ )
				if( a[i][j] != '?' )
				{
					for( int l = j-1 ; l >= 0 ; l -- )
						if( a[i][l] == '?' )
							a[i][l] = a[i][j];
						else
							break;
					for( int l = j+1 ; l < m ; l ++ )
						if( a[i][l] == '?' )
							a[i][l] = a[i][j];
						else
							break;
				}
		for( int i = 0 ; i < n ; i ++ )
			if( a[i][0] == '?' )
			{
				int j = i;
				while( j < n && a[j][0] == '?' )
					j ++;
				if( j < n )
				{
					for( int k = j-1 ; k >= i ; k -- )
						for( int l = 0 ; l < m ; l ++ )
							a[k][l] = a[j][l];
				}
				else
				{
					j = i;
					while( j >= 0 && a[j][0] == '?' )
						j --;
					for( int k = j+1 ; k <= i ; k ++ )
						for( int l = 0 ; l < m ; l ++ )
							a[k][l] = a[j][l];
				}
			}
		cout << "Case #" << ++cc << ":" << endl;
		for( int i = 0 ; i < n ; i ++ )
		{
			for( int j = 0 ; j < m ; j ++ )
				cout << a[i][j];
			cout << endl;
		}
	}
	return 0;
}
