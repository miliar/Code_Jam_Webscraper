#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;

struct node{
	int mh, oh;
	int mb, ob;
	int dist;
};


int hd, ad, hk, ak, b, d;
bool vis[105][105][105][105];

bool enqueue(queue<node> &que, int a, int b, int c, int dd, int e){
	if(b <= 0) return 1;
	a -= max(0, ak - d * dd);
	if(a <= 0) return 0;
	if(c > 101 || dd > 101) return 0;
	if(vis[a][b][c][dd]) return 0;
	vis[a][b][c][dd] = 1;
	que.push({a, b, c, dd, e + 1});
	return 0;
}

int solve(){
	memset(vis, 0, sizeof(vis));
	queue<node> que;
	cin >> hd >> ad >> hk >> ak >> b >> d;
	que.push({hd, hk, 0, 0, 0});
	vis[hd][hk][0][0] = 1;
	while(!que.empty()){
		auto x = que.front();
		que.pop();
		bool ans1 = enqueue(que, x.mh, x.oh - ad - b * x.mb, x.mb, x.ob, x.dist);
		bool ans2 = enqueue(que, x.mh, x.oh, x.mb + 1, x.ob, x.dist);
		bool ans3 = enqueue(que, hd, x.oh, x.mb, x.ob, x.dist);
		bool ans4 = enqueue(que, x.mh, x.oh, x.mb, x.ob + 1, x.dist);
		if(ans1||ans2||ans3||ans4){
			return x.dist;
		}
	}
	return -1;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int x = solve();
		if(x == -1) printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i, x + 1);
	}
}
