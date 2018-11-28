#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;

bool myfunction(long long i, long long j) { return (i>j); }

void solve(long long _N, long long _K, long long *_L, long long *_R) {
	vector <long long> mylist;
	long long L1, R1;
	mylist.push_back(_N);
	for (int i = 0; i < _K; i++) {
		L1 = mylist[0] / 2;
		R1 = mylist[0] - 1 - L1;

		//mylist[0] = L1;
		//mylist.push_back(R1);

		if (mylist[0] == 1) {
			mylist.erase(mylist.begin());
		}
		else if (mylist[0] == 2) {
			mylist[0] = 1;
		}
		else {
			mylist[0] = L1;
			mylist.push_back(R1);
		}
		sort(mylist.begin(), mylist.end(), myfunction);
	}
	*_L = L1;
	*_R = R1;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("C-small-1-attempt4.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		long long N, K;
		scanf("%lld %lld\n", &N, &K);

		printf("Case #%d: ", i);
		long long L, R;
		solve(N, K, &L, &R);
		printf("%lld %lld", max(L, R), min(L, R));
		printf("\n");
	}

	return 0;
}