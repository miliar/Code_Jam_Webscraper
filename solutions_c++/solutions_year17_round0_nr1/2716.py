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
		int K;
		int KK = 0;
		in >> s >> K;
		for (int j = 0;K > 0 && j < s.length() - K + 1; ++j)
			if (s[j] == '-')
			{
				++KK;
				for (size_t k = 0; k < K; ++k)
					s[j + k] = (s[j + k] == '+' ? '-' : '+');
			}
		if (i > 0)
			out << endl;
		out << "Case #" << i + 1 << ": ";

		bool isDashHit = false;
		for (size_t j = 0; j < s.length(); ++j)
			if (s[j] == '-')
				isDashHit = true;
		if (isDashHit)
			out << "IMPOSSIBLE";
		else
			out << KK;
	}

	in.close();
	out.close();
	return 0;
}