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

uint64 n, m;

char v[100][101],
     r[100][101];

struct ddf
{
	uint r[100],
		 c[100],
		 d[200],
		 b[200];
};

ddf ad[3];

bool isp(uint i, uint j)
{
	uint64 cd = n - 1 + j - i,
		   bd = i + j;

	if (ad[0].d[cd] || ad[2].d[cd] || ad[0].b[bd] || ad[2].b[bd])
		return false;

	return true;
}

bool isx(uint i, uint j)
{
	if (ad[1].r[i] || ad[1].c[j] || ad[2].r[i] || ad[2].c[j])
		return false;
	return true;
}

void add(uint q, uint i, uint j)
{
	++ad[q].r[i];
	++ad[q].c[j];
	++ad[q].b[i + j];
	++ad[q].d[n - 1 + j - i];
}

void rem(uint q, uint i, uint j)
{
	--ad[q].r[i];
	--ad[q].c[j];
	--ad[q].b[i + j];
	--ad[q].d[n - 1 + j - i];
}

void rplo(uint i, uint j)
{
	if (r[i][j] == 'x')
		rem(1, i, j);
	else
		rem(0, i, j);

	add(2, i, j);
	r[i][j] = 'o';
}

bool isco(uint i, uint j)
{
	uint64 cd = n - 1 + j - i,
		   bd = i + j;

	if (ad[2].r[i] || ad[2].c[j] || ad[2].d[cd] || ad[2].b[bd])
		return false;

	uint qi = r[i][j] == '+' ? 0 : 1;

	rem(qi, i, j);
	add(2, i, j);
	if (ad[1].r[i] || ad[1].c[j] || ad[0].d[cd] || ad[0].b[bd])
	{
		rem(2, i, j);
		add(qi, i, j);
		return false;
	}
	rem(2, i, j);
	add(qi, i, j);

	return true;
}

uint s;

struct rpl
{
	uint i, j;
	char c;
};

rpl z[10000];
uint nz;

void print()
{
	for (uint i = 0; i < n; ++i)
		cout << r[i] << '\n';
}

struct pps
{
	uint i, j, d, t;

	void getdtp()
	{
		d = t = 0;
		uint ci = i, cj = j;
		for (; ci > 0 && cj > 0; --ci, --cj);

		for (; ci < n && cj < n; ++ci, ++cj)
		{
			++d;
			if (ad[0].d[n - 1 + cj - ci] || ad[0].b[ci + cj] ||
				ad[2].d[n - 1 + cj - ci] || ad[2].b[ci + cj])
				++t;
		}

		ci = i, cj = j;
		for (; ci > 0 && cj < n; --ci, ++cj);

		for (; ci < n && cj != -1; ++ci, --cj)
		{
			++d;
			if (ad[0].d[n - 1 + cj - ci] || ad[0].b[ci + cj] ||
				ad[2].d[n - 1 + cj - ci] || ad[2].b[ci + cj])
				++t;
		}
	}

	void getdtx()
	{
		d = t = 0;

		for (uint ci = 0; ci < n; ++ci)
		{
			++d;
			if (ad[1].r[ci] || ad[2].r[ci] || ad[1].c[ci] || ad[2].c[ci])
				++t;
		}
	}
};

pps lz;
void getlp()
{
	lz.d = -1;

	for (uint i = 0; i < n; ++i)
	{
		for (uint j = 0; j < n; ++j)
		{
			if (r[i][j] == '.' && ad[0].d[n - 1 + j - i] == 0 && ad[0].b[i + j] == 0 &&
				ad[2].d[n - 1 + j - i] == 0 && ad[2].b[i + j] == 0)
			{
				pps zz;
				zz.i = i, zz.j = j;
				zz.getdtp();

				if (lz.d > zz.d || lz.d == zz.d && lz.t < zz.t)
					lz = zz;
			}
		}
	}
}

void getlx()
{
	lz.d = -1;

	for (uint i = 0; i < n; ++i)
	{
		for (uint j = 0; j < n; ++j)
		{
			if (r[i][j] == '.' && ad[1].r[i] == 0 && ad[1].c[j] == 0 &&
				ad[2].r[i] == 0 && ad[2].c[j] == 0)
			{
				pps zz;
				zz.i = i, zz.j = j;
				zz.getdtx();

				if (lz.d > zz.d || lz.d == zz.d && lz.t < zz.t)
					lz = zz;
			}
		}
	}
}

void vclc()
{
	s = 0;
	nz = 0;
	for (uint i = 0; i < n; ++i)
	{
		for (uint j = 0; j < n; ++j)
		{
			if (r[i][j] != '.' && r[i][j] != 'o' && isco(i, j))
				rplo(i, j);

			if (r[i][j] != '.')
				++s;
			if (r[i][j] == 'o')
				++s;

			if (r[i][j] != v[i][j])
			{
				z[nz].i = i;
				z[nz].j = j;
				z[nz].c = r[i][j];
				++nz;
			}
		}
	}
}

void clc()
{
	lz.d = 0;
	while (lz.d != -1)
	{
		getlp();
		if (lz.d != -1)
		{
			r[lz.i][lz.j] = '+';
			add(0, lz.i, lz.j);
		}
	}

	lz.d = 0;
	while (lz.d != -1)
	{
		getlx();
		if (lz.d != -1)
		{
			r[lz.i][lz.j] = 'x';
			add(1, lz.i, lz.j);
		}
	}

	//print();
	vclc();

	//print();
}

void clr()
{
	uint64 nn = n + n - 1;
	for (uint i = 0; i < 3; ++i)
	{
		fill(ad[i].r, ad[i].r + n, 0);
		fill(ad[i].c, ad[i].c + n, 0);
		fill(ad[i].d, ad[i].d + nn, 0);
		fill(ad[i].b, ad[i].b + nn, 0);
	}
}

bool test()
{
	for (uint i = 0; i < n; ++i)
	{
		if (ad[1].r[i] + ad[2].r[i] > 1 || ad[1].c[i] + ad[2].c[i] > 1)
			return false;
	}

	for (uint i = 0; i < n + n - 1; ++i)
	{
		if (ad[0].d[i] + ad[2].d[i] > 1 || ad[0].b[i] + ad[2].b[i] > 1)
			return false;
	}

	return true;
}

void initr()
{
	clr();
	for (uint i = 0; i < n; ++i)
	{
		for (uint j = 0; j < n; ++j)
		{
			r[i][j] = v[i][j];
			if (r[i][j] == 'x')
				add(1, i, j);
			else if (r[i][j] == '+')
				add(0, i, j);
			else if (r[i][j] == 'o')
				add(2, i, j);
		}
	}
}

int main(int argc, char* argv[])
{
	uint64 cases;
	cin >> cases;

	for (uint64 cs = 1; cs <= cases; ++cs)
	{
		cin >> n >> m;
		for (uint i = 0; i < n; ++i)
		{
			fill(v[i], v[i] + n, '.');
			v[i][n] = 0;
		}

		for (uint i = 0; i < m; ++i)
		{
			char c;
			uint cr, cc;
			cin >> c >> cr >> cc;
			--cr, --cc;
			v[cr][cc] = c;
		}

		initr();
		clc();

//		if (!test())
//			break;

		cout << "Case #" << cs << ": " << s << ' ' << nz << '\n';
		//print();
		for (uint i = 0; i < nz; ++i)
			cout << z[i].c << ' ' << z[i].i + 1 << ' ' << z[i].j + 1 << '\n';
	}

	return 0;
}
