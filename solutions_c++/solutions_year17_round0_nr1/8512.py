#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
	int n;
	cin >> n;

	for(int i = 1; i < n+1; i++) {
		cout << "Case #" << i << ": ";
		string x;
		cin >> x;

		int k;
		cin >> k;

		queue<string> bfs;
		unordered_map<string, int> depth;

		bfs.push(x);
		depth.insert({x, 0});

		bool found = false;

		while(bfs.size()) {
			string& curr = bfs.front();

			bfs.pop();
			int dist = depth.find(curr)->second;

			bool goodState = true;
			for(int j = 0; j < curr.size(); j++) {
				if(curr[j] != '+') {
					goodState = false;
					break;
				}
			}

			if(goodState) {
				found = true;
				cout << dist << '\n';
				break;
			}

			//enqueue all states
			string y = curr;
			for(int l = 0; l < k; l++) {
				if(y[l] == '-') {
					y[l] = '+';
				}
				else {
					y[l] = '-';
				}
			}

			if(depth.find(y) == depth.end()) {
				depth.insert({y, dist+1});
				bfs.push(y);
			}

			for(int j = k; j < curr.size(); j++) {
				if(y[j-k] == '-') {
					y[j-k] = '+';
				}
				else {
					y[j-k] = '-';
				}

				if(y[j] == '-') {
					y[j] = '+';
				}
				else {
					y[j] = '-';
				}

				if(depth.find(y) == depth.end()) {
					depth.insert({y, dist+1});
					bfs.push(y);
				}
			}
		}

		if(!found) {
			cout << "IMPOSSIBLE\n";
		}
	}
}