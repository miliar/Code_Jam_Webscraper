#include <bits/stdc++.h>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it)
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define READ(a) int a; 0 == scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(_i,n){ 0 == scanf("%d", &v[_i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;
#define cpx complex<double>
#define MOD 1000000007ll
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define MAXN 100000

int r, c;
vector<string> board;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dc[5] = {'-', '|', '-', '|', '-'};

bool onBoard(int x, int y){
	return x>=0 && x<r && y>=0 && y<c;
}

int f2(int d){
	if(d<=1) return 1-d;
	return 5-d;
}

int f(int d){
	return 3-d;
}

pair<int, pii> findLaser(pii p, int d){
	int xxx = p.ff+dx[d];
	int yyy = p.ss+dy[d];

	if(!onBoard(xxx,yyy)) return mp(-1, mp(-1, -1));
	// cout<<"."<<xxx<<yyy<<d<<endl;

	if(board[xxx][yyy] == '*' || board[xxx][yyy] == '-' || board[xxx][yyy] == '|') return mp(d, mp(xxx,yyy));
	if(board[xxx][yyy]=='/'){return findLaser(mp(xxx,yyy), f(d));}
	if(board[xxx][yyy]=='\\'){return findLaser(mp(xxx,yyy), f2(d));}
	if(board[xxx][yyy] == '#') return mp(-1, mp(-1,-1));
	// cout<<mp(xxx,yyy).ff<<mp(xxx,yyy).ss<<d<<endl;
	return findLaser(mp(xxx,yyy), d);
}

bool solve(){
	FOR(i, r) FOR(j, c){
		if(board[i][j]=='*'){
			auto l0 = findLaser(mp(i,j), 0);
			auto l1 = findLaser(mp(i,j), 1);
			auto l2 = findLaser(mp(i,j), 2);
			auto l3 = findLaser(mp(i,j), 3);
			if(l0.ff != -1 || l2.ff != -1) board[i][j] = '|';
			if(l1.ff != -1 || l3.ff != -1){
				if(board[i][j] == '|') return false;
				board[i][j] = '-';
			}
		}
	}

	vector<pair<pair<int, pii>,pair<int, pii>>> ors;
	FOR(foo, max(r,c))
	FOR(i, r) FOR(j, c){
		if(board[i][j]=='.'){
			auto l0 = findLaser(mp(i,j), 0);
			auto l1 = findLaser(mp(i,j), 1);
			auto l2 = findLaser(mp(i,j), 2);
			auto l3 = findLaser(mp(i,j), 3);
			// cout<<"done1"<<endl;
			if(l0.ff==-1) l0 = l2;
			if(l1.ff==-1) l1 = l3;
			if(l0.ff == -1 && l1.ff == -1) return false;
			// cout<<l0.ff<<" "<<l0.ss.ff<<" "<<l0.ss.ss<<" "<<l1.ss.ff<<" "<<l1.ss.ss<<endl;
			// if(l0.ff!=-1) cout<<(board[l0.ss.ff][l0.ss.ss] != dc[l0.ff+1])<<endl;
			// cout<<board[l0.ss.ff][l0.ss.ss]<<board[l1.ss.ff][l1.ss.ss]<<endl;
			if(l0.ff==-1 || board[l0.ss.ff][l0.ss.ss] == dc[l0.ff+1]){
				// cout<<"a"<<endl;
				if(l1.ff==-1) return false;
				if(board[l1.ss.ff][l1.ss.ss] == dc[l1.ff+1]) return false;
				board[l1.ss.ff][l1.ss.ss] = dc[l1.ff];
			}else if(l1.ff==-1 || board[l1.ss.ff][l1.ss.ss] == dc[l1.ff+1]){
				// cout<<"b"<<endl;
				if(l0.ff==-1) return false;

				if(board[l0.ss.ff][l0.ss.ss] == dc[l0.ff+1]) return false;
				board[l0.ss.ff][l0.ss.ss] = dc[l0.ff];
			}else{
				ors.pb(mp(l0, l1));
				// cout<<"!!!!!"<<l0.ss.ff<<" "<<l0.ss.ss<<" "<<l1.ss.ff<<" "<<l1.ss.ss<<endl;
			}
		}
	}
			// cout<<"done2"<<endl;


	FOR(i, r) FOR(j, c){
		if(board[i][j]=='*'){
			board[i][j]='-';
		}
	}
	return true;
}

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		cin >>r>>c;
		board.clear();
		FOR(i, r){
			string s;
			cin>>s;
			FOR(j, s.length()){
				if(s[j]=='-' || s[j]=='|') s[j]='*';
			}
			board.pb(s);
		}
		auto res = solve();
		if(!res){
			cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
			// FOR(i, r){
			// 	cout<<board[i]<<endl;
			// }
		}else{
			cout<<"Case #"<<(t+1)<<": "<<"POSSIBLE"<<endl;
			FOR(i, r){
				cout<<board[i]<<endl;
			}
		}
	}
	return 0;
}