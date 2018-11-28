#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

typedef long double db;

int T,n,d,cnt;
db res;

int main()
{
	freopen("control.in","r",stdin),freopen("control.out","w",stdout);
	for (scanf("%d",&T);T--;printf("Case #%d: %lf\n",++cnt,(double)(d/res)))
	{
		scanf("%d%d",&d,&n),res=0;
		for (int i=1,x,y;i<=n;++i) scanf("%d%d",&x,&y),res=max(res,(db)(1.*(d-x))/(1.*y));
	}
	fclose(stdin),fclose(stdout);
	return 0;
}