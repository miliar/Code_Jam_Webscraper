#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <deque>
#include <fstream>
using namespace std;

void dec(deque<int>& arr, int pos)
{
	arr[pos]--;
	if (arr[pos] == -1)
	{
		arr[pos] = 9;
		dec(arr, pos - 1);
	}
}
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("out.txt");

	int t;
	cin >> t;

	for (int f = 0; f < t; ++f)
	{
		deque<int> num;
		long long c;
		cin >> c;

		while (c != 0)
		{
			num.push_front(c % 10);
			c /= 10;
		}

		for (int i = num.size() - 1; i > 0; --i)
		{
			if (num[i - 1] > num[i])
			{
				dec(num, i - 1);
				for (int j = i; j < num.size(); ++j)
					num[j] = 9;
			}
		}

		while (num[0] == 0)
			num.pop_front();

		cout << "Case #" << f + 1 << ": ";
		for (auto v : num)
			cout << v;
		cout << endl;
	}


	return 0;
}