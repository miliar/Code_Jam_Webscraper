#include<bits/stdc++.h>
using namespace std;
//nksheokand
int arr[1001][2];
int main()
{
	fstream in,out;
	in.open("B-small-attempt2.in");
	out.open("Output.txt");
	string S;
	int t,n,r,o,y,g,b,v,ol;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>n>>r>>o>>y>>g>>b>>v;
		S="";
		for(int i=0;i<n;i++)
		arr[i][0]=arr[i][1]=0;
		if(r>=y && r>=b)
		{
			if(y+b<r)
			{
				S="IMPOSSIBLE";
			}
			else
			{
				for(int i=0;i<y;i++)
				arr[i][0]=1;
				for(int i=1;i<=b;i++)
				arr[r-i][1]=1;
				for(int i=0;i<r;i++)
				{
					S+='R';
					if(arr[i][0])
					S+='Y';
					if(arr[i][1])
					S+='B';
				}
			}
		}
		else if(y>=r && y>=b)
		{
			if(r+b<y)
			{
				S="IMPOSSIBLE";
			}
			else
			{
				for(int i=0;i<r;i++)
				arr[i][0]=1;
				for(int i=1;i<=b;i++)
				arr[y-i][1]=1;
				for(int i=0;i<y;i++)
				{
					S+='Y';
					if(arr[i][0])
					S+='R';
					if(arr[i][1])
					S+='B';
				}
			}
		}
		else if(b>=y && b>=r)
		{
			if(y+r<b)
			{
				S="IMPOSSIBLE";
			}
			else
			{
				for(int i=0;i<y;i++)
				arr[i][0]=1;
				for(int i=1;i<=r;i++)
				arr[b-i][1]=1;
				for(int i=0;i<b;i++)
				{
					S+='B';
					if(arr[i][0])
					S+='Y';
					if(arr[i][1])
					S+='R';
				}
			}
		}
		else
		{
			S="IMPOSSIBLE";
		}
		out<<"Case #"<<l<<": "<<S<<endl;
	}
	in.close();
	out.close();
	return 0;
}

