#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

template<class T>bool chmax(T &a, const T &b) { return (a<b)?(a=b,1):0;}
template<class T>bool chmin(T &a, const T &b) { return (b<a)?(a=b,1):0;}

using namespace std;
using ll=long long;

int Hd,Ad,Hk,Ak,B,D;
int memo[110][110][210][210];


int main(void){
	int T;
	cin >> T;
	rep(testcase,1,T+1){
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

		using state = tuple<int,int,int,int>;
		int ans = -1;

		rep(a,110)rep(b,110)rep(c,110)rep(d,110) memo[a][b][c][d]=-1;

		queue<state> q;
		q.push(state(Hd,Hk,0,0));
		memo[Hd][Hk][0][0]=1;

		while(!q.empty()){
			state cur = q.front(); q.pop();
			int ca,cb,cc,cd;
			tie(ca,cb,cc,cd)=cur;

			const int ctrun = memo[ca][cb][cc][cd];
			const int cAd=Ad+B*cc;
			const int cAk=max(0,Ak-D*cd);

			//Attack
			if(cb-cAd<=0){
				ans = ctrun;
				break;
			}

			//Attack
			if(ca-cAk>0){
				const int na = ca -cAk;
				const int nb = cb -cAd;
				const int nc = cc;
				const int nd = cd;
				
				if(memo[na][nb][nc][nd]==-1){
					memo[na][nb][nc][nd] = ctrun +1;
					q.push(state(na,nb,nc,nd));
				}
			}

			//Buff
			if(ca-cAk>0 and B!=0){
				const int na = ca -cAk;
				const int nb = cb;
				const int nc = cc + 1;
				const int nd = cd;
				
				if(memo[na][nb][nc][nd]==-1){
					memo[na][nb][nc][nd] = ctrun +1;
					q.push(state(na,nb,nc,nd));
				}
			}


			//Cure
			if(Hd-cAk>0){
				const int na = Hd -cAk;
				const int nb = cb;
				const int nc = cc;
				const int nd = cd;
				
				if(memo[na][nb][nc][nd]==-1){
					memo[na][nb][nc][nd] = ctrun +1;
					q.push(state(na,nb,nc,nd));
				}
			}

			//Debuff
			const int nAk = max(0,Ak-D*cd-D);
			if(ca- nAk >0 and D!=0){
				const int na = ca - nAk;
				const int nb = cb;
				const int nc = cc;
				const int nd = cd + 1;
				
				if(memo[na][nb][nc][nd]==-1){
					memo[na][nb][nc][nd] = ctrun +1;
					q.push(state(na,nb,nc,nd));
				}
			}
		}

		
		cout << "Case #" << testcase << ": ";

		if(ans==-1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;

	}
	return 0;
}