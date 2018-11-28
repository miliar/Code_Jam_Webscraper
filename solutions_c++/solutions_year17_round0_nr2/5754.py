#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		string n;
		cin >> n;

		for(int i = n.length() - 1; i > 0; i--)
		{
			auto &left = n[i-1];
			auto &right = n[i];

			if(left > right)
			{
				left -= 1;
				for(int j = i; j < n.length(); j++)
					n[j] = '9';
			}
		}

		if(n[0] == '0')
			n.erase(0, 1);
		cout << "Case #" << t << ": " << n << "\n";
	}
}