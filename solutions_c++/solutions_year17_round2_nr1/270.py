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
	double D;
	int N;
	fin >> D >> N;
	vd K(N), S(N);
	FOR(i, N) fin >> K[i] >> S[i];
	FOR(i, N)
	{
		FORD(j, i + 1, N - 1)
		{
			if (K[i] > K[j])
			{
				swap(K[i], K[j]);
				swap(S[i], S[j]);
			}
		}
	}

	while (SZ(K) > 1)
	{
		double tmin = -1;
		int j = -1;
		FOR(i, SZ(K) - 1)
		{
			if (S[i + 1] >= S[i]) continue;
			double t1 = (K[i + 1] - K[i]) / (S[i] - S[i + 1]);
			if (j == -1 || t1 < tmin)
			{
				j = i;
				tmin = t1;
			}
		}
		if (j == -1) break;
		if (K[j] + S[j] * tmin >= D) break;
		K.erase(K.begin() + j);
		S.erase(S.begin() + j);
	}

	double t = (D - K[0]) / S[0];
	double v = D / t;

	fout << fixed << setprecision(9) << "Case #" << TN << ": " << v << endl;
	cout << fixed << setprecision(9) << "Case #" << TN << ": " << v << endl;
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
