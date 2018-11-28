#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
#include<cassert>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int num[1010],n2[1010];
int inf=1145141919;
priority_queue<pint> q;
int cal(int x){
	while(!q.empty()) q.pop();
	rep(i,x) q.push(mp(0,0));
	int ret=0;
	rep(i,1005) rep(j,n2[i]){
		pint p=q.top();q.pop();
		int x=-p.fi,y=-p.se;
		if(x>=i) return inf;
		if(y==i) ret++;
		y=max(y,i);x++;
		q.push(mp(-x,-y));
	}
	return ret;
}
int main()
{
	int t,a,b,c,n,m;
	cin>>t;
	rep(i,t){
		memset(num,0,sizeof(num));
		memset(n2,0,sizeof(n2));
		cin>>n>>c>>m;
		rep(j,m){
			cin>>a>>b;
			num[b]++;
			n2[a]++;
		}
		int lo=0,hi=1010;
		rep(j,1005) lo=max(lo,num[j]);
		while(hi>lo){
			int mi=(hi+lo)/2;
			if(cal(mi)<inf) hi=mi;else lo=mi+1;
		}
		printf("Case #%d: %d %d\n",i+1,lo,cal(lo));
	}
}
