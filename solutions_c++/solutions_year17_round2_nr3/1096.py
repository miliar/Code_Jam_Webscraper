#include<bits/stdc++.h>
using namespace std;
//nksheokand
int G[101][101];
int H[101][2];
long double dis[101];
int main()
{
	fstream in,out;
	in.open("C-small-attempt0.in");
	out.open("Output.txt");
	int t,n,q,u,v,d;
	long double rt;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>n>>q;
		for(int i=0;i<n;i++)
		in>>H[i][0]>>H[i][1];
		for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			in>>G[i][j];
		}
		for(int i=0;i<q;i++)
		{
			in>>u>>v;
		}
		for(int i=0;i<n;i++)
		dis[i]=-1;
		dis[0]=0;
		for(int i=0;i<n-1;i++)
		{
			d=0;
			for(int j=i+1;j<n;j++)
			{
				d+=G[j-1][j];
				if(d>H[i][0])
				break;
				rt=dis[i]+(long double)(d)/(long double)(H[i][1]);
				if(dis[j]==-1)
				dis[j]=rt;
				else
				dis[j]=min(dis[j],rt);
			}
		}
		out<<"Case #"<<l<<": "<<fixed<<dis[n-1]<<endl;
	}
	in.close();
	out.close();
	return 0;
}

