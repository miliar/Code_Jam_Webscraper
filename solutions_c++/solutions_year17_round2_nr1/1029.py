#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (size_t i = 0; i < T; ++i)
	{
		size_t D, N;
		in >> D >> N;

		double v = std::numeric_limits<double>::max();
		for (size_t j = 0; j < N; ++j)
		{
			double di, vi;
			in >> di >> vi;
			v = std::min(v, vi*D / (D - di));
		}

		

	    if (i > 0)
			out << endl;
		out << "Case #" << i+1 << ": " << setprecision(6) << fixed << v;
	}

	in.close();
	out.close();
	return 0;
}