#include<iostream>
#include<string>
using namespace std;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int testCase;
	cin >> testCase;

	for (int i = 0; i < testCase; i++)
	{
		string str;
		int s;

		cin >> str;
		cin >> s;

		int cnt = 0;
		
		for (int j = 0; j <= str.length() - s; j++)
		{
			if (str[j] == '-')
			{
				cnt++;
				for (int k = 0; k < s; k++)
					if (str[j + k] == '+') str[j + k] = '-';
					else str[j + k] = '+';
			}
		}


		for (int j = 0; j < str.length() ; j++)
			if (str[j] == '-')
				cnt = -1;

		cout << "Case #" << i + 1 << ": "  ;
		if (cnt == -1)
			cout << "IMPOSSIBLE" << '\n';
		else
			cout << cnt << '\n';
	}

}

