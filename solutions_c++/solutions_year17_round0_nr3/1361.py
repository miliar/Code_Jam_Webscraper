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
priority_queue<lint> q;
map<lint,lint> me;
int main()
{
	int t;lint n,k;
	cin>>t;
	rep(i,t){
		cin>>n>>k;
		while(!q.empty()) q.pop();
		me.clear();
		q.push(n);me[n]++;
		while(!q.empty()){
			lint p=q.top();q.pop();
			//q.push((p-1)/2);q.push(p/2);
			lint x=me[p],a=p/2,b=(p-1)/2;
			if(x>=k){
				printf("Case #%d: ",i+1);
				cout<<a<<' '<<b<<endl;
				break;
			}
			k-=x;
			if(me.count(a)<1) q.push(a);me[a]+=x;
			if(me.count(b)<1) q.push(b);me[b]+=x;
		}
	}
}
