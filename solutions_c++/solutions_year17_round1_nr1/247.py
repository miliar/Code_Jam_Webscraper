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

int main(void){
	int T;
	cin >> T;	
	rep(testcase,1,T+1){
		int R,C;
		string board[30];
		cin >> R >> C;
		rep(i,R) cin >> board[i];

		rep(i,R){
			char tmp = -1;
			rep(j,C) if(board[i][j]!='?') tmp=board[i][j];
			if(tmp == -1) continue;
			rrep(j,C){
				if(board[i][j]=='?')
					board[i][j]=tmp;
				else
					tmp=board[i][j];
			}
		}

		string tmp="";
		rep(i,R) if(board[i]!=string(C,'?')) tmp=board[i];

		rrep(i,R){
			if(board[i]==string(C,'?'))
				board[i]=tmp;
			else
				tmp=board[i];
		}

		
		cout << "Case #" << testcase << ": " << endl;
		rep(i,R) cout << board[i] << endl;
	}
	return 0;
}