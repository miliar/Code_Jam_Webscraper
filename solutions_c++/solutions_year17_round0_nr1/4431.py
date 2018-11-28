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
	int cnt=0;
	string s;
	cin>>s;
	int K;
	cin>>K;
	vector<bool>x;
	for(auto i:s)x.pb(i=='+');
	rep(i,0,sz(s)-K+1){
		if(x[i]==0){
			cnt++;
			rep(j,i,i+K){
				x[j]=x[j]^1;
			}
		}
	}
	if(all_of(all(x),[](bool temp){return temp==1;})){
		cout<<cnt<<endl;
	}
	else{
		cout<<"IMPOSSIBLE\n";
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