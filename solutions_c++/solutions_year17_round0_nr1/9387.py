#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

class OversizedPancakeFlipper
{
public:
	int calc(string s, int K) 
	{
		int flips = 0;
		const auto len = s.length();
		for(;;)
		{
			auto pos = s.find_first_of('-');
			if (pos == string::npos)
			{
				break;
			}
			else if (pos + K > len)
			{
				return -1;
			}
			for (int i = 0; i < K; ++i)
			{
				if (s[pos+i] == '-')
					s[pos+i] = '+';
				else
					s[pos+i] = '-';
			}
			++flips;
			if (pos + K == len)
			{
				return s.find_first_of('-') == string::npos ?  flips : -1;
			}
		}
		return flips;
	}
};

int main()
{
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		string s;
		cin >> s;

		int K;
		cin >> K;

		OversizedPancakeFlipper opf;
		int flips = opf.calc(s, K);
		if (flips >= 0)
		{
			cout << "Case #" << t + 1 << ": " << flips << endl;
		}
		else
		{
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
