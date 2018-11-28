#include <iostream>
#include <vector>
#include <assert.h>

using namespace std;

#define ll long long

vector<ll> split(ll N) { // N >= 0
	vector <ll> result;
	ll tmp = N / 2;
	result.push_back(N - tmp);
	result.push_back(tmp);
	return result;
}

void read(vector<ll> A) {
	cout << "there are " << A[2] << " intevals of length " << A[0] << endl;
	cout << "there are " << A[3] << " intevals of length " << A[1] << endl;
}

vector<ll> iterate(vector<ll> A) {
	//A of length 4: large inteval, small inteval, #large, #small
	assert(A.size() == 4);
	vector<ll> large = split(A[0] - 1);
	vector<ll> small = split(A[1] - 1);
	vector<ll> result;
	result.push_back(large[0]);
	result.push_back(small[1]);
	int numLarge = A[2], numSmall = A[3];
	if (large[1] == large[0]) numLarge += A[2];
	else numSmall += A[2];
	if (small[0] == large[0]) numLarge += A[3];
	else numSmall += A[3];
	result.push_back(numLarge);
	result.push_back(numSmall);
	return result;
}

vector<ll> stalls(ll N, ll K) {
	vector<ll> result;
	if (K == 1) {
		result = split(N - 1);
		return result;
	}
	// 1, 2, 4, ..., 2^e, t = K with 1 <= t <= 2^(e+1) and e >= 0
	int e = 0;
	while (K > (1LL << (e + 2)) - 1) {
		e ++;
	}
	ll t = K - (1LL << (e + 1)) + 1;
	ll tmpArray[4] = {(N - 1) - (N - 1) / 2, (N -1) / 2, 1, 1};
	vector<ll> tmpVector  = vector<ll>(begin(tmpArray), end(tmpArray));
	for (int i = 0; i < e; i ++) {
		tmpVector = iterate(tmpVector);
		//large interval, small interval, # large, # small
	}
	if (t <= tmpVector[2]) {
		result = split(tmpVector[0] - 1);
	} else {
		result = split(tmpVector[1] - 1);
	}
	return result;
}

int main() {
	int T;
	cin >> T;
	ll N, K;
	for (int i = 0; i < T; i ++) {
		cin >> N >> K;
		vector<ll> result = stalls(N, K);
		cout << "Case #" << i + 1 << ": " << result[0] << ' ' << result[1] << endl;
	}
	return 0;
}
