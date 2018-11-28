#include <bits/stdc++.h>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

map<int,int> vis;
int orig, k;
string s;

void show(int x){
	printf("At ");
	for(int i = 0; i < s.size(); i++){
		printf("%c",'0'+(bool)(x&(1<<i)));
	}
	printf("\n");
}

int bfs(){
	vis[orig] = 0;
	queue<int> q;
	q.push(orig);
	while(!q.empty()){
		int x = q.front(); q.pop();
		//show(x);
		for(int i = 0; i < s.size()-k+1; i++){
			int y = x;
			for(int j = 0; j < k; j++){
				y ^= (1 << (i+j));
			}
			if(!vis.count(y)) {
				vis[y] = vis[x]+1;
				q.push(y);
			}
		}
	}
	int mh = 0;
	for(int i = 0; i < s.size(); i++){
		mh |= (1 << i);
	}
	if(vis.count(mh)) return vis[mh];
	return -1;
}

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		cin >> s >> k;
		vis.clear();
		orig = 0;
		for(int i = 0; i < s.size(); i++){
			orig |= ((s[i] == '+')<<i);
		}
		//show(orig);
		printf("Case #%d: ",caso);
		int ans = bfs();
		if(ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);		
	}
	return 0;
}
