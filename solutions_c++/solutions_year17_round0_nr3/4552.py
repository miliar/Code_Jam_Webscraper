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
int test=0;
void solve(){
	cout<<"Case #"<<(++test)<<": ";
	ll N,K;
	cin>>N>>K;
	priority_queue<pair<ll,pair<ll,ll>>>pq;
	pq.push(mp(N,mp(0,N+1)));
	rep(i,0,K){
		auto cur=pq.top();
		pq.pop();
		cur.S.F*=-1;
		ll next=(cur.S.S+cur.S.F)/2;
		if(i==K-1){
			cout<<cur.S.S-1-next<<" "<<next-1-cur.S.F<<endl;
		}
//		cout<<next<<endl;
		pq.push(mp(next-1-cur.S.F,mp(-cur.S.F,next)));
		pq.push(mp(cur.S.S-1-next,mp(-next,cur.S.S)));
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