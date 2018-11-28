#include <bits/stdc++.h>
#define d(x) if(debug) cerr<<#x<<": "<<x<<endl;
#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;

bool debug = 0;

template<class T> ostream& operator<<(ostream& os, vector<T>& v) {for (auto i : v) os << i << " "; return os;}
template<class T> ostream& operator<<(ostream& os, set<T>& v) {for (auto i : v) os << i << " "; return os;}
template<class T, class R> ostream& operator<<(ostream& os, pair<T, R>& v) {os << '(' << v.X << ' ' << v.Y << ')' << ' '; return os;}

inline ll get() {
	ll x;
	cin >> x;
	return x;
}

void solve();

int main() {
#ifdef The_Fusy
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	debug = 1;
#endif
	ios_base::sync_with_stdio(false);
	solve();
	if (debug)
		cerr << endl << "Time: " << (ld(clock()) / ld(CLOCKS_PER_SEC)) << endl << endl;
	return 0;
}

void tp(ll test, string answer){
	if(answer[0] == '0') answer = answer.substr(1);
	cout << "Case #"<< test << ": "<< answer << "\n";
}

void solve() {
	ll t = get();
	for(ll test = 1; test <= t; test++){
		string s;
		cin >> s;
		for(ll kek = 0; kek <= 20; kek++){
			bool u = false;
			for(ll i = 0; i < s.size(); i++){
				if(u) s[i] = '9';
				else if(!u && i == s.size() - 1) break;
				else if(s[i + 1] < s[i]){
					s[i]--;
					u = true;
				}
			}
		}
		tp(test, s);
	}
}
