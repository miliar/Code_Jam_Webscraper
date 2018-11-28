#include <iostream>
#include <cstdio>
#include <cmath>
typedef long long ll;
using namespace std;

ll N;

ll b_slove() {
	while (true) {
	ll tmp = N;
	while (tmp/10 != 0) {
		if (tmp%10 < tmp/10%10) break;
		if (tmp%10 == 0) break;
		tmp /= 10;
	}
	if (tmp/10 == 0) return N;
	N -= 1;
	}
	return N;
}

ll slove() {
	while(true) {
		int r = 0;
		ll tmp = N, b = 1;
		//cout << N << endl;
		while (tmp/10 != 0) {
			if (tmp%10 < tmp/10%10) break;
			tmp /= 10;
		}
		if (tmp/10 == 0) return N;
		tmp = N;
		while (tmp % 10 == 9) {
			r += 1;
			tmp /= 10;
		}
		for (int i =0; i< r; ++i) b *= 10;
		N = N-b;
	}
	return slove();
}

int main() {

	freopen("B-large.in", "r", stdin);
	int T;
	cin >> T;
	for (int i=0; i<T; ++i){
		cin >> N;
		printf("Case #%d: %lld\n", i+1, slove());
	}

}
