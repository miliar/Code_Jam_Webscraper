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

double p[50];

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		uint n, k;
		double u;
		cin >> n >> k >> u;

		for (uint i = 0; i < n; ++i)
			cin >> p[i];

		sort(p, p + n);

		double cd = 0;
		uint ci = 0;
		for (uint i = 0; i < n - 1; ++i)
		{
			cd += (i + 1) * (p[i + 1] - p[i]);
			if (cd > u)
			{
				ci = i + 1;
				break;
			}
		}

		if (cd < u)
			ci = n;

		double ap = u;
		for (uint i = 0; i < ci; ++i)
			ap += p[i];

		ap /= ci;

		for (uint i = 0; i < ci; ++i)
			p[i] = ap;

		double r = 1.;
		for (uint i = 0; i < n; ++i)
			r *= p[i];

		cout << "Case #" << cs << ": " << fixed << setprecision(9) << r << '\n';
	}

	return 0;
}
