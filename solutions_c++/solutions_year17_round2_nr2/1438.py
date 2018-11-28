/*
ID: dixtosa1
PROG: milk2
LANG: C++11
*/
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
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
#include <functional> //std::greater<int>
#include "main.h"
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll, char> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(long long i = 0; i < (long long)N; i++)
#define fornj(N)         for(long long j = 0; j < (long long)N; j++)
#define fornk(N)         for(long long k = 0; k < (long long)N; k++)
#define foreach(c,itr)   for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define awesome vector<int> A(N); forn(N) scanf("%d", &A[i]);
#define v vector
#define File "Patterns"
using namespace std;

pii* aaa;
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int T; cin >> T;
	for (size_t t = 0; t < T; t++)
	{
		ll N, r, o, y, g, b, v;
		cin >> N >> r >> o >> y >> g >> b >> v;

		string ans = "";
		aaa = new pii[3] {make_pair(r, 'R'), make_pair(y, 'Y'), make_pair(b, 'B') };
		sort(aaa, aaa + 3);
		ll l = aaa[2].first;
		ll m = aaa[1].first;
		ll s = aaa[0].first;
		if (l > m + s) ans = "IMPOSSIBLE";
		else
		{
			for (size_t i = 0; i < (m + s - l); i++)
			{
				ans += aaa[2].second;
				ans += aaa[1].second;
				ans += aaa[0].second;
				
				aaa[1].first--;
				aaa[2].first--;
				aaa[0].first--;
			}
			while (aaa[1].first != 0)
			{
				ans += aaa[2].second;
				ans += aaa[1].second;
				aaa[1].first--;
			}
			while (aaa[0].first != 0)
			{
				ans += aaa[2].second;
				ans += aaa[0].second;
				aaa[0].first--;
			}
		}
		
		cout << "Case #" << t + 1<< ": " << ans << endl;
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}