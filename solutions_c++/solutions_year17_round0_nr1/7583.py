#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	int t, k, count;
	bool a[1001];
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		count = 0;		
		cin >> s;
		cin >> k;
		for (int j = 0; j < s.length(); j++)
			a[j] = s[j] == '+' ? true : false;

		for (int j = 0; j < s.length() - k + 1; j++)
			if (!a[j])
			{
				for (int l = j; l < j + k; l++)
					a[l] = !a[l];
				count++;
			}

		for (int j = s.length() - k + 1; j < s.length(); j++)
			if (!a[j])
			{
				count = -1;
				break;
			}

		cout << "Case #" << i << ": ";
		if (count == -1)
			cout << "IMPOSSIBLE";
		else
			cout << count;
		cout << endl;
	}
	return 0;
}