#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<bitset>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

char flip(char c) {
	if(c == '+') {
		return '-';
	} else {
		return '+';
	}
}

void solve() {
	string s;
	int k;
	cin >> s >> k;

	int flips = 0;
	FOR(i, 0, s.length() - k) {
		if(s[i] == '+') {
			continue;
		} else {
			++flips;
			REP(j, k) {
				s[i + j] = flip(s[i + j]);
			}
		}
	}

	REP(i, s.length()) {
		if(s[i] == '-') {
			cout << "IMPOSSIBLE";
			return;
		}
	}

	cout << flips;
}

int main() {
	int t;
	cin >> t;

	REP(i, t) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}
