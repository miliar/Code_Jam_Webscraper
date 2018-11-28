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

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

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
	//    if (!freopen("1.in", "r", stdin))
	//    {
	//        cerr << "No input file" << endl;
	//        return 1;
	//    }
	//    if (!freopen("1.out", "w", stdout))
	//    {
	//        cerr << "Error creating output file" << endl;
	//        return 1;
	//    }
	ios::sync_with_stdio(false);


	FILE *f, *g;
	freopen_s(&f, "input.txt", "r", stdin);
	freopen_s(&g, "output.txt", "w", stdout);
	

	int t;
	cin >> t;

	for (int tr = 0; tr < t; tr++) {
		unsigned long long n, k;
		cin >> n >> k;


		unsigned long long x = 1;
		unsigned long long lvl = 1;
		while ((x-1) < k) x *= 2, lvl++;
		x /= 2;
		lvl--;

		unsigned long long A = n;
		unsigned long long B = n;
		unsigned long long numA = 1;
		unsigned long long numB = 0;

		x = 1;

		for (int i = 0; i < lvl - 1; i++) {
			if (x > k) break;

			unsigned long long x1 = (A - 1) / 2;
			unsigned long long x2 = A / 2;
			unsigned long long y1 = (B - 1) / 2;
			unsigned long long y2 = B / 2;

			unsigned long long newA = min(min(x1, x2), min(y1, y2));
			unsigned long long newB = max(max(x1, x2), max(y1, y2));

			unsigned long long newNumA = 0;
			unsigned long long newNumB = 0;

			if (newA == x1) newNumA += numA;
			if (newA == x2) newNumA += numA;
			if (newA == y1) newNumA += numB;
			if (newA == y2) newNumA += numB;

			if (newB == x1) newNumB += numA;
			if (newB == x2) newNumB += numA;
			if (newB == y1) newNumB += numB;
			if (newB == y2) newNumB += numB;

			
			numA = newNumA;
			numB = newNumB;
			A = newA;
			B = newB;
			if (A == B) numB = 0;

			k -= x;
			x *= 2;
		}
		if (numB<k)
			cout << "Case #" << tr + 1 << ": " << A / 2 << " " << (A - 1) / 2 << endl;
		else
			cout << "Case #" << tr + 1 << ": " << B / 2 << " " << (B - 1) / 2 << endl;
	}

	return 0;
}