/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////


int main()
{
	//ofstream cout ("Aout.out");
	//ifstream cin ("A.in");
	freopen("B.txt", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	int test;
	int t = 0; 
	cin >> test;
	while(test --)
	{
		int n, r, o, y, g, b, v;
		t++;
		cin >> n >> r >> o >> y >> g >> b >> v;
		bool can = true;
		if (r + y < b)
			can = false;
		if (r + b < y)
			can = false;
		if (y + b < r)
			can = false;
		cout << "Case #" << t << ": ";
		if(can)
		{
			string name;
			for (int i = 0; i < n; i++)
				name += "T";
			if(r >= b && r >= y)
			{
				for (int i = 0; i < r; i++)
					name[i * 2] = 'R';
				if (b > y)
					for (int i = 0; i < b - y; i++)
						name[i * 2 + 1] = 'B';
				else 
					for (int i = 0; i < y - b; i++)
						name[i * 2 + 1] = 'Y';
				for(int i = abs(b - y) ; i < r ; i ++)
				{
					if (i % 2)
						name[2 * i + 1] = 'B';
					else
						name[2 * i + 1] = 'Y';
				}
				for(int i = 2*r ; i < n ; i ++)
				{
					if (name[i - 1] == 'Y')
						name[i] = 'B';
					else
						name[i] = 'Y';
				}
				
			}
			else if(b >= r && b >= y)
			{
				for (int i = 0; i < b; i++)
					name[i * 2] = 'B';

				if (r > y)
					for (int i = 0; i < r - y; i++)
						name[i * 2 + 1] = 'R';
				else
					for (int i = 0; i < y - r; i++)
						name[i * 2 + 1] = 'Y';
				for (int i = abs(r - y); i < b; i++)
				{
					if (i % 2)
						name[2 * i + 1] = 'R';
					else
						name[2 * i + 1] = 'Y';
				}
				for (int i = 2 * b ; i < n; i++)
				{
					if (name[i - 1] == 'Y')
						name[i] = 'R';
					else
						name[i] = 'Y';
				}
			}
			else 
			{
				for (int i = 0; i < y; i++)
					name[i * 2] = 'Y';

				if (b > r)
					for (int i = 0; i < b - r; i++)
						name[i * 2 + 1] = 'B';
				else
					for (int i = 0; i < r - b; i++)
						name[i * 2 + 1] = 'R';
				for (int i = abs(b - r); i < y; i++)
				{
					if (i % 2)
						name[2 * i + 1] = 'B';
					else
						name[2 * i + 1] = 'R';
				}
				for (int i = 2 * y ; i < n; i++)
				{
					if (name[i - 1] == 'R')
						name[i] = 'B';
					else
						name[i] = 'R';
				}
			}

			cout << name << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
