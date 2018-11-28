#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int solve(string data, int k) {
	bool marked[data.size()];
	for (int i = 0; i < data.size(); i++)
		marked[i] = data[i] == '+';

	int cnt = 0;

	for (int i = 0; i + k <= data.size(); i++) {
		if (!marked[i]) {
			//printf("found unmarked at position (%d), inverting all guys until position (%d) \n", i, i + k -1);
			cnt++;
			for (int j = i; j < i + k; j++)
				marked[j] = !marked[j];
		}
	}

	for (int i = 0; i < data.size(); i++) {
		//printf("(%d) [%d] ", i, marked[i]);
		if (!marked[i])
			return -1;
	}

	return cnt;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string inp;
		int k;
		cin >> inp >> k;
		printf("Case #%d: ", t);
		int res = solve(inp, k);
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 0;
}