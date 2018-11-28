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
	ll N;
	cin>>N;
	vi x;
	while(N){
		x.pb(N%10);
		N/=10;
	}
	reverse(all(x));
	rep(i,0,20)
	rep(i,1,sz(x)){
		if(x[i]<x[i-1]){
			x[i-1]--;
			rep(j,i,sz(x))x[j]=9;
			break;
		}
	}
	reverse(all(x));
	while(x.back()==0)x.pop_back();
	reverse(all(x));
	for(auto i:x)cout<<i;
	cout<<endl;
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