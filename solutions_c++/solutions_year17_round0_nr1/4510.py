#include <iostream>

using namespace std;

int work()
{
	char data[1005];
	cin >> data;

	int dataSize = 0;
	while (data[dataSize] != 0)
		dataSize++;

	int flipSize;
	cin >> flipSize;

	int flips = 0;

	for (int n = 0; n <= dataSize - flipSize; ++n)
	{
		if (data[n] != '+')
		{
			++flips;

			for (int k = 0; k < flipSize; ++k)
			{
				if (data[n + k] == '+')
				{
					data[n + k] = '-';
				}
				else
				{
					data[n + k] = '+';
				}
			}
		}
	}

	for (int n = dataSize - flipSize + 1; n < dataSize; ++n)
	{
		if (data[n] != '+')
		{
			return -1;
		}
	}

	return flips;
}

void main()
{
	cin.tie(nullptr);
	ios_base::sync_with_stdio(false);

	int cases;
	cin >> cases;

	for (int n = 0; n < cases; ++n)
	{
		int result = work();

		if (result >= 0)
		{
			cout << "Case #" << n + 1 << ": " << result << endl;
		}
		else
		{
			cout << "Case #" << n + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
}