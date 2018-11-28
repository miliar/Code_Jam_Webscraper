#include <iostream>
#include <vector>
#include <string>
#include <deque>
using namespace std;

typedef long long ll;
bool checkSorted(ll n)
{
	int cur = n % 10;
	n /= 10;
	while (n)
	{
		if (cur < n % 10)
		{
			return false;
		}
		cur = n % 10;
		n /= 10;
	}
	return true;
}
bool checkSorted(deque<int> &d)
{
	if (d.size() == 1)
	{
		return true;
	}
	for (int i = d.size() - 1; i > 0; --i)
	{
		if (d[i] < d[i - 1])
			return false;
	}
	
	return true;
}


int main()
{
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		long long n;
		cin >> n;
		string str = to_string(n);
		int length = str.length();
		deque<int> d;
		for (int i = 0; i < length; ++i)
		{
			d.push_back(str[i] - '0');
		}
		if (checkSorted(d))
		{
			cout << "Case #" << k << ": ";
			cout << n << endl;
			continue;
		}
		int i = length - 1;
		while (!checkSorted(d))
		{

			d[i] = 9;
			d[i - 1]--;
			i--;

		}
		bool leadZer = false;
		i = 0;
		while (i < d.size() && d[i] == 0)
		{
			i++;
		}
		cout << "Case #" << k << ": ";
		for (; i < d.size(); ++i)
		{
			cout << d[i];
		}
		cout << endl;
	}
}