#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int N;
	in >> N;

	for (size_t i = 0; i < N; ++i)
	{
		string s;
		in >> s;

		for (size_t j = s.length() - 1; j > 0; --j)
		{
			if (s[j] < s[j - 1])
			{
				--s[j-1];
				for (size_t k = j; k < s.length(); ++k)
					s[k] = '9';
			}
		}

		int l = s.find_first_not_of('0');

		if (l > 0)
			s = s.substr(l, s.length() - l);

		if (i > 0)
			out << endl;
		out << "Case #" << i + 1 << ": " << s;
	}

	in.close();
	out.close();
	return 0;
}