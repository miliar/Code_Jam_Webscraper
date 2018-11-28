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
LL n,po[19];
char x[25];

void go(LL a){
	if(a==0)return;
	LL la=0;
	F4(b,18,0){
		LL ta=a/po[b]%10;
		if(ta<la){
			go(a/po[b+1]-1);
			F4(c,b,0)printf("9");
			return;
		}
		la=ta;
	}
	printf("%lld",a);
}

int main(){
	po[0]=1;
	F1(a,1,19)po[a]=po[a-1]*10;
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%lld",&n);
		printf("Case #%d: ",a);
		go(n);
		printf("\n");
	}
	return 0;
}
