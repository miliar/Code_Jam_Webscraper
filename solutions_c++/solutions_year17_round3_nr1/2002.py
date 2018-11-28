// gj.cpp
//

#include <assert.h>

#include <fstream>
#include <sstream>
#include <stack>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

#define EPS (1E-10)
#define PI 3.1415926535897932384626433832795

pair<uint64, uint64> ph[1000];

uint z[1000];

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		uint n, k;
		cin >> n >> k;

		for (uint i = 0; i < n; ++i)
		{
			cin >> ph[i].first >> ph[i].second;
			if (i < n - k)
				z[i] = 0;
			else
				z[i] = 1;
		}

		double r = 0;
		do
		{
			double cr = 0;
			uint mx = -1;
			for (uint64 i = 0; i < n; ++i)
			{
				if (z[i])
				{
					if (mx == -1)
						mx = i;
					else if (ph[i].first > ph[mx].first)
						mx = i;
					cr += ph[i].second * ph[i].first * 2;
				}
			}
			cr += ph[mx].first * ph[mx].first;

			if (cr > r)
				r = cr;
		} while (next_permutation(z, z + n));

		cout << "Case #" << cs << ": " << fixed << setprecision(9) << r * PI << '\n';
	}

	return 0;
}
