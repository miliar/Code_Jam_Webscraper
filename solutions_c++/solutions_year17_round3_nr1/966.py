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

int main()
{
	ios::sync_with_stdio(false);

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;
	fin >> T;
	REP(t, T)
	{
		int N, K;
		fin >> N >> K;
		REP(i, N)
			fin >> pc[i+1].first >> pc[i+1].second;

		sort(pc+1, pc + N+1);
		reverse(pc+1, pc + N+1);

		REP(i, N+1)
			REP(j, K+1)
				dp[i][j] = 0;
		
		REP(i, N)
		{
			dp[i+1][1] = max(dp[i][1], M_PI * pow(pc[i+1].first, 2) + 2 * M_PI * pc[i+1].first * pc[i+1].second);
			FOR(j, 1, K)
			{
				dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + 2 * M_PI * pc[i+1].first * pc[i+1].second);
			}
		}

		fout << "Case #" <<(t+1) << ": " <<setprecision(8) << fixed << dp[N][K] << endl;
	}

	return 0;
}