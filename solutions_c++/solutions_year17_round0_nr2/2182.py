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

int tidy(const string& S) {
	for (size_t i = 1; i < S.size(); ++i)
		if (S[i] < S[i - 1])
			return i - 1;
	return -1;
}

void solve() {
	string S;
	cin >> S;
	int N = sz(S);
	int t = tidy(S);
	if (t == -1) {
		cout << S << '\n';
		return;
	}
	while (t && S[t - 1] == S[t]) --t;
	
	if (S[t] == '1') {
		for (int i = 0; i < N - 1; ++i)
			cout << '9';
		cout << '\n';
		return;
	}
	// cerr << S << " " << t << endl;
	for (int i = 0; i < N; ++i) {
		if (i < t)
			cout << S[i];
		else if (i == t)
			cout << (char)(S[i] - 1);
		else cout << '9';
	}
	cout << '\n';
	
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
