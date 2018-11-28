#include <bits/stdc++.h>
using namespace std;
typedef long long ull;
ull n, k, s, b;
priority_queue<ull> arr;
int ac, T;
pair<int,int> calc(int n, int k) {
	while(arr.size()) arr.pop();
	arr.push(n);
	for(int i=0; i<k; i++) {
		ull t = arr.top()-1;
		arr.pop();
		s = t/2;
		b = t - s;
		arr.push(b);
		arr.push(s);
	}
	return make_pair(b, s);
} 
pair<ull,ull> calc2(ull n, ull k) {
	n -= k;
	ull block = 64 - __builtin_clzll(k);
	ull b = (n + (1ull << (block-1))) >> block;
	ull s = (n) >> block;
	return make_pair(b, s);
} 
int main() {
	freopen("C-large.in", "r", stdin); 
	freopen("C-large.out", "w", stdout); 
	cin >> T;
	for(int K=1; K<=T; K++) {
		cin >> n >> k;
		auto ans = calc2(n, k);
		cout << "Case #" << K << ": " << ans.first << " " << ans.second << endl;
	}
} 
