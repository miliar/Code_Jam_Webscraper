#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print(long long x) {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": " << x / 2 <<" " << (x - 1) / 2 << "\n";
}

inline void SolveNaive(long long N, long long K) {
	multiset<int> S;
	S.insert(-N);
	while (K --> 1) {
		long long t = -(*S.begin());
		S.erase(S.begin());
		S.insert(-(t / 2));
		S.insert(-((t - 1) / 2));
	}
	return void (case_print(-(*S.begin())));
}
inline void Solve(long long N, long long K) {
	assert(K <= N && K >= 1);
	K --;
	if (K == 0) {
		return void(case_print(N));
	}
	long long two = 1;
	int cnt = 0;
	while (K >= two) {
		K -= two;
		cnt ++;
		two *= 2ll;
	}
	assert(K >= 0);
	
	return void(case_print((N - K) / two));
	
	two /= 2ll;
	assert(two > 0);
	
	cerr << K << " " << cnt << " " << two << endl;
	while (cnt > 0) {
		if (N % 2 == 0 || cnt == 1) {
			if (K >= two) N --;
			N = N / 2;
		}
		else {
			assert( N % 2 == 1 );
			N = N / 2;
			cerr << cnt << " " << K << endl;
			if (K < two && K >= (two / 2))
				K += two / 2;
			else
				if (K >= two && K - two < (two / 2))
					K -= two / 2;
			//cerr << cnt << " " << K << endl;
		}
		
		
		K = (K % two);
		two /= 2ll;
		cnt --;
	}
	return void(case_print(N));
}

int main() {
	ios_base::sync_with_stdio(0);
	freopen("C-large.in", "r",stdin);
	freopen("output2.txt", "w", stdout);
	
	int T;
	cin >> T;
	while (T --> 0) {
		long long N, K;
		cin >> N >> K;
		assert(K <= N);
		Solve(N, K);
		//SolveNaive(N ,K);
	}
	
	return 0;
}
