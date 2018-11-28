#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

string solve()
{
	const string impos = "IMPOSSIBLE";
	int N, R, O, Y, G, B, V;
	fin >> N >> R >> O >> Y >> G >> B >> V;

	if (R + G == N && R < G || R + G < N && R <= G && G > 0) return impos;
	if (Y + V == N && Y < V || Y + V < N && Y <= V && V > 0) return impos;
	if (B + O == N && B < O || B + O < N && B <= O && O > 0) return impos;

	string ret;

	if (R + G == N && R == G)
	{
		FOR(i, R) ret += "RG";
		return ret;
	}
	if (Y + V == N && Y == V)
	{
		FOR(i, Y) ret += "YV";
		return ret;
	}
	if (B + O == N && B == O)
	{
		FOR(i, B) ret += "BO";
		return ret;
	}

	int r = R - G;
	int y = Y - V;
	int b = B - O;
	if (r > y + b || y > r + b || b > r + y) return impos;

	vector<string> aret;

	auto update = [&aret](int & rem, int two, string chars)
	{
		string s;
		s += chars[1];
		rem--;
		if (rem == 0) FOR(i, two) s += chars;
		aret.push_back(s);
	};

	if (r >= y && r >= b)
		update(r, G, "GR");
	else if (y >= r && y >= b)
		update(y, V, "VY");
	else
		update(b, O, "OB");

	while (r + y + b > 0)
	{
		if (aret.back().back() == 'R')
		{
			if (y >= b)
				update(y, V, "VY");
			else
				update(b, O, "OB");
			continue;
		}
		if (aret.back().back() == 'Y')
		{
			if (r >= b)
				update(r, G, "GR");
			else
				update(b, O, "OB");
			continue;
		}
		if (r >= y)
			update(r, G, "GR");
		else
			update(y, V, "VY");
	}

	if (aret.back().back() == aret[0][0])
		swap(aret.back(), *--(--aret.end()));

	ret = accumulate(ALL(aret), string());
	return ret;
}

void solve_case(int TN)
{
	string ans = solve();
	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
