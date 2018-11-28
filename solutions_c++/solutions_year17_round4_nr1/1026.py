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

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

#define ceil2(a,b)  ( ( (a) + (b)-1) / (b) )

int calc(vector<int>& G, int P) {
	
	// cerr << v_2_s(G) << endl;
	int ret, leftovers;
	switch (P) {
		case 2:
			return G[0] + (G[1] + 1) / 2;
		case 3:
			ret = G[0] + min(G[1], G[2]);
			leftovers = max(G[1], G[2]) - min(G[1], G[2]);
			return ret + ceil2(leftovers, 3);
		case 4:
			ret = G[0] + min(G[1], G[3]) + G[2] / 2;
			leftovers = max(G[1], G[3]) - min(G[1], G[3]) + 2 * (G[2] % 2);
			return ret + ceil2(leftovers, 4);
		default:
			return -1;
	}
			
			
}


void solve() {
	int N, P, X;
	cin >> N >> P;
	vector<int> G(P);
	for(int i = 0; i < N; ++i){
		cin >> X;
		G[X % P]++;
	}
	cout << calc(G, P) << endl;
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
