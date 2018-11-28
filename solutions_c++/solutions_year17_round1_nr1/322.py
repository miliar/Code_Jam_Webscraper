#include<cstdio>
#include<cstring>

int t;

int r,c;
char input[30][30];
char color[30];
char output[30][30];

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);

	scanf("%d",&t);
	for(int test_case=1;test_case<=t;test_case++)
	{
		memset(input,0,sizeof(input[0][0])*30*30);
		memset(output,0,sizeof(output[0][0])*30*30);
		memset(color,0,sizeof(color[0])*30);

		scanf("%d %d\n",&r,&c);
		for(int i=0;i<r;i++) fgets(input[i],30,stdin);

		int ix,iy;
		int ox,oy;

		for(ix=ox=0;ix<r;ix++)
		{
			for(iy=oy=0;iy<c;iy++) if(input[ix][iy]>='A'&&input[ix][iy]<='Z')for(;oy<=iy;oy++) color[oy]=input[ix][iy];
			if(oy!=0) for(;oy<c;oy++) color[oy]=color[oy-1];
			if(oy!=0) for(;ox<=ix;ox++) for(oy=0;oy<c;oy++) output[ox][oy]=color[oy];
		}
		for(;ox<r;ox++) for(oy=0;oy<c;oy++) output[ox][oy]=color[oy];

		printf("Case #%d:\n",test_case);
		for(int i=0;i<r;i++) printf("%s\n",output[i]);
	}
	return 0;
}
