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

int t;
LL n,k;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%lld%lld",&n,&k);
		for(LL b=1;;b<<=1){
			n-=b;
			if(n<=0)n=0;
			if(k<=b){
				n=n/b+(k<=n%b);
				printf("Case #%d: %lld %lld\n",a,(n+1)/2,n/2);
				break;
			}else k-=b;
		}
	}
	return 0;
}
