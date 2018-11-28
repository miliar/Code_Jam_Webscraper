#include <iostream>
#include <map>

using namespace std;

int main()
{
	int t;
	cin >> t;
	int Case = 1;
	char mp[26][26];
	while( t--)
	{
		int c, r;
		cin >> r >> c;
		map< pair<int, int>, char> points;
		for( int i = 0; i < r; i++)
			for( int j = 0; j < c; j++)
			{
				char tmp;
				cin >> tmp;
				mp[i][j] = tmp;
				if( tmp != '?')
					points[ pair<int, int>(i, j)] = tmp;
			}
		int last = -1;
		for( map< pair<int, int>, char>::iterator it = points.begin(); it != points.end(); ++it)
		{
			int from = (last == it->first.first) ? it->first.second : 0;
			for( int i = from; i < c; i++)
				mp[it->first.first][i] = it->second;
			last = it->first.first;
		}
		int first = -1;
		for( int j = 0; j < c; j++)
		{
			char ch = '?';
			for( int i = 0; i < r; i++)
			{
				if(mp[i][j] != '?')
				{
					ch = mp[i][j];
					if(first == -1)
						first = i;
				}
				mp[i][j] = ch;
			}
		}
		for( int j = 0; j < c; j++)
		{
			char ch;
			for( int i = first; i >-1 ; i--)
			{
				if(mp[i][j] != '?')
					ch = mp[i][j];
				mp[i][j] = ch;
			}
		}
		cout << "Case #" << Case++ << ":" << endl ;
		for( int i = 0; i < r; i++)
		{
			for( int j = 0; j < c; j++)
				cout << mp[i][j];
			cout << endl;
		}
	}
	return 0;
}