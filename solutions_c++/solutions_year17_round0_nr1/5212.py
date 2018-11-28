#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;
unordered_set<string> visited;
int ans = -1;

bool bfs(int depth, const vector<string> queue, int K) {
	if (queue.empty()) {
		return false;
	}
	vector<string> queue_check;
	for (int i=0; i<queue.size(); ++i) {
		string S;
		S = queue[i];
		//cout << "checking S=" << S << " depth=" << depth << endl;
		bool ok = true;
		for (int i=0; i<S.length(); ++i) {
			if (S[i] == '-') {
				ok = false;
				break;
			}
		}
		if (ok) {
			ans = depth;
			return true;
		}
		if (visited.find(S) != visited.end()) {
			continue;
		}
		visited.insert(S);
		for (int i=0; i<=S.length()-K; ++i) {
			string S_check = S;
			for (int j=0; j<K; ++j) {
				S_check[i+j] = S_check[i+j] == '+' ? '-' : '+';
			}
			queue_check.push_back(S_check);
		}
	}
	/*
	cout << "queue for next depth" << endl;
	for (int i=0; i<queue_check.size(); ++i)
		cout << queue_check[i] << endl;
	*/
	if (bfs(depth + 1, queue_check, K))
		return true;
	return false;
}

int main() {
	string S;
	int T, K;
	cin >> T;
	for (int i=0; i<T; ++i) {
		cin >> S;
		cin >> K;
		visited.clear();
		vector<string> queue;
		queue.push_back(S);
		if (!bfs(0, queue, K))
			cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << (i+1) << ": " << ans << endl;
	}
}