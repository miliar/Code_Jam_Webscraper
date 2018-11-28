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


const int DAY = 1440;
const int TARGET = DAY / 2;

struct activity {
	int S, E, P;
	int length() const { return E - S; }
	activity(int s, int e, int p) : S(s), E(e), P(p) {}	
	bool operator<(const activity& other) const {
		return S < other.S;
	}
};

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}

int solve_easy(vector<activity>& A, int Ac, int Aj) {
	int N = sz(A);
	
	if (N < 2 || Ac == 1 || Aj == 1)
		return 2;
	for(int i = 0; i < N; ++i) {
		int j = (i + 1) % N;
		if (A[i].P != A[j].P)
			continue;
		int dist = (A[j].E + DAY - A[i].S) % DAY;		
		if (dist <= TARGET) {
			return 2;
		}
	}
	return 4;
}

int solve_hard(vector<activity>& A) {
	int N = sz(A);
	vector<int> total(2, 0);
	vector<int> counts(2, 0);
	for(int i = 0; i < N; ++i){
		total[A[i].P] += A[i].length();
		counts[A[i].P] ++;
	}
	vector<vector<int> > gaps(2, vector<int>());
	for(int i = 0; i < N; ++i){
		int j = (i + 1) % N;
		if (A[i].P != A[j].P)
			continue;
		int dist = (A[j].S + DAY - A[i].E) % DAY;
		gaps[A[i].P].push_back(dist);
	}
	int tasks = 0;
	for(int i = 0; i < 2; ++i){
		sort(gaps[i].begin(), gaps[i].end());
		for(int j = 0; j < sz(gaps[i]); ++j){
			if (total[i] + gaps[i][j] > TARGET)
				break;
			total[i] += gaps[i][j];
			counts[i]--;
		}
		relaxmax(tasks, counts[i]);
	}
	
	return tasks * 2;
}


void solve() {
	int Ac, Aj;
	cin >> Ac >> Aj;
	vector<activity> A;
	int X, Y;
	for(int i = 0; i < Ac + Aj; ++i){
		cin >> X >> Y;
		A.emplace_back(X, Y, i < Ac ? 0 : 1);
	}
	sort(A.begin(), A.end());
	int ret = solve_hard(A);
	// cerr << ret << endl << endl;
	cout << ret << endl;

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
