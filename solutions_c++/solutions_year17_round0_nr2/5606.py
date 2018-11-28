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
		size_t N;

		in >> N;

		auto str = to_string(N);

		while (!is_sorted(str.begin(), str.end()))
		{
			for (size_t i = str.size() - 1; i > 0; --i)
			{
				if (str[i - 1] > str[i])
				{
					--str[i - 1];
					str[i] = '9';

					for (size_t j = i; j < str.size(); ++j)
						str[j] = '9';
				}
			}
		}

		out << "Case #" << z << ": " << to_string(stoll(str)) << "\n";
	}
}