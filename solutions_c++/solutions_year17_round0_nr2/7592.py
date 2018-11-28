#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int Case = 1, index = 1;

vector<int> number;

void makeNumber(long long n)
{
	number.clear();

	stack<int> s;

	while (n != 0)
	{
		s.push(n % 10);

		n /= 10;
	}

	while (!s.empty())
	{
		number.push_back(s.top());

		s.pop();
	}
}

void printAnswer()
{
	int start = 0;

	while (number[start] == 0)
	{
		start++;
	}

	cout << "Case #" << Case++ << ": ";

	for (int i = start; i < number.size(); i++)
	{
		cout << number[i];
	}

	cout << endl;
}

bool isSafe()
{
	index = 1;

	bool ok = true;

	for (int i = 1; i < number.size() && ok; i++)
	{
		if (number[i] < number[i - 1] || number[i] == 0)
		{
			ok = false;

			index = i;
		}
	}

	return ok;
}

void fixNumber()
{
	while (true)
	{
		if (!isSafe())
		{
			for (int i = index; i < number.size(); i++)
			{
				number[i] = 9;
			}

			number[index - 1] = (number[index - 1] - 1);
		}

		else
		{
			printAnswer();

			break;
		}
	}
}

int main()
{
	int test;

	cin >> test;

	long long n;

	while (test--)
	{
		cin >> n;

		makeNumber(n);

		fixNumber();
	}
}