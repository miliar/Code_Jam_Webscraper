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


void printNumber(vi &xs) {
	rep(i, 0, sz(xs))
		cout << xs[i];
	cout << endl;
}

int main() {
	cin.sync_with_stdio(0);
	
	int T;
	ll N;

	cin >> T;
	rep(tc, 1, T+1) {
		cin >> N;
		vi number;

		while(N > 0) {
			number.push_back((int) N % 10);
			N /= 10;
		}
		reverse(all(number));

		rep(i, 1, sz(number)) {
			if(number[i] < number[i-1]) {
				rep(j, i, sz(number)) {
					number[j] = 9;
				}
				number[i-1]--;

				if(number[0] == 0) {
					number.erase(number.begin());
				}

				i = 0;
			}
		}

		cout << "Case #" << tc << ": ";
		printNumber(number);
	}
}