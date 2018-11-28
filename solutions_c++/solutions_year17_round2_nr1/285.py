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

int t,n;
double d,k,s,ans;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%lf%d",&d,&n);
		ans=0;
		F1(b,0,n){
			scanf("%lf%lf",&k,&s);
			ans=max(ans,(d-k)/s);
		}
		printf("Case #%d: %.10lf\n",a,d/ans);
	}
	return 0;
}
