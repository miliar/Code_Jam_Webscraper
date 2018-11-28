#include <iostream>
#include <utility>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long ll;




pair<int, int> solve(ll N, ll K) {	
	priority_queue<ll> q;
	q.push(N);

	for(int i = 0; i < K - 1; i++) {

		ll largestPiece = q.top();
		q.pop();
		q.push(largestPiece / 2);
		if(largestPiece % 2 == 0) {
			q.push(largestPiece / 2 - 1);
		} else {
			q.push(largestPiece / 2);
		}
	}
	ll largestPiece = q.top();
	if(largestPiece % 2 == 0) {
		return make_pair(largestPiece / 2 -1, largestPiece/2);
	} else {
		return make_pair(largestPiece/2 , largestPiece/2);
	}

	
}

int main() {

	
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	ll N, K;
	for(int t = 1; t <= T; t++) {
		cin >> N >> K;
		
		pair<int, int> sol = solve(N, K);
		cout << "Case #" << t << ": " << sol.second << " " << sol.first << "\n";

	}

	return 0;
}