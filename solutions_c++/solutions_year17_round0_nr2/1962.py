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
		string s;
		
		cin >> s;

		for (int i = 0; i<s.length() - 1; i++)
			if (s[i] > s[i + 1])
			{
				s[i] = (char)((int)s[i] - 1);
				while (i>=1 && s[i-1] > s[i]) s[i-1] = (char)((int)s[i-1] - 1), i--;
				for (int j = i + 1; j < s.length(); j++) s[j] = '9';
				while (s.length() > 0 && s[0] == '0') s.erase(s.begin(), s.begin() + 1);
				break;
			}


		cout << "Case #" << tr + 1 << ": " << s << endl;
	}

	return 0;
}