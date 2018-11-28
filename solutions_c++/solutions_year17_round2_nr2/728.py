#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>

using namespace std;

const int N=1500;

struct dat
{
	int tp,num;

	bool operator<(dat const x)const{return num>x.num;}
}srt[10];

int per[N];
int T,n,R,O,Y,G,B,V,cnt,id,tot;

int main()
{
	freopen("neighbor.in","r",stdin),freopen("neighbor.out","w",stdout);
	for (scanf("%d",&T);T--;)
	{
		memset(per,0,sizeof per);
		scanf("%d%d%d%d%d%d%d",&n,&R,&O,&Y,&G,&B,&V);
		if (G>R||O>B||V>Y)
		{
			printf("Case #%d: IMPOSSIBLE\n",++id);
			continue;
		}
		if (G==R&&G)
		{
			if (O||B||V||Y)
			{
				printf("Case #%d: IMPOSSIBLE\n",++id);
				continue;
			}
			printf("Case #%d: ",++id);
			for (int i=1;i<=n;++i)
				if (i&1) putchar('G');
				else putchar('R');
			printf("\n");
			continue;
		}
		if (O==B&&O)
		{
			if (G||R||V||Y)
			{
				printf("Case #%d: IMPOSSIBLE\n",++id);
				continue;
			}
			printf("Case #%d: ",++id);
			for (int i=1;i<=n;++i)
				if (i&1) putchar('O');
				else putchar('B');
			printf("\n");
			continue;
		}
		if (V==Y&&V)
		{
			if (G||R||O||B)
			{
				printf("Case #%d: IMPOSSIBLE\n",++id);
				continue;
			}
			printf("Case #%d: ",++id);
			for (int i=1;i<=n;++i)
				if (i&1) putchar('V');
				else putchar('Y');
			printf("\n");
			continue;
		}
		srt[1].tp=1,srt[1].num=R-G;
		srt[2].tp=2,srt[2].num=Y-V;
		srt[3].tp=3,srt[3].num=B-O;
		tot=R-G+Y-V+B-O;
		sort(srt+1,srt+4);
		for (int i=1;i<=srt[1].num;++i)
		{
			if (i*2-1>n)
			{
				n=-1;
				break;
			}
			per[i*2-1]=srt[1].tp;
		}
		if (n==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n",++id);
			continue;
		}
		int now=3,nxt=2;
		int r1=srt[3].tp==1?R:(srt[3].tp==2?Y:B),r2=srt[2].tp==1?R:(srt[2].tp==2?Y:B);
		for (int i=tot;i>=1;--i)
			if (!per[i])
			{
				swap(now,nxt),swap(r1,r2);
				if (!r1) swap(now,nxt),swap(r1,r2);
				per[i]=srt[now].tp,--r1;
			}
		bool judge=1;
		for (int i=1;i<=tot;++i)
			if (per[i]==per[i==1?tot:i-1]||per[i]==per[i==tot?1:i+1])
			{
				judge=0;
				break;
			}
		if (!judge)
		{
			printf("Case #%d: IMPOSSIBLE\n",++id);
			continue;
		}
		printf("Case #%d: ",++id);
		for (int i=1;i<=tot;++i)
		{
			if (per[i]==1)
			{
				putchar('R');
				if (G>0) for (;G--;) putchar('G'),putchar('R');
			}
			if (per[i]==2)
			{
				putchar('Y');
				if (V>0) for (;V--;) putchar('V'),putchar('Y');
			}
			if (per[i]==3)
			{
				putchar('B');
				if (O>0) for (;O--;) putchar('O'),putchar('B');
			}
		}
		printf("\n");
	}
	fclose(stdin),fclose(stdout);
	return 0;
}