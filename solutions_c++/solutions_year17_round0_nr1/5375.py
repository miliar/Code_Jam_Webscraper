#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		string s;
		int k, count = 0;
		cin >> s >> k;
		for (int i = 0; i < s.size() - k + 1; i++)
			if (s[i] == '-')
			{
				count++;
				for (int j = 0; j < k; j++)
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
			}
		bool flag = true;
		for (int i = s.size() - k + 1; i < s.size(); i++)
			if (s[i] == '-')
				flag = false;
		if (flag)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
		
