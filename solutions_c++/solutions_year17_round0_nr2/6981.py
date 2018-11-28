#include <iostream>

using namespace std;

int t;
char s[200];
int res[200];
int n;
int res_size;

int digit(char c)
{
	return (int)c - (int)'0';
}

char character(int d)
{
	return (char)(d + (int)'0');
}

void parse_input()
{
	cin >> s;
}

void algorithm()
{
	res_size = strlen(s);
	res[0] = digit(s[0]);
	bool nine_enabled = false;
	for (int i = 1; i < res_size; i++)
	{
		int dig = digit(s[i]);
		if (nine_enabled)
			res[i] = 9;
		else if (dig >= res[i - 1])
			res[i] = dig;
		else
		{
			int k;
			for (k = i - 1; k >= 0 && res[k] == res[i - 1]; k--)
			{

			}
			k++;

			res[k]--;
			i = k + 1;
			res[i] = 9;
			nine_enabled = true;
		}
	}
}

void print_result(int test_case)
{
	cout << "Case #" << test_case << ": ";
	for (int i = 0; i < res_size; i++)
	{
		if (res[i] != 0)
			cout << character(res[i]);
	}
	cout << "\n";
}

int main()
{
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		parse_input();
		algorithm();
		print_result(i);
	}
	return 0;
}