#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	long long N, K;
	cin >> N >> K;
	
	map<long long, long long> segs;
	
	segs[N] = 1;
	
	while (1) {
		long long l = segs.rbegin()->first;
		long long n = segs.rbegin()->second;
		if (n >= K) {
			cout << "Case #" << t << ": " << l/2 << " " << (l-1)/2 << endl;
			return;
		}
		
		K -= n;
		segs[l/2] += n;
		segs[(l-1)/2] += n;
		segs.erase(l);
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
