/*
ID: ahri1
PROG: A
LANG: C++
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

double solve_easy(int N, double U, vector<double>& P) {
	sort(P.begin(), P.end());
	// reverse(P.begin(), P.end());
	for(int i = 1; i < N; ++i){
		if (U == 0)
			break;
		double needed = (P[i] - P[i - 1]) * i;
		needed = min(needed, U);
		U -= needed;
		for(int j = 0; j < i; ++j){
			P[j] += needed / i;
		}
	}
	if (U > 0) {
		for(int i = 0; i < N; ++i){
			P[i] += U / N;
		}
	}
	double ret = 1;
	for(int i = 0; i < N; ++i){
		ret *= P[i];
	}
	return ret;
}

void solve() {
	int N, K;
	cin >> N >> K;
	double U;
	cin >> U;
	vector<double> P(N);
	for(int i = 0; i < N; ++i){
		cin >> P[i];
	}
	cout.precision(6);
	cout << fixed << solve_easy(N, U, P) << endl;
}

int main() {

  cin.sync_with_stdio(0);
  int T;
  cin >> T;
  for (int i=0;i<T;i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  
  return 0;
}
