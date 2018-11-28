#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
ull N, tens[20] = {1};
int T, K;
inline ull _(ull x, int d) { return (x/tens[d]) % 10; }
bool istidy(ull x) {
	stringstream ss;
	ss << x;
	string s = ss.str();
	for(int i=1; i<s.length(); i++){
		if (s[i-1] > s[i]) return 0;
	}
	return 1;
}
int main() {
	freopen("B-large.in", "r", stdin); 
	freopen("B-large.out", "w", stdout); 
	for(int i=1; i<20; i++) tens[i] = tens[i-1] * 10ull;
	cin >> T;
	for(int K=1; K<=T; K++) {
		cin >> N;
		int cur = 0;
		for(; !istidy(N); cur++) {
			N -= tens[cur] * (_(N, cur) + 1);
		}
		cout << "Case #" << K << ": " << N << endl;
	}
} 
