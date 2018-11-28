#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
long long N, Q;
vector<long long> E, S;
vector< vector<long long> > D;
vector<int> U;
vector<int> V;

vector< vector<long long> > paths;
const long long maxpath = 1000000000000000ll;
const double maxt = 1.e20;
int startind;
double dp[1001][1001];

int stackl = 0;

//double solve(int Nf) {
//	stackl++;
//	cout << stackl << " ";
//	if (dp[Nf] >= 0.0) return dp[Nf];
//
//	if (Nf == startind) return 0.;
//
//	double ret = maxt;
//	rep(i,N)
//		if (i != Nf) {
//			if (E[i] >= paths[i][Nf])
//				ret = min(ret, solve(i) + paths[i][Nf] / (double)(S[i]));
//		}
//	return dp[Nf] = ret;
//}

double solve(int Nf, int nchg) {
	//stackl++;
	//cout << stackl << " ";
	if (dp[Nf][nchg] >= 0.0) return dp[Nf][nchg];
	if (Nf == startind) return 0.;
	if (nchg == 0) {
		double ret = maxt;
		if (E[startind] >= paths[startind][Nf])
			ret = paths[startind][Nf] / (double)(S[startind]);
		return dp[Nf][nchg] = ret;
	}

	double ret = solve(Nf, nchg - 1);
	rep(i, N)
		if (i != Nf && E[i] >= paths[i][Nf] && paths[i][Nf] / (double)(S[i])<ret) {
			ret = min(ret, solve(i, nchg - 1) + paths[i][Nf] / (double)(S[i]));
		}
	return dp[Nf][nchg] = ret;
}

int main()
{
	std::string dir = "../../1B/";
	fstream fin(dir + "C-large.in", ifstream::in);
	fstream fout(dir + "C-large.out", ofstream::out);

	cout.precision(12);
	fout.precision(12);

	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		fin >> N >> Q;

		E.resize(N);
		S.resize(N);

		rep(i, N)
			fin >> E[i] >> S[i];

		D = vector< vector<long long> >(N, vector<long long>(N));

		rep(i, N)
			rep(j, N)
				fin >> D[i][j];

		U.resize(Q);
		V.resize(Q);

		rep(i, Q)
			fin >> U[i] >> V[i];

		paths = D;

		
		// Floyd-Warshall
		rep(i, N)
			rep(j, N) {
				if (i == j) paths[i][j] = 0;
				else {
					if (D[i][j]==-1) paths[i][j] = maxpath;
					else paths[i][j] = D[i][j];
				}
			}

		cout << "running time=" << clock() / (double)CLOCKS_PER_SEC << " s\n";
		rep(k, N)
			rep(i, N)
				rep(j, N)
					paths[i][j] = min(paths[i][j], paths[i][k] + paths[k][j]);
		cout << "running time=" << clock() / (double)CLOCKS_PER_SEC << " s\n";

		// Solution
		vector<double> rets;

		rep(k, Q) {
			cout << k << " ";

			startind = U[k] - 1;

			/*rep(i, 1001)
				dp[i] = -1.;*/
			rep(i, 1001)
				rep(j, 1001)
					dp[i][j] = -1.;

			stackl = 0;
			double tret = maxt;// solve(V[k] - 1);
			rep(i, N)
				tret = solve(V[k] - 1, i);

			rets.push_back(tret);
		}
		cout << "\n";

		fout << "Case #" << t << ": ";
		cout << "Case #" << t << ": ";

		rep(i, Q) {
			fout << rets[i] << " ";
			cout << rets[i] << " ";
		}
		fout << "\n";
		cout << "\n";
	}
	fin.close();
	fout.close();
	cout << "running time=" << clock() / (double)CLOCKS_PER_SEC << " s\n";
	system("PAUSE");
	return 0;
}
