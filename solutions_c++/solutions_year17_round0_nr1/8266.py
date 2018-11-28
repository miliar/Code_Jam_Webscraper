#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int Case = 1;
	while( n--)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		bool *v;
		v = new bool [s.length()];
		for( int i = 0; i < s.length(); i++)
			v[i] = ( s[i] == '+');
		bool mask[k];
		for( int i = 0; i < k; i++)
			mask[i] = true;
		int flips = 0;
		for( int i = 0; i < s.length()-k+1; i++)
			if( !v[i])
			{
				flips++;
				for( int j = 0; j < k; j++)
					v[i+j] = (v[i+j] != mask[j]);
			}
		bool done = true;
		for( int i = 0; i < s.length(); i++)
			if(!v[i])
				done = false;
		cout << "Case #" << Case++ << ": ";
		if( done)
			cout << flips << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}