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

uint64 n, k;
uint64 a, b;

void clc()
{
	map<uint64, uint64, greater<uint64>> v;
	uint64 c = 0;

	v[n] = 1;
	while (c < k)
	{
		auto it = v.begin();

		a = it->first / 2;
		b = it->first ? (it->first - 1) / 2 : 0;

		if (c + it->second >= k)
			break;

		c += it->second;

		v[a] += it->second;
		v[b] += it->second;

		v.erase(it);
	}
}

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		cin >> n >> k;
		clc();

		cout << "Case #" << cs << ": " << a << ' ' << b << '\n';
	}

	return 0;
}
