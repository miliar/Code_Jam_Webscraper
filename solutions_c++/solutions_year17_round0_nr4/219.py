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

typedef vector<int> vi;
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

struct MaxMatching
{
	vvi a;
	bool found;
	vector<int> w, pr1, pr2;

	bool augment(int v)
	{
		w[v] = 1;
		FOR(i, SZ(a[v]))
		{
			if (a[v][i] && (pr2[i] == -1 || !w[pr2[i]] && augment(pr2[i])))
			{
				pr2[i] = v;
				pr1[v] = i;
				return true;
			}
		}
		return false;
	}

	int matching()
	{
		int n = SZ(a);
		int m = SZ(a[0]);
		found = true;
		pr1.assign(n, -1);
		pr2.assign(m, -1);
		while (found)
		{
			found = false;
			w.assign(n, 0);
			FOR(i, n)
			{
				if (pr1[i] == -1 && augment(i))
				{
					found = true;
					break;
				}
			}
		}
		return n - (int)count(ALL(pr1), -1);
	}
};

void solve_case(int TN)
{
	int N, M;
	fin >> N >> M;	
	vs B(N, string(N, '.'));
	MaxMatching axes, diags;
	axes.a.assign(N, vi(N, 0));
	diags.a.assign(N + N - 1, vi(N + N - 1, 0));
	FOR(i, N) FOR(j, N)
	{
		axes.a[i][j] = 1;
		diags.a[i + j][i - j + N - 1] = 1;
	}
	FOR(i, M)
	{
		char st;
		int r, c;
		fin >> st >> r >> c;
		--r, --c;
		B[r][c] = st;
		if (st == 'x' || st == 'o')
		{
			FOR(j, N)
			{
				axes.a[r][j] = 0;
				axes.a[j][c] = 0;
			}
		}
		if (st == '+' || st == 'o')
		{
			FOR(j, N + N - 1)
			{
				diags.a[r + c][j] = 0;
				diags.a[j][r - c + N - 1] = 0;
			}
		}
	}

	vector<char> Style;
	vector<int> R, C;
	int m1 = axes.matching();
	FOR(i, N)
	{
		int j = axes.pr1[i];
		if (j == -1) continue;
		char st = B[i][j] == '.' ? 'x' : 'o';
		B[i][j] = st;
		Style.push_back(st);
		R.push_back(i);
		C.push_back(j);
	}
	int m2 = diags.matching();
	FOR(i, N + N - 1)
	{
		int j = diags.pr1[i];
		if (j == -1) continue;
		int r = (i + j - (N - 1)) / 2;
		int c = i - r;
		char st = B[r][c] == '.' ? '+' : 'o';
		B[r][c] = st;
		Style.push_back(st);
		R.push_back(r);
		C.push_back(c);
		FOR(k, SZ(R) - 1)
		{
			if (R[k] == R.back() && C[k] == C.back())
			{
				Style[k] = st;
				Style.pop_back();
				R.pop_back();
				C.pop_back();
				break;
			}
		}
	}

	int ans = 0;
	FOR(i, N) FOR(j, N) ans += B[i][j] == 'o' ? 2 : B[i][j] != '.' ? 1 : 0;

	fout << "Case #" << TN << ": " << ans << " " << SZ(R) << endl;
	cout << "Case #" << TN << ": " << ans << " " << SZ(R) << endl;
	FOR(i, SZ(R))
	{
		R[i]++, C[i]++;
		fout << Style[i] << " " << R[i] << " " << C[i] << endl;
		cout << Style[i] << " " << R[i] << " " << C[i] << endl;
	}
}

int main()
{
	fin.open("D.in"); 
	fout.open("D.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
