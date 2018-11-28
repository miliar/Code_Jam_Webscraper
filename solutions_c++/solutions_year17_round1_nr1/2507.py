#include <bits/stdc++.h>
using namespace std;
char mat[100][100];
int x,y;
void lol(int i,int j,char C)
{
	mat[i][j]=C;
	int ar[4]={0,1,0,-1};
	int ar2[4]={1,0,-1,0};
	int ii,jj;
	for(int xd=0;xd<4;xd++)
	{
		ii=i+ar[xd];
		jj=j+ar2[xd];
		if(ii>=0 and jj>=0 and ii<x and jj<y and mat[ii][jj]=='?')
		{
			mat[i][j]=C;
			lol(ii,jj,C);
		}
	}
}
int main()
{
	//freopen("A.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("resuA.txt","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		cin>>x>>y;
		cout<<"Case #"<<tt<<":"<<endl;
		for(int i=0;i<x;i++)
		{
			for(int j=0;j<y;j++)
			{
				cin>>mat[i][j];
			}
		}
		for(int i=0;i<x;i++)
		{
			for(int j=0;j<y;j++)
			{
				if(mat[i][j]!='?')
				{
					for(int k=j-1;k>=0;k--)
					{
						if(mat[i][k]=='?')mat[i][k]=mat[i][j];
						else break;
					}
					for(int k=j+1;k<y;k++)
					{
						if(mat[i][k]=='?')mat[i][k]=mat[i][j];
						else break;
					}
				}
			}
		}
		bool izi=0;
		gnu:;
		izi=0;
		for(int i=0;i<x;i++)
		{
			for(int j=0;j<y;j++)
			{
				if(mat[i][j]=='?')
				{
					izi=1;	
					if(i-1>=0 and mat[i-1][j]!='?')
					{
						char aux=mat[i-1][j];
						mat[i][j]=aux;
						//char aux=mat[i-1][j];
						for(int k=j+1;k<y;k++)
						{
							if(mat[i-1][k]!=aux)break;
							else
							{
								mat[i][k]=aux;
							}
						}
					}
					else if( i+1<x and mat[i+1][j]!='?')
					{
						char aux=mat[i+1][j];
						mat[i][j]=aux;
						//char aux=mat[i-1][j];
						for(int k=j+1;k<y;k++)
						{
							if(mat[i+1][k]!=aux)break;
							else
							{
								mat[i][k]=aux;
							}
						}
					}
				}

			}
		}
		if(izi==1)goto gnu;
	//	cout<<x<<y<<endl;
		for(int i=0;i<x;i++)
		{
			for(int j=0;j<y;j++)
			{
				cout<<mat[i][j];
			}
			cout<<endl;
		}
	}
	
}
