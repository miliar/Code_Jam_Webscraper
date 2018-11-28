#include <algorithm>
#include <vector>
#include <limits.h> 
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <unordered_map>
#include <queue>
#include <sstream>


using namespace std;
#define ll long long

struct node
{
	ll s;
	ll e;
	node(ll _s, ll _e): s(_s) , e(_e) {}
	bool operator < (const node &a) const {
		int len1 = e - s + 1;
		int len2 = a.e - a.s + 1;
		if(len1 == len2) return s < a.s;
		return len1 < len2;
	}

};

void slove(int t, ll n, ll k) {
	ll s = 1;
	ll e = n;
	priority_queue<node> q;
	q.push(node(s,e));
	ll cnt = 0;
	ll ls = 0 , rs=0;
	while(!q.empty()) {
		auto top = q.top(); q.pop();
		ll c = (top.e - top.s) / 2 + top.s;
		if(c-1 >= top.s) {
			q.push(node(top.s,c-1));
		}
		if(c+1 <= top.e) {
			q.push(node(c+1,top.e));
		}
		cnt += 1;
		if(cnt == k) {
			ls = c - top.s;
			rs = top.e - c;
			break;
		}
	}
	cout<<"Case #"<<t<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
}
int main(int argc, char *argv[]) {
	if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        freopen("A.in", "r", stdin);    
    }
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		ll n;
		ll k;
		cin>>n>>k;
		slove(i+1,n,k);
	}
	return 0;
}