#include <string>
#include <iostream>
using namespace std;

bool FNonDecreasing(string s)
{
	for (int i = 1; i < s.length(); ++i)
		if (s[i] < s[i - 1])
			return false;

	return true;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		string N;
		cin >> N;

		string ret;
		
		// check current;
		bool fGood = FNonDecreasing(N);
				
		if (fGood)
			ret = N;
		else
		{
			int pos = -1;
			for (int j = 1; j < N.length(); ++j)
				if (N[j] < N[j - 1])
				{
					pos = j-1;
					break;
				}

			if (N[pos] == '1')
			{
				for (int j = 0; j < N.length() - 1; ++j)
					ret += '9';
			}
			else
			{
				// find the pos to decrement
				string half = N.substr(0, pos + 1);
				half[half.length() - 1] = N[pos] - 1;
				if (FNonDecreasing(half))
				{
					ret = half;

					// append 9
					int count = N.length() - ret.length();
					for (int k = 0; k < count; ++k)
						ret += '9';
				}
				else
				{
					// go back find the first one that is <= N[pos]-1
					int j = half.length() - 2;
					while (j >= 0)
					{
						if (half[j] <= N[pos] - 1)
							break;
						--j;
					}

					if (j == -1)
					{
						ret += N[pos] - 1;
					}
					else
					{
						ret = half.substr(0, j + 1);

						// append N[pos]-1
						for (int k = 0; k < half.length() - j - 1; ++k)
							ret += N[pos] - 1;
					}

					// append 9
					int count = N.length() - ret.length();
					for (int k = 0; k < count; ++k)
						ret += '9';
				}
			}
		}
		
		cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}

