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

int t,n,c,m,fre[1005],hv[1005],p[1005],u[1005],la,aa,q[3],bb;
bool v[1005],uu[1005];

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		memset(fre,0,sizeof(fre));
		memset(hv,0,sizeof(hv));
		memset(v,0,sizeof(v));
		scanf("%d%d%d",&n,&c,&m);
		F1(b,0,m){
			scanf("%d%d",p+b,u+b);
			fre[p[b]]++;
			hv[u[b]]++;
		}
		aa=1,la=0;
		memset(uu,0,sizeof(uu));
		F1(b,0,m){
			q[0]=INT_MAX;
			F1(c,0,m)if(!v[c]&&p[c]>la&&!uu[u[c]]){
				if(p[c]<q[0]||(p[c]==q[0]&&hv[u[c]]>q[1])){
					q[0]=p[c];
					q[1]=hv[u[c]];
					q[2]=c;
				}
			}
			if(q[0]==INT_MAX)aa++,la=0,b--,memset(uu,0,sizeof(uu));
			else{
				v[q[2]]=1;
				la++;
				uu[u[q[2]]]=1;
				hv[u[q[2]]]--;
			}
		}
		bb=0;
		F2(b,1,n)bb+=max(0,fre[b]-aa);
		printf("Case #%d: %d %d\n",a,aa,bb);
	}
	return 0;
}
