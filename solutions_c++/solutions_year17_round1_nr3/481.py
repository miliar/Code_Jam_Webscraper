#include <bits/stdc++.h>

using namespace std;

struct Node {
	int hd, ad, hk, ak;
	int dist;
};

bool visited[101][101][301][101];

int ihd, iad, ihk, iak, b, d;


int best(int hd, int hk, int ad, int ak) {
	if(hd == 0) {
		return INT_MAX;
	}
	else if(hk == 0) {
		return 0;
	}
		
	int score = best(hd - ak, hk - ad, ad, ak); // attack
	score = min(best(hd - ak, hk, ad + b, ak), score); // buff
	score = min(best(ihd - ak, hk, ad, ak), score); // cure
	score = min(best(hd - (ak - d), hk, ad, max(ak - d, 0)), score); // debuff

	if(score == INT_MAX) {
		return INT_MAX;
	}
	else {
		return score + 1;
	}
}

void runTestCase(int t) {
	cin >> ihd >> iad >> ihk >> iak >> b >> d;

	for(int i = 0; i < 101; i++) {
		for(int j = 0; j < 101; j++) {
			for(int k = 0; k < 301; k++) {
				for(int l = 0; l < 101; l++) {
					visited[i][j][k][l] = false;
				}
			}
		}
	}

	Node start;
	start.hd = ihd;
	start.ad = iad;
	start.hk = ihk;
	start.ak = iak;
	start.dist = 0;

	queue<Node> bfs;
	bfs.push(start);

	int ans = -1;
	while(bfs.size() > 0) {
		Node node = bfs.front();
		bfs.pop();

		if(node.hk == 0) {
			ans = node.dist;
			break;
		}
		else if(node.hd == 0) {
			continue;
		}
		else if(node.ad > 250) {
			continue;
		}

		if(visited[node.hd][node.hk][node.ad][node.ak]) {
			continue;
		}
		else {
			visited[node.hd][node.hk][node.ad][node.ak] = true;
		}


		Node attack = node;
		attack.hd = max(node.hd - node.ak, 0);
		attack.hk = max(node.hk - node.ad, 0);
		attack.dist++;
		bfs.push(attack);
		
		Node buff = node;
		buff.hd = max(node.hd - node.ak, 0);
		buff.ad += b;
		buff.dist++;
		bfs.push(buff);

		Node cure = node;
		cure.hd = max(ihd - node.ak, 0);
		cure.dist++;
		bfs.push(cure);

		Node debuff = node;
		debuff.ak = max(node.ak - d, 0); debuff.hd = max(node.hd - debuff.ak, 0);
		debuff.dist++;
		bfs.push(debuff);
	}

	cout << "Case #" << t << ": ";
	if(ans == -1) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << ans << endl;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
