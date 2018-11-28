#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		long long a,b;
		scanf("%lld%lld",&a,&b);
		b--;
		int dep=0;
		long long at=0;
		long long sz=1;
		while(1){
			if(b<sz){
				at=b;break;
			}
			dep++;
			b-=sz;
			sz*=2;
		}
		long long n=a-sz+1;
		long long m=n/sz-1;
		if(n%sz>at)m++;
		//printf("%lld %lld\n",n,m);
		printf("Case #%d: %lld %lld\n",t,(m+1)/2,m/2);
	}
}