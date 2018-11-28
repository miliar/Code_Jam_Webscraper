#include <iostream>
#include <string>
using namespace std;

bool all_happy(string &s);
int num_of_flip(string &s, int k);

int main()
{
	int T, K, x, y;//T: test case, K: size of pancake flipper
	string S;

	cin >> T;
	for (x = 1; x <= T; x++)
	{
		cin >> S >> K;
		y = num_of_flip(S, K);
		if (y == -1)cout << "Case #" << x << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << x << ": " << y << endl;
	}
	return 0;
}

bool all_happy(string &s)
{
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == '-')return false;
	}
	return true;
}

int num_of_flip(string &s, int k)
{
	//-1: represent impossible to make all happy side
	int count = 0;
	//int num = num_of_blank_side(s);
	if (all_happy(s) == true) count = 0;
	else if (s.length() < k)count = -1;
	else
	{
		for (int i = 0; i < s.length() - k + 1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-')s[j] = '+';
					else if (s[j] == '+')s[j] = '-';
				}
				count++;
			}
		}
		if (all_happy(s) == false)count = -1;
	}
	return count;
}