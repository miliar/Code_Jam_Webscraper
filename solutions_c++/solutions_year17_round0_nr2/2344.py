#include<iostream>
#include<fstream>

using namespace std;

#define N 19

static char num[N];

bool is_tidy(int len)
{
	int i;
	bool result = true;

	for (i = len - 1; i > 0; i--)
	{
		if (num[i] > num[i - 1])
		{
			result = false;
			break;
		}
	}

	if (!result)
	{
		num[i--]--;
		for (; i >= 0; i--)
		{
			num[i] = '9';
		}
	}

	return result;
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;

	cin >> T;
	for (int test_case = 0; test_case < T; test_case++)
	{
		unsigned long long number;
		int digits = 0, i = 0, len;

		cin >> number;
		
		while (number != 0)
		{
			num[i] = (char)(number % 10) + '0';
			number /= 10;
			i++;
		}
		len = i;

		while (!is_tidy(len));

		cout << "Case #" << test_case + 1 << ": ";
		for (i = len - 1; i >= 0; i--)
		{
			if (num[i] != '0') cout << num[i];
		}
		cout << endl;
	}
}