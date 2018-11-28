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

void n2arr(i64 n, vi& a)
{
	a.clear();
	if (n == 0) a.push_back(0);
	while (n > 0)
	{
		a.push_back(n % 10);
		n /= 10;
	}
}

i64 arr2n(const vi& r)
{
	i64 n = 0;
	FORR(i, 0, SZ(r) - 1) n = 10 * n + r[i];
	return n;
}

void solve_case(int TN)
{
	i64 X;
	fin >> X;
	vi A;
	n2arr(X, A);
	FOR(i, SZ(A) - 1)
	{
		if (A[i] < A[i + 1])
		{
			FOR(j, i + 1) A[j] = 9;
			A[i + 1]--;
		}
	}
	if (A.back() == 0)
		A.pop_back();

	i64 ans = arr2n(A);

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
