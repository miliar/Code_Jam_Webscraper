#include <stdio.h>
#include <cstring>
#include <algorithm>

typedef long long lli;
lli val,n;
lli arr[20], power[20], cache[20][10][2];
lli DP(int idx, int prev, int flag) {
	if(idx==-1) return 0;
	lli &ret=cache[idx][prev][flag];
	if(ret!=-1) return ret;

	ret=-2;
	lli b=(flag==0)?arr[idx]:9;
	for(lli i=prev;i<=b;i++) {
		int next_flag;
		if(flag==1||i<arr[idx]) next_flag=1;
		else next_flag=0;

		lli tmp=DP(idx-1,i,next_flag);
		if(tmp!=-2) {
			ret=std::max(ret, tmp+i*power[idx]);
		}
	}
	return ret;
}
int main() {
	power[0]=1;
	for(lli i=1;i<=18;i++)
		power[i]=power[i-1]*10;

	int test;
	scanf("%d",&test);
	for(int tc=1;tc<=test;tc++) {
		scanf("%lld",&val);
		n=0;

		while(val) {
			arr[n++]=val%10;
			val/=10;
		}

		memset(cache, -1,sizeof(cache));
		printf("Case #%d: %lld\n",tc, DP(n-1,0,0));
	}
	return 0;
}