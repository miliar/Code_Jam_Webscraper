#include <bits/stdc++.h>

using namespace std;

char g[100][100];

int al[100][100];

char have[100];


int r,c;

int find2(char ch,int tr,int tc)
{
	int fr,fc;
	int f=0;
	for(int t=0;t<r;t++)
	{
		for(int t1=0;t1<c;t1++)
		{
			if(g[t][t1]==ch && tr!=t && tc!=t1)
			{
				fr=t,fc=t1;
				f=1;
			}
		}
	}

	for(int t=min(tr,fr);t<=max(tr,fr) && f ;t++)
	{
		for(int t1=min(fc,tc);t1<=max(fc,tc);t1++)
		{
			g[t][t1]=ch;
			al[t][t1]=1;
		}
		have[t]=ch;
	}

	return f;


}

int main()
{
	int T;
	
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		memset(al,0,sizeof(al));
		memset(have,0,sizeof(have));

		scanf(" %d %d",&r,&c);
		char in[100];
		for(int t=0;t<r;t++)
		{
			scanf(" %s",in);
			int len=strlen(in);
			for(int t1=0;t1<len;t1++)
			{
				g[t][t1]=in[t1];
			}
		}

		char ch=0;
		int a_r,a_c;
		int b_r,b_c;
		int result=1;

		for(int t=0;t<r;t++)
		{
			for(int t1=0;t1<c;t1++)
			{
				if(g[t][t1]!='?')
				{
					have[t]=g[t][t1];
				}
			}
		}

		for(int t=0;t<r;t++)
		{

			for(int t1=0;t1<c;t1++)
			{
				if(ch==0 && g[t][t1]!='?' && (!al[t][t1]))
				{
					a_r=t,a_c=t1;
					ch=g[t][t1];
					find2(ch,a_r,a_c);
				}
			}
		}

		int hc;
		if(have[0]==0)
		{
			for(int t=1;t<r;t++)
			{
				if(have[t]!=0)
				{
					hc=t;
					break;
				}

			}

			for(int t=c-1;t>=0;t--)
			{
				if(g[hc][t]=='?')
					g[hc][t]=have[hc];
				else
					have[hc]=g[hc][t];
			}


			for(int t=0;t<hc;t++)
			{
				for(int t1=0;t1<c;t1++)
				{
					g[t][t1]=g[hc][t1];
				}
			}
		}
		else
		{
			for(int t1=c-1;t1>=0;t1--)
			{
				
				if(g[0][t1]=='?')
				{
					g[0][t1]=have[0];
				}
				else
				{
					have[0]=g[0][t1];
				}
				
			}
		}

		for(int t=1;t<r;t++)
		{
			for(int t1=c-1;t1>=0;t1--)
			{
				if(have[t]==0)
				{
					g[t][t1]=g[t-1][t1];
				}
				else
				{
					if(g[t][t1]=='?')
					{
						g[t][t1]=have[t];
					}
					else
					{
						have[t]=g[t][t1];
					}
				}
			}
		}

		printf("Case #%d:\n",i);
		for(int t=0;t<r;t++)
		{
			for(int t1=0;t1<c;t1++)
			{
				printf("%c",g[t][t1]);
			}
			printf("\n");
		}


	}
	return 0;
}