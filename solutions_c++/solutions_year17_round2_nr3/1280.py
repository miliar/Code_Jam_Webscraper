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

struct horse {
	int64 E, S;
};

template<typename T, typename U> inline void relaxmin(T &res, const U &x) {
  if (x < res) {
    res = x;
  }
}

double solve(int N, int Q, const vector<horse>& H, vector<vector<int64> >& D, int U, int V) {
	vector<double> ret(N, 0);
	for(int i = 0; i < N; ++i) {
		int64 dist = 0;
		auto h = H[i];
		for(int j = i + 1; j < N; ++j) {			
			dist += D[j - 1][j];
			if (h.E < dist)
				break;
			double t = (double)dist / h.S;
			if (ret[j] == 0 || ret[j] > ret[i] + t)
				ret[j] = ret[i] + t;
			// cerr << j << " " << dist << " " << ret[j] << endl;
		}
	}
	return ret[V - 1];
}


void solve() {
	int N, Q; 
	cin >> N >> Q;
	vector<horse> H(N);
	for(int i = 0; i < N; ++i){
		cin >> H[i].E >> H[i].S;
	}
	vector<vector<int64> > D(N, vector<int64>(N));
	for(int i = 0; i < N; ++i){
		for(int j = 0; j < N; ++j){
			cin >> D[i][j];
		}
	}
	
	for(int i = 0; i < Q; ++i){
		int U, V;
		cin >> U >> V;
		cout << std::setprecision(6) << std::fixed << solve(N, Q, H, D, U, V) << ((i != Q - 1) ? ' ' : '\n');
	}

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
