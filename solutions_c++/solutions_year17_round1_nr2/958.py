#include <bits/stdc++.h>

using namespace std;

struct Node {
	int wt;
	int minser, maxser;
	vector<int> edges;
	vector<bool> taken;
};

int n, p;
vector<int> recipe;
vector<vector<Node>> graph;

bool augment(int ) {
}

void runTestCase(int t) {
	cin >> n >> p;

	//reset
	recipe.clear();
	recipe.resize(n);
	graph.clear();
	graph.resize(n, vector<Node>(p));

	for(int i = 0; i < n; i++) {
		int ing;
		cin >> recipe[i];
	}

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < p; j++) {
			int wt;
			cin >> wt;
			graph[i][j].wt = wt;
			graph[i][j].minser = (int) ceil(wt*.9 / (recipe[i]));
			graph[i][j].maxser = (int) floor(wt*1.1 / (recipe[i]));
			//cout << "i: " << i << "j: " << j << " " << graph[i][j].minser << " " << graph[i][j].maxser << endl;
		}
	}

	cout << "Case #" << t << ": ";
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
