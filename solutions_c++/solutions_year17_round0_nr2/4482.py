#include <iostream>

using namespace std;

int work(int numbers[])
{
	char data[30];
	cin >> data;

	int lastIndex = 0;
	while (data[lastIndex] != 0)
		lastIndex++;

	for (int n = 0; n < lastIndex; ++n)
	{
		numbers[n] = data[n] - '0';
	}

	for (int n = lastIndex - 2; n >= 0; --n)
	{
		if (numbers[n] > numbers[n + 1])
		{
			if (n == 0)
			{
				numbers[0] = numbers[0] - 1;
				for (int k = 1; k < lastIndex; ++k)
				{
					numbers[k] = 9;
				}
			}
			else
			{
				//numbers[n] = numbers[n + 1];
				numbers[n] = numbers[n] - 1;
				for (int k = n + 1; k < lastIndex; ++k)
				{
					numbers[k] = 9;
				}
			}
		}
	}

	return lastIndex;
}

void main()
{
	cin.tie(nullptr);
	ios_base::sync_with_stdio(false);

	int cases;
	cin >> cases;

	for (int n = 0; n < cases; ++n)
	{
		int numbers[30];
		int size = work(numbers);

		cout << "Case #" << n + 1 << ": ";

		bool leading = true;
		for (int k = 0; k < size; ++k)
		{
			if (leading && numbers[k] == 0)
				continue;

			leading = false;
			cout << numbers[k];
		}
		cout << endl;
	}
}