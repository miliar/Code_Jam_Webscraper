#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <stack>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(i, a, n) for(int i=(a), __ ## i=(n); i<__ ## i; i++)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";if(sz(X))cout<<*(X).end();cout<<"}"<<endl;}

template<class T> ostream &operator<<(ostream &os, const vector<T> &vec)
{
	os << '{';
	REP(i, sz(vec))
	{
		os << vec[i];
		if (i + 1 != sz(vec))
			os << ',';
	}
	os << '}';
	return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &par)
{
	os << '(' << par.X << ',' << par.Y << ')';
	return os;
}

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<unsigned long long> VULL;
typedef vector<vector<int>> VVI;
typedef queue<int> QI;

int gcd(int x, int y)
{
	return y ? gcd(y, x % y) : abs(x);
}

template<class T> T sqr(T x)
{
	return x * x;
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	ios::sync_with_stdio(false);

	int T;
	fin >> T;
	REP(t, T)
	{
		LL N;
		fin >> N;

		LL n = N;
		int len = 1;
		LL pp = 1;
		while ((n /= 10) > 0)
		{
			len++;
			pp *= 10;
		}

		int last = -1;
		LL pptochange = pp;
		REP(i, len)
		{
			int cur = (N / pp) % 10;
			if (cur > last)
			{
				pptochange = pp;
				last = cur;
			}
			else if (cur < last)
			{
				N = (N / pptochange) - 1;
				while (pptochange > 1)
				{
					N = (N * 10) + 9;
					pptochange /= 10;
				}
				break;
			}

			pp /= 10;
		}


		fout << "Case #" << (t + 1) << ": " << N << endl;
	}

	fin.close();
	fout.close();

	return 0;
}