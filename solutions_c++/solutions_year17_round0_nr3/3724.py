#include <iostream>
#include <utility>
#include <queue>
#define ll long long int
using namespace std;
typedef pair<ll, ll> pll;

pll split(ll length) {
	if(length % 2 == 0) {
		return make_pair((length - 1)/2+1, (length-1)/2);
	} else {
		return make_pair((length - 1)/2, (length - 1)/2);
	}
}

pll solve(ll N, ll K) {
	priority_queue<ll> q;
	q.push(N);
	ll moves = 0;
	while(true) {
		moves++;
		ll to_do = q.top(); q.pop();
		pll to_add = split(to_do);
		if(to_add.first > 0) {
			q.push(to_add.first);
		}
		if(to_add.second > 0) {
			q.push(to_add.second);
		}
		if(moves == K) {
			return make_pair(to_add.first, to_add.second);
			break;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for(int z = 1; z <= T; z++) {
		ll N, K;
		cin >> N >> K;
		pll answer = solve(N, K);
		cout << "Case #" << z << ": " << answer.first << " " << answer.second << endl;
	}
}