#include <iostream>
#include <cstdio>

using namespace std;

typedef long long LL;

int dig[22];
LL POW[22];
LL n,ans;
int T,cnt;

LL number()
{
	LL ret=0;
	for (int i=0;i<=18;++i) ret+=POW[i]*dig[i];
	return ret;
}

int main()
{
	//freopen("tidy.in","r",stdin),freopen("tidy.out","w",stdout);
	POW[0]=1;
	for (int i=1;i<=18;++i) POW[i]=POW[i-1]*10;
	for (scanf("%d",&T);T--;)
	{
		scanf("%lld",&n);
		for (int i=0;i<=18;++i) dig[i]=0;
		for (int i=18;i>=0;--i)
			for (int d=i<18?9:1;d>=0;--d)
			{
				for (int j=i;j>=0;--j) dig[j]=d;
				if (number()<=n) break;
			}
		printf("Case #%d: %lld\n",++cnt,number());
	}
	//fclose(stdin),fclose(stdout);
	return 0;
}