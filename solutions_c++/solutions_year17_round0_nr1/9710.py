#include <iostream>
#include <string>
#include <list>
using namespace std;

bool check(string str)
{
	bool f = true;
	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] == '-')
		{
			f = false;
		}
	}
	return f;
}

void swap(string &str, int s, int K)
{
	for (int i = s; i < s + K; i++)
	{
		if (str[i] == '+')
		{
			str[i] = '-';
		}
		else
		{
			str[i] = '+';
		}
	}
}

int main()
{
	int T, K, count = 0;
	string str;
	cin >> T;
	list<int> lis;

	for (int i = 0; i < T; i++)
	{
		count = 0;
		cin >> str >> K;
		for (int f = 0; f < str.length(); f++)
		{
			if (f + K <= str.length())
			{
				if (str[f] == '-')
				{
					swap(str, f, K);
					count++;
				}
			}
		}
		if (check(str))
		{
			lis.push_back(count);
		}
		else
		{
			lis.push_back(-1);
		}
	}
	int i = 1;
	for (list<int>::iterator it = lis.begin(); it != lis.end(); ++it)
	{
		cout << "Case #" << i << ": ";
		i++;
		if (*it == -1)
			cout << "IMPOSSIBLE";
		else
			cout << *it;
		cout << endl;
	}
	return 0;
}