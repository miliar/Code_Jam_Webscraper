#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 100 + 10;
const double EPS = 1e-9;
typedef long long LL;
const LL MOD = 1000 * 1000 * 1000 + 7;



int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("data.in", "r", stdin); freopen("data.out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie();

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt) {
		int ans;

		int n, d;
		cin >> d >> n;
		vector<pair<int, int> > horses(n);
		forn(i, 0, n)cin >> horses[i].first >> horses[i].second;

		vector<double> times;

		double mintime = 0;

		forn(i, 0, n) {
			double dist = d - horses[i].first;
			double time = dist / ((double)horses[i].second);
			times.push_back(time);
			mintime = min(mintime, time);
		}

		while (times.size() > 0) {
			mintime = max(times.back(), mintime); times.pop_back();}

		cout << "Case #" << tt  + 1<< ": "<<fixed<<setprecision(10) << d / mintime <<endl;
	}


	return 0;
}