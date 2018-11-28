#include <iostream>

using namespace std;

int t;
char s[1005];
int k;
int size_s;
int result;

char flip_c(char c)
{
	return c == '+' ? '-' : '+';
}

void flip(int begin)
{
	for (int i = begin; i < begin + k; i++)
	{
		s[i] = flip_c(s[i]);
	}
	result++;
}

void parse_input()
{
	cin >> s >> k;
}

bool algorithm()
{
	result = 0;
	size_s = strlen(s);
	for (int i = 0; i <= size_s - k; i++)
	{
		if (s[i] == '-')
			flip(i);
	}
	for (int i = size_s - k; i < size_s; i++)
	{
		if (s[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	cin >> t;
	for (int i=1; i <=t; i++)
	{
		parse_input();
		if (algorithm())
		{
			cout << "Case #" << i << ": " << result << "\n";
		}
		else
		{
			cout << "Case #" << i << ": IMPOSSIBLE\n";
		}
	}
	return 0;
}