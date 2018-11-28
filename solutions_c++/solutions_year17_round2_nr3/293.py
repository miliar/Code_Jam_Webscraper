#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=(y);x<(z);x++)
#define F2(x,y,z) for(int x=(y);x<=(z);x++)
#define F3(x,y,z) for(int x=(y);x>(z);x--)
#define F4(x,y,z) for(int x=(y);x>=(z);x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>
#define fi first
#define se second

#define MAX 100005
#define AMAX 1025*1005
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,qq,ta,tb;
LL e[105],d[105][105];
double s[105],x[105];
bool v[105],vv[105];
vector<int> y[105];
vector<double> z[105];
priority_queue<pair<double,int> > q;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%d%d",&n,&qq);
		F2(b,1,n)scanf("%lld%lf",e+b,s+b);
		F2(b,1,n)F2(c,1,n)scanf("%lld",&d[b][c]);
		F2(b,1,n)F2(c,1,n)F2(dd,1,n)if(d[c][b]>0&&d[b][dd]>0){
			if(d[c][dd]==-1)d[c][dd]=d[c][b]+d[b][dd];
			else d[c][dd]=min(d[c][dd],d[c][b]+d[b][dd]);
		}
		F2(b,1,n){
			y[b].clear(),z[b].clear();
			F2(c,1,n)if(b!=c&&d[b][c]>0&&d[b][c]<=e[b])y[b].pb(c),z[b].pb(d[b][c]/s[b]);
		}
		printf("Case #%d:",a);
		while(qq--){
			scanf("%d%d",&ta,&tb);
			memset(v,0,sizeof(v));
			memset(vv,0,sizeof(vv));
			vv[ta]=1,q.push(mp(-(x[ta]=0),ta));
			while(!q.empty()){
				ta=q.top().se;
				q.pop();
				if(ta==tb){
					printf(" %.9lf",x[tb]);
					q=priority_queue<pair<double,int> >();
				}
				if(!v[ta]){
					v[ta]=1;
					F1(b,0,y[ta].size())if(!vv[y[ta][b]]||x[ta]+z[ta][b]<x[y[ta][b]]){
						vv[y[ta][b]]=1;
						q.push(mp(-(x[y[ta][b]]=x[ta]+z[ta][b]),y[ta][b]));
					}
				}
			}
		}
		printf("\n");
	}
	return 0;
}
