#pragma GCC optimize("03")
#include <bits/stdc++.h>
#include "pp.hpp"
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
#define endl '\n'
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

int main() {
	cin.sync_with_stdio(0);
	
	int T, K;
	string S;

	cin >> T;
	rep(tc, 1, T+1) {
		cin >> S >> K;
		bitset<1000> state(S, 0, S.size(), '+', '-');
		int counter = 0;

		rep(i, 0, sz(S)-K+1) {
			// Flip
			if(state[i] == 1) {
				counter++;
				rep(j, i, i+K) {
					state.flip(j);
				}
			}
		}

		cout << "Case #" << tc << ": ";
		if(state.none()) {
			cout  << counter;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}