#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	ifstream in("input.txt");

	size_t T;

	in >> T;

	ofstream out("output.txt");

	for (int z = 1; z <= T; ++z)
	{
		string s;
		size_t K;

		in >> s >> K;

		size_t k = 0;
		for (; k < 100 && count(s.begin(), s.end(), '+') != s.size(); ++k)
		{
			size_t best_i = 0, best_cnt = 0;
			for (size_t i = 0; i < s.size() - K; ++i)
			{
				if (s[i] != '-')
					continue;

				auto cnt = count(s.begin() + i, s.begin() + i + K, '-');

				if (cnt > best_cnt)
				{
					best_cnt = cnt;
					best_i = i;
				}
			}

			auto cnt = count(s.end() - K, s.end(), '-');

			if (cnt > best_cnt)
			{
				best_cnt = cnt;
				best_i = s.size() - K;
			}

			for (size_t r = best_i; r < best_i + K; ++r)
				if (s[r] == '+')
					s[r] = '-';
				else
					s[r] = '+';
		}

		out << "Case #" << z << ": " << (k < 100 ? to_string(k) : "IMPOSSIBLE") << "\n";
	}
}