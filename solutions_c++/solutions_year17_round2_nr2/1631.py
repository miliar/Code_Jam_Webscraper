#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
#include <bitset>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(ll i = 0; i<(int)N; i++)
#define fornj(N)         for(ll j = 0; j<(int)N; j++)
#define fornk(N)         for(ll k = 0; k<(int)N; k++)
#define forn1(N)          for(ll i = 1; i<=(int)N; i++)
#define fornj1(N)         for(ll j = 1; j<=(int)N; j++)
#define fornk1(N)         for(ll k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
#define File "fileName"

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

#define log2BitApproximate(S) ((int)(log((double)S) / log(2.0)))
#define log2Bit(S) (1 << (log2BitApproximate(S) + 1) > S ? log2BitApproximate(S) : log2BitApproximate(S) + 1)
#define highBit(S) (isPowerOfTwo(S) ? S : 1 << log2Bit(S))

#define modulo(S, N) ((S) & (N - 1))   // returns S % N, where N is a power of 2
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

using namespace std;

const ll MOD = 1000000007;
const double EPS = 1e-6;

int main()

{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int t;
	cin >> t;

	for (int u = 0; u < t; ++u)
	{
		int n,r,o,y,g,b,vv;
		cin >> n >> r >> o >> y >> g >> b >> vv;

		int colors[3];
		char colChar[3];
		colChar[0] = 'R';
		colChar[1] = 'Y';
		colChar[2] = 'B';
		colors[0] = r;
		colors[1] = y;
		colors[2] = b;

		int mini = 0;
		int other1 = -1;
		int other2 = -1;
		int minv = INT_MAX;

		forn(3)
		{
			if (colors[i] < minv)
			{
				minv = colors[i];
				mini = i;
			}
		}

		forn(3)
		{
			if (i != mini)
			{
				if (other1 == -1)
					other1 = i;
				else
					other2 = i;
			}
		}

		cout << "Case #" << u + 1 << ": ";

		if (minv == 0)
		{
			if (colors[other1] != colors[other2])
				cout << "IMPOSSIBLE" << endl;
			else
			{
				while (colors[other1])
				{
					colors[other1]--;
					cout << colChar[other1] << colChar[other2];
				}
				cout << endl;
			}
		}
		else
		{
			v<char> ans;

			bool isPos = true;
			while (minv)
			{
				ans.push_back(colChar[mini]);
				minv--;
				if (colors[other1] >= colors[other2])
				{
					ans.push_back(colChar[other1]);
					colors[other1]--;
				}
				else
				{
					ans.push_back(colChar[other2]);
					colors[other2]--;
				}
			}

			while (colors[other1] || colors[other2])
			{
				if (ans[ans.size() - 1] == colChar[other1])
				{
					if (colors[other2] > 0)
					{
						ans.push_back(colChar[other2]);
						colors[other2]--;
					}
					else
					{
						isPos = false;
						break;
					}
				}
				else
				{
					if (colors[other1] > 0)
					{
						ans.push_back(colChar[other1]);
						colors[other1]--;
					}
					else
					{
						isPos = false;
						break;
					}
				}
			}

			if (isPos)
			{
				forn(ans.size())
					cout << ans[i];
				cout << endl;
			} 
			else
			{
				cout << "IMPOSSIBLE" << endl;
			}
		}
	}
	
	return 0;
}