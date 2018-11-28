#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void run() {
	ll T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		string S;
		ll K;

		cin >> S;
		cin >> K;

		ll N = S.size();

		ll am = 0;
		for(int i = 0; i <= N-K; i++) {
			if(S[i] == '+') continue;
			
			am++;
			for(int j = i; j < i+K; j++) {
				if(S[j] == '+') S[j] = '-';
				else if(S[j] == '-') S[j] = '+';
			}
		}		

		ll poss = 1;
		for(int i = 0; i < N; i++) {
			if(S[i] == '-') poss = 0;
		}

		if(!poss) printf("Case #%d: IMPOSSIBLE\n", t+1);
		else printf("Case #%d: %lld\n", t+1, am);
	}


}

int main() {
	run();
}
