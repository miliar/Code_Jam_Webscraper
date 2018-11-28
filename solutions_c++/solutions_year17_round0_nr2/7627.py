#include<iostream>
#include<string>
#include<cstring>
using namespace std;


int find_inc_index(char * s, int num_digits)
{
	int i;
	for (i = 0; i < num_digits-1; ++i)
	{
		if (s[i] > s[i + 1])
		{
			break;
		}
	}
	return i;

}

int uneq_index(char *s, int index)
{
	int i = 0;
	for (i = index; i > 0; --i)
	{
		if (s[i] != s[i - 1])
			break;
	}
	return i;
}

int main()
{
	int t = 0;
	int num_digits = 0;
	long long n = 0;
	char s[21];
	int index = 0;

	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		num_digits = 0;
		cin >> n;
		//num_digits = cnt_digits(n);
		sprintf_s(s, "%lld", n);
		num_digits = strlen(s);
		if (num_digits < 2)
		{
			cout << "Case #" << i << ": " << s<<endl;
			continue;
		}
		index = find_inc_index(s, num_digits);
		if (index == num_digits - 1)
		{
			cout << "Case #" << i << ": " << s<<endl;
			continue;
		}
		if (index == 0)
		{
			cout << "Case #" << i << ": ";
			if (s[0] == '1')
			{
				for (int j = 0; j < num_digits - 1; ++j)
				{
					cout << "9";
				}
			}
			else
			{
				s[0] -= 1;
				cout << s[0];
				for (int j = 0; j < num_digits - 1; ++j)
				{
					cout << "9";
				}
			}
			cout << endl;
			continue;
		}
		index = uneq_index(s, index);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < index; ++j)
		{
			cout << s[j];
		}
		if (s[index] != '1')
		{
			s[index] -= 1;
			cout << s[index];
		}
		for (int j = index+1; j < num_digits; ++j)
		{
			cout << "9";
		}
		cout << endl;
		continue;
	}
	return 1;
}