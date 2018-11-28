#include <bits/stdc++.h>
using namespace std;

typedef struct Node {
	int l, r;
	Node() {}
	Node(int l, int r) : l(l), r(r) {}
	friend bool operator<(const Node a, const Node b) {
		if(a.r-a.l != b.r-b.l) return a.r-a.l < b.r-b.l;
		if(a.l != b.l) return a.l < b.l;
		return a.r < b.r;
	}
}Node;

int n, k;
priority_queue<Node> pq;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d",&n,&k);
		while(!pq.empty()) pq.pop();
		pq.push(Node(1, n));
		for(int i = 0; i < k-1; i++) {
			Node t = pq.top(); pq.pop();
			int cut = (t.l + t.r) / 2;
			if(t.l <= cut - 1) pq.push(Node(t.l, cut-1));
			if(cut + 1 <= t.r) pq.push(Node(cut+1, t.r));
		}
		Node t = pq.top(); pq.pop();
		int cut = (t.l + t.r) / 2;
		int l = cut - t.l;
		int r = t.r - cut;
		printf("Case #%d: ", _++);
		cout << max(l, r) << " " << min(l, r) << endl;
	}
	return 0;
}