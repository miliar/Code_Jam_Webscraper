#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef struct Node {
	int hd, hk, ad, ak;
	Node() {}
	Node(int a, int b, int c, int d) : 
		hd(a), hk(b), ad(c), ak(d) {}
	friend bool operator<(const Node& a, const Node& b) {
    pair<pii, pii> x = make_pair(make_pair(a.hd, a.hk), make_pair(a.ad, a.ak));
    pair<pii, pii> y = make_pair(make_pair(b.hd, b.hk), make_pair(b.ad, b.ak));
    return x < y;
  }
}Node;

const int maxn = 110;
int hd, ad, hk, ak, b, d;
queue<Node> q;
map<Node, int> dp;

int bfs() {
	dp.clear();
	while(!q.empty()) q.pop();
	dp[Node(hd, hk, ad, ak)] = 1;
	q.push(Node(hd, hk, ad, ak));
	while(!q.empty()) {
		Node p = q.front(); q.pop();

		Node tmp = p;
		tmp.hk -= tmp.ad;
		if(tmp.hk <= 0) {
			return dp[p] + 1;
		}
		
		tmp.hd -= tmp.ak;
		if(tmp.hd > 0 && !dp[tmp]) {
			dp[tmp] = dp[p] + 1;
			q.push(tmp);
		}

		tmp = p;
		tmp.ad += b;
		tmp.hd -= tmp.ak;
		if(tmp.hd > 0 && !dp[tmp]) {
			dp[tmp] = dp[p] + 1;
			q.push(tmp);
		}

		tmp = p;
		tmp.hd = hd;
		tmp.hd -= tmp.ak;
		if(tmp.hd > 0 && !dp[tmp]) {
			dp[tmp] = dp[p] + 1;
			q.push(tmp);
		}

		tmp = p;
		tmp.ak -= d;
		if(tmp.ak < 0) tmp.ak = 0;
		tmp.hd -= tmp.ak;
		if(tmp.hd > 0 && !dp[tmp]) {
			dp[tmp] = dp[p] + 1;
			q.push(tmp);
		}
	}
	return -1;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	cerr << "Begin: " << endl;
	while(T--) {
		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
		printf("Case #%d: ", _++);
		int ret = bfs();
		if(ret == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ret - 1);
		cerr << "Case " << _ - 1 << " Done." << endl;
	}
	return 0;
}
