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

int t,n,p,x[55],ta,tb,tc,ans;
multiset<pair<int,int> > s[55];
bool o;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		ans=0;
		scanf("%d%d",&n,&p);
		F1(b,0,n)scanf("%d",x+b),s[b].clear();
		F1(b,0,n){
			F1(c,0,p){
				scanf("%d",&ta);
				ta*=10;
				tb=ta/(9*x[b]);
				tc=(ta+11*x[b]-1)/(11*x[b]);
				s[b].insert(mp(tc,tb));
			}
		}
		o=1;
		while(1){
			ta=INT_MIN,tb=INT_MAX;
			F1(b,0,n){
				if(s[b].empty()){
					o=0;
					break;
				}
				ta=max(ta,s[b].begin()->fi);
				tb=min(tb,s[b].begin()->se);
			}
			if(!o)break;
			if(ta<=tb){
				ans++;
				F1(b,0,n)s[b].erase(s[b].begin());
			}else F1(b,0,n)if(s[b].begin()->se<ta)s[b].erase(s[b].begin());
		}
		printf("Case #%d: %d\n",a,ans);
	}
	return 0;
}
