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

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

#define EPS (1E-10)
#define PI 3.1415926535897932384626433832795

char s[1001];
uint n;

uint clc()
{
	uint l = strlen(s);
	uint r = 0;
	for (uint i = 0; i + n <= l; ++i)
	{
		if (s[i] == '-')
		{
			for (uint j = 0; j < n; ++j)
				s[i + j] = s[i + j] == '-' ? '+' : '-';

			++r;
		}
	}

	bool ok = true;
	for (uint i = 0; i < l; ++i)
	{
		if (s[i] == '-')
		{
			ok = false;
			break;
		}
	}

	return ok ? r : -1;
}

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		cin >> s >> n;
		uint r = clc();

		if (r == -1)
			cout << "Case #" << cs << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << cs << ": " << r << '\n';
	}

	return 0;
}
