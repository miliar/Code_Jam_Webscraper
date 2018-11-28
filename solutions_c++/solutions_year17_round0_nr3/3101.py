#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

pair<long long, long long> border(long long N, long long K) {
	set <long long> S;
	map <long long, long long> MAP;
	S.insert(N);
	MAP[N] = 1;
	
	while (S.size() > 0) {
		long long L = *S.rbegin();
		S.erase(L);
		long long times = MAP[L];

		long long a = (L-1)/2;
		long long b = L - 1 - a;
		
		if (K <= times) return {b,a};
		
		K -= times;
		if ( a > 0) S.insert(a);
		if ( b > 0) S.insert(b);
		MAP[a] += times;
		MAP[b] += times;
	}
	assert(false);
	return {-1,-1};
}

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		long long N, K;
		cin >> N >> K;
		
		pair<long long, long long> p = border(N, K);
		
		cout<<"Case #"<<test<<": " << p.first << " " << p.second << "\n";
	}
	return 0;
}
