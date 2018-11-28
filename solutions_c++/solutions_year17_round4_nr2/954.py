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

template<typename T>
inline max3(T a, T b, T c) {
	return a > b ? (a > c ? a : c) : (b > c ? b : c);
}


struct ticket{
	int p, b;
	bool operator<(const ticket& other) const {
		return p != other.p ? p < other.p : b < other.b;
	}
};

struct seat {
	int p, f;
	bool operator<(const seat& other) const {
		return f != other.f ? f > other.f : p < other.p;
	}
	seat(int _p, int _f) : p(_p), f(_f) {}
};

struct ticket_holder {
	int n1 = 0;
	int count = 0;
	map<int, int> T;
	set<seat> S;
	
	int top() const {
		if (S.size())
			return S.begin()->p;
		return -1;
	}
	
	void inc(int P) {
		count++;
		if (P == 1) {
			n1++;
			return;
		}
		int F = 0;
		if (T.find(P) != T.end())
			F = T[P];
		if (F > 0) 
			S.erase(seat(P, F));
		T[P] = F + 1;
		S.insert(seat(P, F + 1));
		// cerr << P << " " << F << endl;
	}
	
	int dec_top(int preference = 0) {
		if (S.size() == 0)
			return -1;
		auto X = S.begin();
		
		if (S.size() > 1) {
			auto Y = S.begin();
			Y++;
			if (Y->p == preference && X->f == Y->f) {
				X = Y;
			}
		}
		
		// cerr << ":::" << X->p << " " << X->f << endl;
		int ret = X->p;
		T[ret]--;
		if (X->f > 1)
			S.insert(seat(ret, X->f - 1));
		else
			T.erase(ret);
		S.erase(*X);
		return ret;
	}
	
	int dec(int not_P) {
		
		if (T.find(not_P) != T.end())
			S.erase(seat(not_P, T[not_P]));
		
		if (S.size()) {
			dec_top();
			if (T.find(not_P) != T.end())
				S.insert(seat(not_P, T[not_P]));
			return 0;
		}

		T[not_P]--;
		if (T[not_P])
			S.insert(seat(not_P, T[not_P]));
		return 1;
	}
	
};


void solve_simple(vector<ticket>& T, int M) {
	sort(T.begin(), T.end());
	
	map<int, ticket_holder> TH;
	
	for(int i = 0; i < M; ++i){
		int B = T[i].b;
		int P = T[i].p;
		if (TH.find(B) == TH.end())
			TH[B] = ticket_holder();
		TH[B].inc(P);
	}
	
	// cerr << TH[1].count << " " << TH[2].count << " __ " << TH[1].n1 << " "  << TH[2].n1 << endl;
	
	if (false) {	
		for(int j = 1; j <= 2; ++j){
			foreach(x, TH[j].T)
				cerr << j << " :: " << x->first << " " << x->second << endl;			
		}
	}
	
	int Y = max3(TH[1].count, TH[2].count, TH[1].n1 + TH[2].n1);
	for (int i = 1; i <= 2; ++i) {
		int N = TH[i].n1;
		for(int j = 0; j < N; ++j) {
			TH[3 - i].dec_top(TH[i].top());
		}
	}
	int Z = 0;
	while (TH[1].S.size() && TH[2].S.size()) {
		int i = TH[1].S.size() < TH[2].S.size() ? 1 : 2;
		int P = TH[i].dec_top();
		Z += TH[3 - i].dec(P);
		
	}
	
	cout << Y << " " << Z << endl;
	// cerr << "RET: " << Y << " " << Z << endl;
	
}

void solve() {
	int N, C, M;
	cin >> N >> C >> M;
	vector<ticket> T(M);	
	for(int i = 0; i < M; ++i){
		cin >> T[i].p >> T[i].b;
	}
	solve_simple(T, M);

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
