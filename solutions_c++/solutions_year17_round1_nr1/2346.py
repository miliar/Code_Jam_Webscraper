#include <iostream>
using namespace std;
char G[30][30];
struct s
{
	int x,y;
	int left,right;
	char c;
	s(int x1='0',int y1='0',char c1='0')
	{
		x=x1,y=y1,c=c1;
		left=y,right=y;
	}
};
s A[40];
int main()
{
	int T,num,R,C;
	int i,j,k,t;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>R>>C;
		num=0;
		for(j=1;j<=R;j++)
		{
			for(k=1;k<=C;k++)
			{
				cin>>G[j][k];
				if(G[j][k]!='?')
				{
					s s1(j,k,G[j][k]);
					A[num++]=s1;
				}
			}
		}
		for(j=0;j<num;j++)
		{
			int x=A[j].x;
			int y=A[j].y;
			char c=A[j].c;
			int left=A[j].left;
			int right=A[j].right;
			for(k=y+1;k<=C;k++)
			{
				if(G[x][k]=='?')
				{
					G[x][k]=c;
					right++;
				}
				else
				{
					break;
				}
			}
			for(k=y-1;k>=1;k--)
			{
				if(G[x][k]=='?')
				{
					G[x][k]=c;
					left--;
				}
				else
				{
					break;
				}
			}
			for(k=x-1;k>=1;k--)
			{
				for(t=left;t<=right;t++)
				{
					if(G[k][t]!='?')
						break;
				}
				if(t>right)
				{
					for(t=left;t<=right;t++)
					{
						G[k][t]=c;
					}
				}
				else
				{
					break;
				}
			}
			for(k=x+1;k<=R;k++)
			{
				for(t=left;t<=right;t++)
				{
					if(G[k][t]!='?')
						break;
				}
				if(t>right)
				{
					for(t=left;t<=right;t++)
					{
						G[k][t]=c;
					}
				}
				else
				{
					break;
				}
			}
		}
		cout<<"Case #"<<i<<":"<<endl;
		for(j=1;j<=R;j++)
		{
			for(k=1;k<=C;k++)
				cout<<G[j][k];
			cout<<endl;
		}
	}
}
