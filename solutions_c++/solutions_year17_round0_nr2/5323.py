#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, l, j, last_bigger;
	bool flag;
	string n;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n;
		l = n.size();
		if (l != 1)
		{
			last_bigger = 0;
			for (j = 1; j < l; j++)
				if (n[j] >= n[j - 1])
					last_bigger = j;
				else
					break;
			flag = false;
			for (j = 1; j < l; j++)
				if (n[j] != n[j - 1])
					flag = true;
			if (flag && last_bigger < l - 1)
			{
				while (last_bigger > 0 && n[last_bigger] == n[last_bigger - 1])
					last_bigger--;
				n[last_bigger]--;
				for (j = last_bigger + 1; j < l; j++)
					n[j] = '9';
				if (n[0] == '0')
					n.erase(0, 1);
			}
		}
		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}
