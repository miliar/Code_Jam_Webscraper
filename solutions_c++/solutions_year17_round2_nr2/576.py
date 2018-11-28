#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

struct Node {
	char color;
	int cnt;
	
}node[3];
bool cmp(Node &A, Node &B) {
		return A.cnt > B.cnt;
	}
int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int N;
		cin >> N;
		int R, O, Y, G, B, V;
		cin >> R >> O >> Y >> G >> B >> V;
		node[0].color = 'R';
		node[0].cnt = R;
		node[1].color = 'Y';
		node[1].cnt = Y;
		node[2].color = 'B';
		node[2].cnt = B;
		sort(node, node + 3, cmp);
		cout <<"Case #"<<cas<<": ";
		if (node[0].cnt > node[1].cnt + node[2].cnt) {
			cout <<"IMPOSSIBLE"<<endl;
			continue;
		}
		string str = "";
		for (int i = 0; i < node[2].cnt + node[1].cnt - node[0].cnt; i++) {
			str += node[0].color;
			str += node[1].color;
			str += node[2].color;
		}
		int sum = node[2].cnt + node[1].cnt - node[0].cnt;

			node[0].cnt -= sum;
			node[1].cnt -= sum;
			node[2].cnt -= sum;
		//cout << str <<endl;
		while (node[1].cnt > 0) {
			str += node[0].color;
			str += node[1].color;
			node[0].cnt--;
			node[1].cnt--;
		}
		//cout << str <<endl;
		while (node[2].cnt > 0) {
			str += node[0].color;
			str += node[2].color;
			node[0].cnt--;
			node[2].cnt--;
		}
		cout << str<<endl;
		assert(str.length() == N);
	}
	return 0;
}