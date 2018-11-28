#include <bits/stdc++.h>

using namespace std;

vector <int> digits;
vector <int> after;

void count(long long n)
{
	if (n == 0)
	{
		digits.push_back(0);
		return;
	}
	while (n != 0)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	reverse(digits.begin(), digits.end());
}

long long collect()
{
	long long now = 0;
	for (size_t i = 0; i < after.size(); i++)
	{
		now *= 10;
		now += after[i];
	}
	return now;
}

int main()
{
	//freopen("input", "r", stdin);
	
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		digits.clear();
		after.clear();
		long long n;
		cin >> n;
		count(n);
		size_t prev = 0;
		int cnt = 1;
		bool truth = false;
		for (size_t i = 1; i < digits.size(); i++)
		{
			if (digits[prev] > digits[i])
			{
				after.push_back(digits[prev] - 1);
				for (size_t j = prev + 1; j < digits.size(); j++)
				{
					after.push_back(9);
				}
				truth = true;
				break;
			}
			if (digits[prev] == digits[i])
			{
				cnt++;
			}
			else if (digits[prev] < digits[i])
			{
				for (int j = 0; j < cnt; j++)
				{
					after.push_back(digits[prev]);
				}
				prev = i;
				cnt = 1;
			}
		}
		if (!truth)
		{
			for (int j = 0; j < cnt; j++)
			{
				after.push_back(digits[prev]);
			}
		}
		cout << "Case #" << i + 1 << ": " << collect() << endl;
	}	
	return 0;
}
