#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

inline bool check(string s)
{
	if ( s.size() == 1 )
		return true;
	for(int i = 0; i + 1  < s.size(); i++)
		if ( s[i] > s[i+1])
			return false;
	return true;
}

long long toInt(string s)
{
	long long res = 0;
	for ( int i = 0; i < s.size(); i++ )
		res = res * 10 + int(s[i] - '0');
	return res;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for ( int h = 0; h < t; h++ )
	{
		string s;
		cin >> s;
		if ( !check(s) )
		{
			string ss = s;
			for ( int i = 0; i < ss.size(); i++ )
				ss[i] = '1';
			if ( toInt(ss) > toInt(s) )
			{
				cout << "Case #" << h+1 << ": ";
				ss.pop_back();
				for ( int i = 0; i < ss.size(); i++ )
					ss[i] = '9';
				cout << ss << endl;
				continue;
			}

			string ress;
			for ( int i = 0; i < s.size(); i++ )
			{
				ss = s.substr(i);
				if ( ress.size() == s.size() )
					break;
				for ( int k = 9; k >= 0; k-- )
				{
					for ( int j = 0; j < ss.size(); j++ )
					{
						ss[j] = char('0' + k);
					}
					if ( toInt(s.substr(i)) >= toInt(ss) )
					{
						ress += ss[0];
						if ( ress.size() != s.size() && ss[0] != s[i] )
							while ( ress.size() != s.size() )
								ress += "9";
						break;
					}
				}					
			}
			cout << "Case #" << h+1 << ": " << ress << endl;
		}
		else
			cout << "Case #" << h+1 << ": " << s << endl;
	}

	return 0;
}