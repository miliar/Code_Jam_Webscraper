#include <bits/stdc++.h>
using namespace std;

int T, K;
string S;

int main(){
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cin >> S >> K;
		S = "+" + S + "+";
		vector<char> step(S.size());
		int flips = 0;
		for(unsigned i=1; i<step.size(); ++i) {
			if(S[i] != S[i-1]) step[i] = true;
		}
		for(unsigned i=0; i<step.size(); ++i) {
			if(step[i]) {
				++flips;
				if(i+K >= step.size()) flips = -1;
				else step[i+K] ^= 1;
			}
		}
		cout << "Case #" << t << ": ";
		if(flips == -1) cout << "IMPOSSIBLE\n";
		else cout << flips << "\n";
	}
}
