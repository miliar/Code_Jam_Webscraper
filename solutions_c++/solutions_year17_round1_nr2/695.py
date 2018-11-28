// topcoder.cpp : �R���\�[�� �A�v���P�[�V�����̃G���g�� �|�C���g���`���܂��B
//

#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <unordered_map>
#include "assert.h"

using namespace std;

static const double EPS = 1e-9;
template<class T> bool INRANGE(T x,T a,T b){return a<=x&&x<=b || b<=x&&x<=a;}
template<class T> void amin(T &a,T v){if(a>v) a=v;}
template<class T> void amax(T &a,T v){if(a<v) a=v;}
int ROUND(double x) { return (int)(x+0.5); }
bool ISINT(double x) { return fabs(ROUND(x)-x)<=EPS; }
bool ISEQUAL(double x,double y) { return fabs(x-y)<=EPS*max(1.0,max(fabs(x),fabs(y))); }

#define PI  (acos(-1))
#define ARRAY_NUM(a) (sizeof(a)/sizeof(a[0])) 
#define NG (-1)
#define BIG ((int)1e9)
#define BIGLL ((ll)4e18)
#define SZ(a) ((int)(a).size())
#define SQ(a) ((a)*(a))

typedef unsigned long long ull;
typedef long long ll;

ll SQSUM(ll x,ll y) { return x*x+y*y; }

#define PRINTF(fmt,...) fprintf(stderr,fmt,__VA_ARGS__); printf(fmt,__VA_ARGS__);





#if 1


int main() {

	freopen("_google_code_jam_input.txt", "r", stdin);
	freopen("_google_code_jam_output.txt", "w", stdout);

	int T;
	scanf("%d ", &T);


	for (int testcase = 0; testcase < T; ++testcase)
	{
		int N, P;
		cin >> N >> P;

		vector <ll> unit(N);
		for (int i = 0; i < N; ++i)
		{
			cin >> unit[i];
		}

		vector < vector <ll> > quantity(N, vector <ll>(P, 0));
		for (int i = 0; i < N; ++i)
		{
			for (int k = 0; k < P; ++k)
			{
				cin >> quantity[i][k];
			}

			sort(quantity[i].begin(), quantity[i].end());
		}


		ll kit = 1;
		vector <int> cur(N);
		int ret = 0;
		while (kit <= 1000000)
		{
			vector <int> goodCur(N);
			// ����邩�`�F�b�N
			bool ok = true;
			for (int i=0;i<N;i++)
			{
				bool found = false;
				for(int k = cur[i];k<P;k++)
				{
					if (unit[i] * kit * 9 <= quantity[i][k] * 10 && quantity[i][k] * 10 <= unit[i] * kit * 11)
					{
						found = true;
						goodCur[i]=k+1;
						break;
					}
				}

				if (!found)
				{
					ok = false;
					break;
				}
			}

			if(ok)
			{
				ret++;
				cur = goodCur;
			}
			else
			{
				kit++;
			}
		}
	

		PRINTF("Case #%d: %d\n", testcase + 1, ret);
	}

	return 0;
}
#else

int main() {

	freopen("_google_code_jam_input.txt", "r", stdin);
	freopen("_google_code_jam_output.txt", "w", stdout);

	int T;
	scanf("%d ", &T);


	for (int testcase = 0; testcase < T; ++testcase)
	{
		int R,C;

		cin >> R >> C;
		vector <string> vs(R);
		for (int y = 0; y < R; ++y)
		{
			cin >> vs[y];
		}

		for (int y = 0; y < R; ++y)
		{
			for (int x = 0; x < C-1; ++x)
			{
				if (vs[y][x] != '?' && vs[y][x + 1] == '?')
				{
					vs[y][x + 1] = vs[y][x];

				}

			}

			for (int x = C-1; x >= 1; --x)
			{
				if (vs[y][x] != '?' && vs[y][x - 1] == '?')
				{
					vs[y][x - 1] = vs[y][x];
				}
			}
		}

		for (int y = 0; y < R-1; ++y)
		{
			if (count(vs[y].begin(), vs[y].end(), '?')==0 && count(vs[y+1].begin(), vs[y+1].end(), '?')>0)
			{
				vs[y+1] = vs[y];
			}
		}

		for (int y = R - 1; y >= 1; --y)
		{
			if (count(vs[y].begin(), vs[y].end(), '?') == 0 && count(vs[y - 1].begin(), vs[y - 1].end(), '?') > 0)
			{
				vs[y - 1] = vs[y];
			}
		}

		PRINTF("Case #%d:\n", testcase + 1);

		for (int y = 0; y < R; ++y)
		{
			PRINTF("%s\n", vs[y].c_str());
		}
	}

	return 0;
}

#endif