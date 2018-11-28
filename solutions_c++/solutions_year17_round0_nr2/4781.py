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

string solve(string S)
{
	if (S.length() == 0) return "";

	int b = 0;
	while (b + 1 < S.length() && S[b] <= S[b + 1]) b++;
	if (b + 1 == S.length())
	{
		return S;
	}
	string newS = S.substr(0, b + 1);
	int j = newS.length() - 1;
	while (newS[j] == '0') {
		newS[j] = '9';
		j--;
	}
	newS[j]--;

	if (newS[0] == '0') newS.erase(newS.begin());

	return solve(newS) + string(S.length() - b - 1, '9');
}
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
		string S; cin >> S;
		cout << "Case #" << t + 1<< ": " << solve(S) << endl;
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}