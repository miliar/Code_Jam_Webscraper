#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++ cas) {
		long long n, K;
		scanf("%I64d %I64d", &n, &K);
		printf("Case #%d: ", cas);
		vector < pair <long long , long long> > A, B;
		A.push_back( {n, 1} );
		while(K) {
			sort(A.begin(), A.end());
			reverse(A.begin(), A.end());
			int sz = A.size(), p = 0;
			long long sum = 0;
			while(p < sz && A[p].first == A[0].first) {
				sum += A[p].second;
				++ p;
			}
			long long ls, rs;
			if(A[0].first & 1) {
				ls = rs = A[0].first / 2;
			} else {
				ls = A[0].first / 2 - 1;
				rs = ls + 1;
			}
			if(sum >= K) {
				printf("%I64d %I64d\n", rs, ls);
				break;
			}
			K -= sum;
			B.clear();
			for(int i = p; i < sz; ++ i)
				B.push_back(A[i]);
			if(ls == rs) {
				if(ls)
					B.push_back( {ls, sum * 2} );
			} else {
				if(rs)
					B.push_back( {rs, sum} );
				if(ls)
					B.push_back( {ls, sum} );
			}
			swap(A, B);
		}
	}
	return 0;
}