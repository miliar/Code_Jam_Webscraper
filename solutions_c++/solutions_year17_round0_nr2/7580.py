#include <iostream>
#include <string>
using namespace std;

int main()
{
	string n;
	int t, count = 0;
	int cur_digit = 0;
	bool isTidy = true;
	int a[1001];
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		count = 0;
		cur_digit = 0;
		isTidy = true;
		cin >> n;
		cout << "Case #" << i << ": ";
		for (int j = 0; j < n.length(); j++)
			a[j] = n[j] - 48;

		for (int j = 0; j < n.length(); j++)
		{
			if (a[j] > cur_digit)
			{
				count = 0;
				cur_digit = a[j];
			}

			if (a[j] == cur_digit)
			{
				count++;
			}

			if (a[j] < cur_digit)
			{
				isTidy = false;
				if (cur_digit == 1)
				{
					for (int k = 0; k < n.length() - 1; k++)
						cout << 9;
				}
				else
				{

					for (int k = j - count + 1; k < n.length(); k++)
						a[k] = 9;

					a[j - count]--;

					for (int k = 0; k < n.length(); k++)
						cout << a[k];
				}
				break;
			}
		}

		if (isTidy)
			cout << n;

		cout << endl;
	}
	return 0;
}