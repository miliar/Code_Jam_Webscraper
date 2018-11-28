#include<bits/stdc++.h>
using namespace std;
int main() {
	int T; cin >> T;
	for (int tc=1; tc<=T; tc++) {
		string s; cin >> s;
		int N = (int) s.size();
		int K; cin >> K;
		int answer = 0;
		for (int i=0; i<N-K+1; i++) {
			if (s[i] == '-') {
				answer++;
				for(int j=0;j<K;j++)s[i+j]='-'+'+'-s[i+j];
			}
		}
		if (count(s.begin(), s.end(), '-')) printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, answer);
	}
}
