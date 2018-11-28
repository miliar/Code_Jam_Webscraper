#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

void print_answer(long long N) {
	cout << N/2 << " " << (N-1)/2 << endl;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int NumberOfTestCases;
	cin >> NumberOfTestCases;
	for(int TC = 1; TC <= NumberOfTestCases; TC++) {
		cout << "Case #" << TC << ": ";
		long long n, k;
		cin >> n >> k;
		long long cnt1 = 1, cnt2 = 0, N = n;
		while(k > 0) {
			long long CNT1 = 0, CNT2 = 0, _N = N/2;
			if(k <= cnt1) {
				print_answer(N);
				break;
			}
			else {
				k -= cnt1;
				if(N % 2) CNT1 += 2*cnt1;
				else {
					CNT1 += cnt1;
					CNT2 += cnt1;
				}
			}
			if(k <= cnt2) {
				print_answer(N-1);
				break;
			}
			else {
				k -= cnt2;
				if(N % 2) {
					CNT1 += cnt2;
					CNT2 += cnt2;
				}
				else CNT2 += 2*cnt2;
			}
			N = _N;
			cnt1 = CNT1;
			cnt2 = CNT2;
		}
	}
	return 0;
}