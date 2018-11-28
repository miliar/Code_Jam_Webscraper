#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#define forr(i,a,b) for(int i=(a);(i)<int(b);(i)++)
#define forn(i,n) forr(i,0,n)
#define pb push_back

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

struct interval {
	int l, r, s;
};

bool operator < (const interval &a, const interval &b){
	if( a.s==b.s )
		return a.l>b.l;
	return a.s<b.s;
}

int main(){
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	
	int T,N,K;
	cin>>T;
		
	forn(t,T){
		cin>>N>>K;

		priority_queue <interval> PQ;
		
		PQ.push({0,N+1});
		
		int l,r,m;
		
		interval act;
		forn(k,K){
			act = PQ.top();
			l = act.l;
			r = act.r;
			//~ cout<<l<<" "<<r<<endl;
			PQ.pop();
			m = (l + r)/2;
			PQ.push({l, m, m - l});
			PQ.push({m, r, r - m});
		}
		
		cout<<"Case #"<<t+1<<": "<<max(m-l, r-m) - 1<<" "<<min(m-l, r-m) - 1<<"\n";
	}
	
	return 0;
}
