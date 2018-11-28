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

int t,n,p,ta,x[4],s;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		memset(x,0,sizeof(x));
		s=0;
		scanf("%d%d",&n,&p);
		while(n--){
			scanf("%d",&ta);
			s+=ta;
			x[ta%p]++;
		}
		if(p==2)x[0]+=x[1]/2;
		else if(p==3){
			ta=min(x[1],x[2]);
			x[0]+=ta;
			x[0]+=(x[1]-ta)/3;
			x[0]+=(x[2]-ta)/3;
		}else{
			ta=min(x[1],x[3]);
			x[1]-=ta,x[3]-=ta;
			x[0]+=ta;
			ta=min(x[1]/2,x[2]);
			x[1]-=ta*2,x[2]-=ta;
			x[0]+=ta;
			ta=min(x[3]/2,x[2]);
			x[3]-=ta*2,x[2]-=ta;
			x[0]+=ta;
			x[0]+=x[1]/4+x[2]/2+x[3]/4;
		}
		if(s%p)x[0]++;
		printf("Case #%d: %d\n",a,x[0]);
	}
	return 0;
}
