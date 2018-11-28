#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define rev(i,n) for(i=n;i>=0;i--)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define INF 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

void solve(){
	string s[30];
	int R,C;
	cin >> R >> C;
	queue< pair<int,int> > q,qq;
	for(int i = 0; i < R; i++) {
		cin >> s[i];
		for(int j = 0; j < C; j++){
			if(s[i][j] != '?'){
				q.push({i,j});
				qq.push({i,j});
			}
		}
	}
	int nx,ny;
	while(! q.empty()){
		auto p = q.front(); q.pop();
		nx = p.first;
		ny = p.second-1;
		while( ny >= 0 and s[nx][ny] == '?') s[nx][ny--] = s[p.first][p.second];
		ny = p.second+1;
		while( ny < C and s[nx][ny] == '?') s[nx][ny++] = s[p.first][p.second];
	}
	for(int i = 0; i < R; i++) {
		if(s[i][0] == '?'){
			if(i) s[i] = s[i-1];
			else s[i] = s[i+1];
		}
	}
	for(int i = R-1; i >= 0; i--){
		if(s[i][0] == '?'){
			if(s[i][0] == '?'){
				if( i != (R-1) ) s[i] = s[i+1];
				else s[i] = s[i-1];
			}
		}
	}
	for(int i = 0; i < R; i++) cout << s[i] << endl;
}

int main(){
	int t;
	cin >> t;
	int i = 1;
	while(t--) {
		printf("Case #%d:\n",i++);
		solve();
	}
}
