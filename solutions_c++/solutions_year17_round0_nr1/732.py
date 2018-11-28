#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>

using namespace std;

int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

char getnxt()
{
	char ch=getchar();
	while (ch!='+'&&ch!='-'&&ch!=' ') ch=getchar();
	return ch;
}

const int N=1005;

int step,T,n,k,cnt;
bool mark[N];

int main()
{
	freopen("flipper.in","r",stdin),freopen("flipper.out","w",stdout);
	for (T=read();T--;n=step=0)
	{
		char ch=getnxt();
		for (;ch!=' ';mark[n++]=ch=='+',ch=getnxt());
		k=read();
		for (int i=0;i+k-1<n;++i)
			if (!mark[i])
			{
				for (int j=0;j<k&&i+j<n;++j) mark[i+j]^=1;
				++step;
			}
		for (int i=0;i<n;++i)
			if (!mark[i]) step=-1;
		if (step!=-1) printf("Case #%d: %d\n",++cnt,step);
		else printf("Case #%d: IMPOSSIBLE\n",++cnt);
	}
	fclose(stdin),fclose(stdout);
	return 0;
}