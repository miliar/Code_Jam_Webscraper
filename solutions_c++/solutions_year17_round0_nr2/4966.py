#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T = 3;

	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{

		string s;
		cin >> s;

	
		int n = 0;
		

		for (int i = s.size() - 1; i >= 0; --i)
		{
			int cur = s[i] - '0';
			int prev = i == 0 ? 0 : s[i - 1] - '0';

			cur -= n;
			n = 0;

			if (cur >= prev )
			{
				s[i] = '0' + cur;
			}
			else
			{
				for (int j = i; j < s.size(); ++j)
				{
					s[j] = '9';
				}
				n = 1;
			}
		}


		if ( s[0] == '0')
		{
			s = string(s.size( ) - 1, '9' );
		}

		printf("Case #%d: %s\n", t + 1, s.c_str());

	}

	return 0;
}