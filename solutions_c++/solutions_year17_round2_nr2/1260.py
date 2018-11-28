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

#define NO_WAY "IMPOSSIBLE"

enum colors {
	red = 1, yellow, orange, blue, violet, green
};

struct color {
	char mask;
	int count;
	int initial_count;
	color(char _mask, int _count) : mask(_mask), count(_count), initial_count(_count) {}
	
	const bool operator<(const color& o) const {
		if (count != o.count)
			return count < o.count;
		if (initial_count != o.initial_count)
			return initial_count < o.initial_count;
		return mask < o.mask;
	}
	const bool operator&(const color& o) const {
		return mask & o.mask;
	}
	
	inline char to_str() const {
		switch(mask) {
			case colors::red: return 'R'; break;
			case colors::yellow: return 'Y'; break;
			case colors::orange: return 'O'; break;
			case colors::blue: return 'B'; break;
			case colors::violet: return 'V'; break;
			case colors::green: return 'G'; break;			
		}
		return 0;
	}
	
};



string solve_simple(vector<color>& C) {
	int sum = 0, biggest = 0;
	for(const auto& c : C){
		sum += c.count;
		biggest = max(biggest, c.count);
	}
	if (2 * biggest > sum)
		return NO_WAY;
	sort(C.begin(), C.end());
	vector<color> ret;
	for (int i = 0; i < sum; ++i) {
		int idx = 1;
		if (ret.empty() || !(ret.back() & C[2]))
			idx = 2;
		ret.push_back(C[idx]);
		C[idx].count--;
		sort(C.begin(), C.end());
	}
	string res = "";
	for (const auto& c : ret)
		res += c.to_str();
	return res;	
}



void solve() {
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	vector<color> C;
	C.emplace_back(colors::red, R);
	C.emplace_back(colors::blue, B);
	C.emplace_back(colors::yellow, Y);
	cout << solve_simple(C) << endl;
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
