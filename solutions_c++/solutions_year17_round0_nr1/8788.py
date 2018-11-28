//============================================================================
// Name        : PancakeFlipperSmall.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <queue>
using namespace std;

int n, k;
int target;
int mask;

int dist[1<<10];

int bfs(int initialState){
	queue<int> q;
	fill(dist,dist+(1<<10),5000);
	dist[initialState]=0;
	if (initialState == target) return 0;
	q.push(initialState);
	int current, nextState;
	while (! q.empty()){
		current = q.front(); q.pop();
		for (int i=0; i + k - 1 < n; i++){
			nextState = current ^ (mask << i);
			if (dist[nextState] == 5000) {
				dist[nextState] = dist[current] + 1;
				if (nextState == target) return dist[target];
				q.push(nextState);
			}
		}
	}
	return -1;
}

int toState(string &s){
	int r = 1, p = 1;
	for (int i = 0; i < (int)s.length(); i++){
		r*=2; p*=2;
		if (s[i]=='+')r++;
	}
	return r-p;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int TC;
	cin >> TC;
	string s;
	int c = 1;
	while (TC--){
		cout << "Case #" << c++ << ": ";
		cin >> s >> k;
		target = (1 << (s.size())) - 1;
		n = s.size();
		mask = (1 << k) - 1;
		int r = bfs(toState(s));
		if (r == -1){
			cout << "IMPOSSIBLE\n";
		} else {
			cout << r << "\n";
		}
	}
}
