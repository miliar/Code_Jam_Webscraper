#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;
typedef long long int Z;

int N;
int S[3];
int S2[3];
string Sc = "RYB";
int D[3];
int D2[3];
string Dc = "GVO";

string nope = "IMPOSSIBLE";

string solve() {
	for(int i = 0; i < 3; ++i) {
		if(S[i] + D[i] == N) {
			if(S[i] != D[i]) return nope;
			string ret;
			for(int it = 0; it < S[i]; ++it) {
				ret.push_back(Sc[i]);
				ret.push_back(Dc[i]);
			}
			return ret;
		}
	}
	
	for(int i = 0; i < 3; ++i) {
		if(D[i] && D[i] >= S[i]) return nope;
		S[i] -= D[i];
	}
	
	int m = 0;
	for(int i = 0; i < 3; ++i) {
		m = max(m, S[i]);
	}
	if(2 * m > S[0] + S[1] + S[2]) return nope;
	
	vector<int> asd;
	vector<int> app;
	for(int i = 0; i < 3; ++i) {
		if(S[i]) app.push_back(i);
	}
	
	if((int)app.size() == 2) {
		for(int i = 0; i < m; ++i) {
			asd.push_back(app[0]);
			asd.push_back(app[1]);
		}
	} else {
		while(true) {
			bool stop = false;
			for(int i = 0; i < 3; ++i) {
				if(!S[i]) stop = true;
			}
			if(stop) break;
			int p = -1;
			int b = 0;
			for(int i = 0; i < 3; ++i) {
				if(S[i] > b && (asd.empty() || asd.back() != i)) {
					b = S[i];
					p = i;
				}
			}
			if(p == -1) throw 0;
			--S[p];
			asd.push_back(p);
		}
		
		int xxx = asd.size();
		asd.resize((int)asd.size() + S[0] + S[1] + S[2]);
		int pos = asd.size();
		if(!xxx) throw 0;
		int prev = asd.front();
		while(pos != xxx) {
			--pos;
			bool found = false;
			for(int i = 0; i < 3; ++i) {
				if(i != prev && S[i]) {
					--S[i];
					prev = i;
					asd[pos] = i;
					found = true;
					break;
				}
			}
			if(!found) throw 0;
		}
	}
	
	string ret;
	for(int x : asd) {
		ret.push_back(Sc[x]);
		while(D[x] > 0) {
			ret.push_back(Dc[x]);
			ret.push_back(Sc[x]);
			--D[x];
		}
	}
	return ret;
}

void check(char a, char b) {
	if(a == b) throw 0;
	for(int asdfa = 0; asdfa < 2; ++asdfa) {
		if(a != 'R' && b == 'G') throw 0;
		if(a != 'Y' && b == 'V') throw 0;
		if(a != 'B' && b == 'O') throw 0;
		swap(a, b);
	}
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	Z tc;
	cin >> tc;
	for(Z ti = 1; ti <= tc; ++ti) {
		cin >> N >> S[0] >> D[2] >> S[1] >> D[0] >> S[2] >> D[1];
		copy(S, S + 3, S2);
		copy(D, D + 3, D2);
		
		string result = solve();
		if(result != "IMPOSSIBLE" && N != (int)result.size()) throw 0;
		if(result != "IMPOSSIBLE") {
			for(int i = 0; i < 3; ++i) {
				int asd = 0;
				int bsd = 0;
				for(char c : result) {
					if(c == Sc[i]) ++asd;
					if(c == Dc[i]) ++bsd;
				}
				if(asd != S2[i]) throw 0;
				if(bsd != D2[i]) throw 0;
			}
			for(int p = 1; p < (int)result.size(); ++p) {
				check(result[p - 1], result[p]);
			}
			check(result.front(), result.back());
		}
		cout << "Case #" << ti << ": " << result << '\n';
	}
	
	return 0;
}
