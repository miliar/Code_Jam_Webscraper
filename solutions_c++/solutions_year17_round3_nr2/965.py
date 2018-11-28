#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
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
#include <functional> 
#include <fstream> 

using namespace std;

#define M_PI           3.14159265358979323846
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

double dp[1001][1001];
PII pc[1001];

PII task[200];
PII full[200];

int main()
{
	ios::sync_with_stdio(false);

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;
	fin >> T;
	REP(t, T)
	{
		int AC, AJ;
		fin >> AC >> AJ;

		int rest[2] = { 720, 720 };

		REP(i, AC)
		{
			fin >> task[i].first >> task[i].second;
			full[i] = { task[i].first , i };
			rest[0] -= task[i].second - task[i].first;
		}
		REP(i, AJ)
		{
			fin >> task[AC + i].first >> task[AC + i].second;
			full[AC + i] = { task[AC + i].first , AC + i };
			rest[1] -= task[AC + i].second - task[AC + i].first;
		}

		sort(full, full + AC + AJ);

		vector<PII> interv;
		LL res = 0;
		FOR(i, 1, AC + AJ)
		{
			if ((full[i].second < AC) == (full[i - 1].second < AC))
			{
				interv.pb({ task[full[i].second].first - task[full[i - 1].second].second, full[i].second < AC ? 0 : 1 });
				res += 2;
			}
			else
				res += 1;
		}

		if ((full[0].second < AC) == (full[AC + AJ - 1].second < AC))
		{
			interv.pb({ task[full[0].second].first + 24 * 60 - task[full[AC + AJ - 1].second].second, full[0].second < AC ? 0 : 1 });
			res += 2;
		}
		else
			res += 1;

		REP(i, interv.size())
		{
			if (interv[i].first <= rest[interv[i].second])
			{
				rest[interv[i].second] -= interv[i].first;
				res -= 2;
			}
		}

		fout <<"Case #" <<t+1 <<": " << res <<endl;
	}

	return 0;
}