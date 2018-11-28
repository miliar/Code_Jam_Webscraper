#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

using ll = long long;
ll const INF = 1000000000;

int main(void) {

	ios::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	ll T;
	cin >> T;

	for (ll test = 1; test <= T; test++) {

		map<ll, ll> Q;

		ll N, K;

		cin >> N >> K;

		Q[N] = 1;

		ll num, cnt;
		for (ll i = 0; i < K; i+=cnt) {
			num = Q.rbegin()->first;
			cnt = Q.rbegin()->second;
			Q.erase(num);
			if (num % 2 == 0) {
				Q[num / 2] += cnt;
				Q[num / 2 - 1 ] += cnt;
			}
			else {
				Q[num / 2] += 2*cnt;
			}
		}

		if (num % 2 == 0) {
			cout << "Case #" << test << ": " << num / 2 << " " << num / 2 - 1 << "\n";
		}
		else {
			cout << "Case #" << test << ": " << num / 2 << " " << num / 2 << "\n";
		}
	

	}

	return 0;
}