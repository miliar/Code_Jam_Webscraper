#include <bits/stdc++.h>
using namespace std;
int n, k;
struct node {
	string s;
	int w;
};
int check(string str) {
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '-')
			return 0;
	}
	return 1;
}
node newnode(string str, int cost) {
	node n;
	n.s = str;
	n.w = cost;
	return n;
}
map<string, int> visited;
queue<node> q;
int dijkstra(string sr) {
	visited.clear();
	visited[sr] = 1;
	while (!q.empty()) {
		q.pop();
	}
	node nw = newnode(sr, 0);
	q.push(nw);
	while (!q.empty()) {
		node currnet = q.front();
		q.pop();
		if (check(currnet.s) == 1) {
			return currnet.w;
		}
		for (int i = 0; i <= (int)sr.size()- k; i++) {

			string sqr = currnet.s;
			for (int j = i; j < k + i; j++) {
				if (currnet.s[j] == '+') {
					sqr[j] = '-';
				} else {
					sqr[j] = '+';
				}
			}
			map<string, int>::iterator it;
			it = visited.find(sqr);
			if (it != visited.end())
				continue;
			visited[sqr] = 1;
			node n = newnode(sqr, currnet.w + 1);
			q.push(n);
		}
	}
	return -1;
}
int main() {
	int t;
	string ss;
	freopen("out.txt", "w", stdout);
	cin>>t;
	int coot = 0;
	while (t--) {
		coot++;
		cin >> ss;
		cin>>k;
		n = ss.size();
		int ret = dijkstra(ss);
		 if (ret == -1) {
		 cout<<"Case #"<<coot<<": IMPOSSIBLE"<<endl;
		 } else {
		 cout<<"Case #"<<coot<<": "<<ret<<endl;
		 }
	}
}
