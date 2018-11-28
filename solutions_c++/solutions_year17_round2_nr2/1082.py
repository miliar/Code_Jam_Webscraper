#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int T;
	char cmx,cmd,cmn;
	int mx,md,mn,N,R,O,Y,G,B,V,n;
	scanf("%d",&T);
	for(int I=1;I<=T;I++)
	{
		scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
		cmx='R';	cmd='Y';	cmn='B';
		mx=R;		md=Y;		mn=B;

		if(mx<md)
		{
			swap(cmx,cmd);
			swap(mx,md);
		}	
		if(md<mn)
		{
			swap(cmn,cmd);
			swap(mn,md);
		}
		if(mx<md)
		{
			swap(cmx,cmd);
			swap(mx,md);
		}	

		if(mn+md<mx)
			printf("Case #%d: IMPOSSIBLE\n",I);
		else
		{
			printf("Case #%d: ",I);
			n=0;
			for(int i=0;i<mx-md;i++)
				{printf("%c%c%c%c",cmx,cmd,cmx,cmn);n+=4;}
			for(int i=0;i<mn-mx+md;i++)
				{printf("%c%c%c",cmx,cmd,cmn);n+=3;}
			for(int i=0;i<md-mn;i++)
				{printf("%c%c",cmx,cmd);n+=2;}
			printf("\n");
			//printf("-> %d vs %d\n",n,N);
		}
	}
}