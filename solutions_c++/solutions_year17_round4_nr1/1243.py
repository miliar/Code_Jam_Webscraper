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


void solve_case(int TN)
{
	int n, p;
	fin >> n >> p;
	vector<int> M(p);
	FOR(i, n)
	{
		int x;
		fin >> x;
		M[x%p]++;
	}

	int ans = 0;
	if (p == 2)
	{
		ans = M[0] + (M[1] + 1) / 2;
	}
	else if (p == 3)
	{
		ans = M[0] + min(M[1], M[2]);
		ans += (abs(M[1] - M[2]) + 2) / 3;
	}
	else
	{
		ans = M[0] + M[2] / 2 + min(M[1], M[3]);
		int r2 = M[2] % 2;
		int r13 = abs(M[3] - M[1]);
		if (r2 == 1 && r13 >= 2)
		{
			ans++;
			r2 = 0;
			r13 -= 2;
		}
		ans += r13 / 4;
		r13 %= 4;
		if (r2 + r13 > 0)
			ans++;
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
