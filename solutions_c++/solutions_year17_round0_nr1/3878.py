#include <iostream>

using namespace std;


int getMinMoves(string S, int K) {
	int moves = 0;

	int ind = 0;
	for(int i = 0; i < S.length(); i++) {
		int cur, dir;
		if(i % 2 == 0) {
			cur = ind;
			dir = 1;
		} else {
			cur = (S.length()-ind-1);
			dir = -1;
			ind++;
		}

		int endPoint = cur+K*dir;
		if(S[cur] == '+' || endPoint < -1 || endPoint > S.length()) { continue; }
		for(; cur*dir < endPoint*dir; cur += dir) {
			S[cur] = (S[cur] == '+') ? '-' : '+';
		}
		moves++;
	}

	// Check if result is valid
	for(int i = 0; i < S.length(); i++) {
		if(S[i] == '-') {
			moves = -1;
			break;
		}
	}

	return moves;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T, K;
	string S;
	cin >> T;

	string cakes;
	for(int i = 0; i < T; i++) {
		cin >> S >> K;
		int moves = getMinMoves(S, K);
		if(moves != -1) {
			cout << "Case #" << (i+1) << ": " << moves << endl;
		} else {
			cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
