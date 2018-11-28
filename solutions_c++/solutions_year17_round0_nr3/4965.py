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
		int N, K, ansMax, ansMin; cin >> N >> K;

		priority_queue<pair<int, int>> pq;
		pq.push(make_pair(N, 0));
		for (int i = 0; i < K; i++)
		{
			auto top = pq.top();
			pq.pop();
			ansMin = top.first / 2 - (top.first % 2 == 0);
			ansMax = top.first / 2;
			pq.push(make_pair(ansMin, top.second));
			pq.push(make_pair(ansMax, -(-top.second + 1 + ansMin)));
		}
		cout << "Case #" << t + 1<< ": " << ansMax << " " << ansMin << "\n";
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}