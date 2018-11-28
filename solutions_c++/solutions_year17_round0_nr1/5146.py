#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		string pancakes;
		int K;
		int count, i;

		cin >> pancakes >> K;

		count = 0;

		for (i = 0; i <= pancakes.length() - K; ++i)
		{
			if (pancakes[i] == '-')
			{
				for (int j = i; j < i + K; ++j)
				{
					pancakes[j] = pancakes[j] == '-' ? '+' : '-';
				}

				++count;
			}
		}

		for (; i < pancakes.length(); ++i)
		{
			if (pancakes[i] == '-')
			{
				cout << "Case #" << t << ": IMPOSSIBLE" << endl;
				break;
			}
		}

		if(i == pancakes.length())
			cout << "Case #" << t << ": " << count << endl;
	}

	return 0;
}