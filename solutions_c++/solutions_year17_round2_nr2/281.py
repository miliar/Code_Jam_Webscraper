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

int t,n,z[6],at;
char x[MAX],y[]="RYB";
bool o;
vector<pair<int,int> > v;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%d",&n);
		F1(b,0,6)scanf("%d",z+b);
		at=o=1;
		while(z[0]||z[2]||z[4]){
			v.clear();
			F1(b,0,3)v.pb(mp(x[at-1]==y[b]?-1:z[b*2],b));
			sort(v.begin(),v.end());
			if(v[2].fi>0)x[at++]=y[v[2].se],z[v[2].se*2]--;
			else{
				o=0;
				break;
			}
		}
		if(o&&x[at-1]==x[1]){
			if(x[at-1]==x[at-3])o=0;
			else swap(x[at-1],x[at-2]);
		}
		if(o)printf("Case #%d: %s\n",a,x+1);
		else printf("Case #%d: IMPOSSIBLE\n",a);
		memset(x,0,n+1);
	}
	return 0;
}
