#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int R, C;
		cin >> R >> C;
		vector <string> s (R);
		for (int i = 0; i < R; ++ i)
		{
			cin >> s[i];
			}
		
		int first = -1;

		for (int i = 0; i < R && first < 0; ++ i)
		{
			for (int j = 0; j < C; ++j)
				if (s[i][j] != '?')
				{
					first = i;
					break;
				}
		}
		
		for (int i = 0; i < first; ++i)
			s[i] = s[first];
			
		
		for (int i = first+1; i < R; ++i)
		{
			bool empty = true;
			for (int j = 0; j < C; ++j)
			{
				
				if (s[i][j] != '?')
				{
					empty = false;
					break;
				}
			}
			if (empty) s[i] = s[i-1];
		}
		
		for (int i = 0; i < R; ++ i)
		{
			int first_char = 0;
			for (int j = 0; j < C; ++ j)
				if (s[i][j] != '?')
				{
					first_char = j;
					break;
				}
			for (int j = 0; j < first_char; ++ j)
				s[i][j] = s[i][first_char];
		}
		
		for (int i = 0; i < R; ++ i)
		{
			for (int j = 1; j < C; ++ j)
				if (s[i][j] == '?')
				{
					s[i][j] = s[i][j-1];
				}
		}
		
		cout << "Case #" << t+1 << ": " << endl;
		for (int i = 0; i < R; ++ i)
		{
			cout << s[i] << endl;
		}
	}

}