#include <iostream>
#include <string>

using namespace std;

void main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		string N;
		cin >> N;

		for (size_t i = 0; i < N.size() - 1; ++i)
		{
			if (N[i] > N[i + 1])
			{
				--N[i];
				while (i != 0 && N[i - 1] > N[i])
				{
					--i;
					--N[i];
				}
				for (auto j = i + 1; j < N.size(); ++j)
				{
					N[j] = '9';
				}
				break;
			}
		}

		N.erase(0, N.find_first_not_of('0'));

		cout << "Case #" << t + 1 << ": " << N << endl;
	}
}
