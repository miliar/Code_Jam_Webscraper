#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

#ifdef PRINTERS
#include "printers.hpp"
using namespace printers;
#define tr(a)		cerr<<#a<<": "<<a<<endl;
#else
#define tr(a)    
#endif

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a,b)	for(int i=a;i<b;i++)
using namespace std;
int test=1;
void solve(){
	cout<<"Case #"<<test++<<": ";
	int R,O,Y,G,B,V,N;
	cin>>N>>R>>O>>Y>>G>>B>>V;
	if(R>B+Y or B>R+Y or Y>R+B){
		cout<<"IMPOSSIBLE\n";
		return;
	}
	if(R==0 and B==0){
		cout<<"IMPOSSIBLE\n";
		return;	
	}
	if(Y==0 and B==0){
		cout<<"IMPOSSIBLE\n";
		return;	
	}
	if(R==0 and Y==0){
		cout<<"IMPOSSIBLE\n";
		return;	
	}
	if(R==0){
		if(B==Y){
			string ans;
			rep(i,0,B)ans+="BY";
			cout<<ans<<endl;
			return;
		}
		cout<<"IMPOSSIBLE\n";
		return;
	}
	if(B==0){
		if(R==Y){
			string ans;
			rep(i,0,R)ans+="RY";
			cout<<ans<<endl;
			return;
		}
		cout<<"IMPOSSIBLE\n";
		return;
	}
	if(Y==0){
		if(R==B){
			string ans;
			rep(i,0,R)ans+="RB";
			cout<<ans<<endl;
			return;
		}
		cout<<"IMPOSSIBLE\n";
		return;
	}
	if(R>=B and R>=Y){
		string ans="R";
		priority_queue<pair<int,char>>pq;
		pq.push(mp(B,'B'));
		pq.push(mp(Y,'Y'));
		rep(i,1,R){
			if(pq.empty()){
				cout<<"IMPOSSIBLE\n";
				return;
			}
			auto cur=pq.top();
			pq.pop();
			ans+=cur.S;
			if(cur.S=='B')B--;
			if(cur.S=='Y')Y--;
			ans+="R";
			cur.F--;
			pq.push(cur);
		}
		if(abs(B-Y)>1){
			cout<<"IMPOSSIBLE\n";
			return;
		}
		if(B==Y){
			rep(i,0,B)ans+="BY";
			cout<<ans<<endl;
			return;
		}
		if(B>Y){
			ans+="B";
			rep(i,0,Y)ans+="YB";
			cout<<ans<<endl;
			return;	
		}
		if(Y>B){
			ans+="Y";
			rep(i,0,B)ans+="BY";
			cout<<ans<<endl;
			return;
		}
	}
	if(Y>=R and Y>=B){
		string ans="Y";
		priority_queue<pair<int,char>>pq;
		pq.push(mp(B,'B'));
		pq.push(mp(R,'R'));
		rep(i,1,Y){
			if(pq.empty()){
				cout<<"IMPOSSIRLE\n";
				return;
			}
			auto cur=pq.top();
			pq.pop();
			ans+=cur.S;
			if(cur.S=='R')R--;
			if(cur.S=='B')B--;
			ans+="Y";
			cur.F--;
			pq.push(cur);
		}
		if(abs(R-B)>1){
			cout<<"IMPOSSIRLE\n";
			return;
		}
		if(R==B){
			rep(i,0,R)ans+="RB";
			cout<<ans<<endl;
			return;
		}
		if(R>B){
			ans+="R";
			rep(i,0,B)ans+="BR";
			cout<<ans<<endl;
			return;	
		}
		if(B>R){
			ans+="B";
			rep(i,0,R)ans+="RB";
			cout<<ans<<endl;
			return;
		}
	}
	if(B>=R and B>=Y){
		string ans="B";
		priority_queue<pair<int,char>>pq;
		pq.push(mp(Y,'Y'));
		pq.push(mp(R,'R'));
		rep(i,1,B){
			if(pq.empty()){
				cout<<"IMPOSSIRLE\n";
				return;
			}
			auto cur=pq.top();
			pq.pop();
			ans+=cur.S;
			if(cur.S=='R')R--;
			if(cur.S=='Y')Y--;
			ans+="B";
			cur.F--;
			pq.push(cur);
		}
		if(abs(R-Y)>1){
			cout<<"IMPOSSIRLE\n";
			return;
		}
		if(R==Y){
			rep(i,0,R)ans+="RY";
			cout<<ans<<endl;
			return;
		}
		if(R>Y){
			ans+="R";
			rep(i,0,Y)ans+="YR";
			cout<<ans<<endl;
			return;	
		}
		if(Y>R){
			ans+="Y";
			rep(i,0,R)ans+="RY";
			cout<<ans<<endl;
			return;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t=1;
	cin>>t;
	while(t--){
		solve();
	}
	return 0;
}