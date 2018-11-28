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
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll, ll> pii;
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

ll f2(ll w)
{
	return (1 + w) * w / 2;
}

int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int T; cin >> T;
	for (size_t i = 0; i < T; i++)
	{
		int K, ans = 0;
		string S; cin >> S >> K;
		for (size_t j = 0; j + K - 1 <= S.length() - 1; j++)
		{
			if (S[j] == '-'){
				ans++;
				for (size_t jj = 0; jj < K; jj++)
				{
					S[j + jj] = S[j + jj] == '-' ? '+' : '-';
				}
			}
		}
		if (count(ALL(S), '+') == S.length())
		{
			cout << "Case #" << i + 1 <<": " << ans;
		}
		else
			cout << "Case #"<< i + 1<<": IMPOSSIBLE";
		cout << endl;
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}