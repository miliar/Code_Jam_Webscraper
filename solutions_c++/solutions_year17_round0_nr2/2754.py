#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

typedef long long LL;
int INT(){int x;scanf("%d",&x);return x;}
char N[100]; 
int len;

LL dp[22][2][10];
LL pwr[22];

LL F(int at, bool smaller, int last) {
	if (at == len) {
		return 0;
	}
	LL& ret = dp[at][smaller][last];
	if (ret!=-1)return ret;
	ret=-2;

	int dig = N[at]-'0';
	for (int d=last;d<10;++d) {
		if (!smaller && d>dig)continue;
		LL tmp = F(at+1, smaller || (d < dig), d);
		if (tmp != -2) {
			if(ret<0)ret=0;
			ret=max(ret, d * pwr[at] + tmp);
		}
	}
	return ret;
}

int main() {
	int T=INT();
	for(int t=1;t<=T;++t){
		scanf("%s",N);
		len=strlen(N);
		pwr[len-1]=1;
		for (int i=len-2;i>=0;--i)pwr[i]=pwr[i+1]*10;
		memset(dp,-1,sizeof(dp));
		LL ans = F(0, false, 0);
		printf("Case #%d: ", t); cout << ans << "\n";
	}
	return 0;
}
