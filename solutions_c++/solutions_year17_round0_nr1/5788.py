#include <bits/stdc++.h>

using namespace std;

void flip(string &s, const int k, const int start)
{
	for(int i = 0; i < k; i++)
	{
		s[start + i] = (s[start + i] == '+') ? '-' : '+';
	}
}

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;

		int flip_count = 0;
		int last_i = s.length() - k + 1;
		for(int i = 0; i < last_i; i++)
		{
			if(s[i] == '-')
			{
				flip_count++;
				flip(s, k, i);
			}
		}
		for(int i = last_i; i < s.length(); i++)
		{
			if(s[i] == '-')
			{
				flip_count = -1;
				break;
			}
		}

		if(flip_count == -1)
			cout << "Case #" << t << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << t << ": " << flip_count << "\n";
	}

	return 0;
}

