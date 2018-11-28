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

char a[26][26];

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		uint r, c;
		cin >> r >> c;

		for (uint i = 0; i < r; ++i)
		{
			cin >> a[i];
			char z = 0;
			for (uint j = 0; j < c; ++j)
			{
				if (a[i][j] != '?')
					z = a[i][j];

				if (a[i][j] == '?' && z)
					a[i][j] = z;
			}

			z = 0;
			for (uint j = c - 1; j != -1; --j)
			{
				if (a[i][j] != '?')
					z = a[i][j];

				if (a[i][j] == '?' && z)
					a[i][j] = z;
			}
		}

		bool go = true;
		while (go)
		{
			go = false;
			for (uint i = 0; i < r; ++i)
			{
				if (a[i][0] != '?')
				{
					if (i > 0 && a[i - 1][0] == '?')
					{
						go = true;
						for (uint j = 0; j < c; ++j)
							a[i - 1][j] = a[i][j];
					}

					if (i < r - 1 && a[i + 1][0] == '?')
					{
						go = true;
						for (uint j = 0; j < c; ++j)
							a[i + 1][j] = a[i][j];
					}
				}
			}
		}

		cout << "Case #" << cs << ": " << '\n';
		for (uint i = 0; i < r; ++i)
			cout << a[i] << '\n';
	}

	return 0;
}
