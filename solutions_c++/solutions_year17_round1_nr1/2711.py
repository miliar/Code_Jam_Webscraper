#include<bits/stdc++.h>
using namespace std;
//nksheokand
vector<string> V;
bool f;
int t,r,c;
bool fnc(int idx)
{
	int k,l,m,n;
	if(idx==26)
	{
		for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		{
			if(V[i][j]=='?')
			return false;
		}
		return true;
	}
	char ch='A';
	ch+=idx;
	for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
	{
		if(V[i][j]==ch)
		{
			for(int k=0;k<=i;k++)
			for(int l=0;l<=j;l++)
			for(int m=i;m<r;m++)
			for(int n=j;n<c;n++)
			{
				f=true;
				for(int o=k;o<=m;o++)
				for(int p=l;p<=n;p++)
				{
					if(V[o][p]=='?' || V[o][p]==ch)
					{
						V[o][p]=ch;
					}
					else
					{
						f=false;
					}
				}
				if(f)
				{
					if(fnc(idx+1))
					return true;
				}
				for(int o=k;o<=m;o++)
				for(int p=l;p<=n;p++)
				{
					if(V[o][p]==ch && (o!=i || p!=j))
					{
						V[o][p]='?';
					}
				}
			}
		}
	}
	fnc(idx+1);
}
int main()
{
	fstream in,out;
	in.open("A-small-attempt0.in");
	out.open("Output.txt");
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>r>>c;
		V.resize(r);
		for(int i=0;i<r;i++)
		{
			in>>V[i];
			//V[i]="."+V[i];
		}
		fnc(0);
		out<<"Case #"<<l<<":"<<endl;
		for(int i=0;i<r;i++)
		{
			out<<V[i]<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}
