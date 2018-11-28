#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	fstream fs("a.in");
	int t;
	fs >> t;
	vector<unsigned long long> input;
	for (int i = 0; i < t; ++i)
	{
		unsigned long long n;
		fs >> n;
		input.push_back(n);
	}

	


	for (int i = 0; i < input.size(); ++i)
	{
		stringstream ss;
		ss << input[i];
		string s = ss.str();

		bool need = false;
		char p = s[0];
		for (int j = 0; j < s.size(); ++j)
		{
			if (s[j] < p)
				need = true;
			p = s[j];
		}

		if (need)
		{
			int goodind = 0;
			char prev = s.back();
			for (int j = s.size() - 1; j >= 0; --j)
			{
				if (s[j] >= prev)
				{
					goodind = j;
				}
				prev = s[j];
			}
			if (goodind != s.size() - 1)
			{
				s[goodind] -= 1;
				for (int j = goodind + 1; j < s.size(); j++)
				{
					s[j] = '9';
				}
			}
		}
		unsigned long long res = atoll(s.c_str());
		std::cout << "Case #" << i + 1 << ": " << res << endl;
	}
	int f;
	cin >> f;

	return 0;
}