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

char rev(char c)
{
	return c == '+' ? '-' : '+';
}

void solve_case(int TN)
{
	int K;
	string S;
	fin >> S >> K;
	int N = LEN(S);
	
	int ans = 0;
	FORD(i, 0, N - K)
	{
		if (S[i] == '-')
		{
			ans++;
			FORD(j, i, i + K - 1)
				S[j] = rev(S[j]);
		}
	}

	if (S == string(N, '+'))
	{
		fout << "Case #" << TN << ": " << ans << endl;
		cout << "Case #" << TN << ": " << ans << endl;
	}
	else
	{
		fout << "Case #" << TN << ": IMPOSSIBLE\n";
		cout << "Case #" << TN << ": IMPOSSIBLE\n";
	}

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
