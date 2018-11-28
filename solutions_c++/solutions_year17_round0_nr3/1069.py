#include <bits/stdc++.h>
using namespace std;
map <long long, long long> M;


int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, cases = 0;
	long long n, k;
	cin >> T;
	while(T--) {
		cin >> n >> k;
		M.clear();
		M[n] = 1;
		long long last_space;
		while(k > 0) {
			long long space = M.rbegin()-> first;
			long long count = M.rbegin()-> second;
			if(k <= count) {
				last_space = space;
				k = 0;
			} else {
				long long l = (space - 1) / 2;
				long long r = (space - 1) - l;
				M.erase(space);
				M[l] += count;
				M[r] += count;
				k -= count;
			}
		}
		long long tl = (last_space - 1) / 2;
		long long tr = (last_space - 1) - tl;
		printf("Case #%d: %I64d %I64d\n", ++cases, max(tl, tr), min(tl, tr));
	}
	return 0;
}
