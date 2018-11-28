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
typedef pair<i64, i64> pii;

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
	i64 N, K;
	fin >> N >> K;

	i64 n1 = N + 1, k1 = 0, k2 = 1;
	while (K > k1 + k2)
	{
		K -= k1 + k2;
		i64 q1 = (n1 & 1) ? 2 * k1 + k2 : k1;
		i64 q2 = (n1 & 1) ? k2 : k1 + 2 * k2;
		k1 = q1;
		k2 = q2;
		n1 /= 2;
	}

	pii ans = K <= k1 ? pii(n1 / 2, (n1 - 1) / 2) : pii((n1 - 1) / 2, (n1 - 2) / 2);

	fout << "Case #" << TN << ": " << ans.first << " " << ans.second << endl;
	cout << "Case #" << TN << ": " << ans.first << " " << ans.second << endl;
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
