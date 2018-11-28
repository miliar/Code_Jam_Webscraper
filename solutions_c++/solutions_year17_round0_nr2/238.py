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

char s[20];

void clc()
{
	char p = s[0];

	uint i = 0;
	while (s[i] && s[i] >= p)
	{
		p = s[i];
		++i;
	}

	if (s[i])
	{
		--i;
		while (i > 0)
		{
			if (s[i] <= s[i - 1])
				--i;
			else
				break;
		}

		--s[i];
		for (++i; s[i]; ++i)
			s[i] = '9';
	}
}

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		cin >> s;
		clc();

		uint i = 0;
		while (s[i] == '0')
			++i;

		cout << "Case #" << cs << ": " << s + i << '\n';
	}

	return 0;
}
