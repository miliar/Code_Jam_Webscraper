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
#define READV(v,n) vi v(n);FOR(i,n){ 0 == scanf("%d", &v[si]);}
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
#define MAXN 1005

int main(int argc, char *argv[]){
	READ(T);
	FOR(t, T){
		READ(n);
		READ(m);
		vector<vi> board(n,vi(n,0));
		FOR(i,m){
			char ch;
			int r,c;
			cin>>ch>>r>>c;
			if(ch=='x'){board[r-1][c-1] = 1;}
			if(ch=='+'){board[r-1][c-1] = 2;}
			if(ch=='o'){board[r-1][c-1] = 3;}
		}
		auto board2 = board;
		vi e, e2;
		FOR(i, n){
			bool bad = false;
			FOR(j, n){
				if(board2[i][j] & 1) {bad = true; break;}
			}
			if(!bad) e.pb(i);
		}
		FOR(j, n){
			FOR(i, n){
				if(board2[i][j] & 1) goto next;
			}
			e2.pb(j);
			next:
			continue;
		}
		FOR(i, sz(e)){
			board2[e[i]][e2[i]] |= 1;
		}

		set<int> u, u2;
		FOR(x, n) FOR(y, n){
			if(board2[x][y] & 2){
				u.insert(x+y);
				u2.insert(x-y);
			}
		}
		FOR(sum, n+n-1){
			if(u.count(sum)) continue;
			FOR(x, sum+1){
				int y = sum-x;
				if(y<0 || y>=n || x<0 || x>=n) continue;
				if(u2.count(x-y)) goto skip;
				board2[x][y] |= 2;
				u.insert(sum);
				u2.insert(x-y);
				break;
				skip:
				if(u2.count(y-x)) continue;
				board2[y][x] |= 2;
				u.insert(sum);
				u2.insert(y-x);
				break;
			}
		}
		// FOR(i, n) {FOR(j, n) cout<<board2[i][j]<<" "; cout<<endl;}
		int points = 0;
		vector<string> lines;
		int p[4] = {0, 1, 1, 2};
		char c[4] = {' ', 'x', '+', 'o'};
		FOR(i, n) FOR(j, n){
			points += p[board2[i][j]];
			if(board[i][j] == board2[i][j]) continue;
			stringstream ss;
			ss<<c[board2[i][j]]<<" "<<i+1<<" "<<j+1;
			lines.pb(ss.str());
		}
		cout<<"Case #"<<(t+1)<<": "<<points<<" "<<lines.size()<<endl;
		FOR(i, sz(lines)) cout<<lines[i]<<endl;
	}
	return 0;
}