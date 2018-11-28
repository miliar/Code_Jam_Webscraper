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
	const i64 inf = (i64)1e16;
	int N, Q;
	fin >> N >> Q;
	vi D(N), S(N);
	FOR(i, N) fin >> D[i] >> S[i];
	vvi A(N, vi(N));
	FOR(i, N) FOR(j, N)
	{
		fin >> A[i][j];
		if (A[i][j] == -1) A[i][j] = inf;
	}

	vvi B = A;
	FOR(i, N) B[i][i] = 0;
	FOR(k, N) FOR(i, N) FOR(j, N) B[i][j] = min(B[i][j], B[i][k] + B[k][j]);

	vvd T(N, vd(N));
	FOR(i, N) FOR(j, N)
	{
		if (B[i][j] >= inf || B[i][j] > D[i])
			T[i][j] = inf;
		else
			T[i][j] = B[i][j] / (double)S[i];
	}
	FOR(k, N) FOR(i, N) FOR(j, N) T[i][j] = min(T[i][j], T[i][k] + T[k][j]);

	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";
	FOR(i, Q)
	{
		int u, v;
		fin >> u >> v;
		u--, v--;
		fout << fixed << setprecision(9) << " " << T[u][v];
		cout << fixed << setprecision(9) << " " << T[u][v];
	}
	fout << endl;
	cout << endl;
}

int main()
{
	fin.open("C.in"); 
	fout.open("C.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
