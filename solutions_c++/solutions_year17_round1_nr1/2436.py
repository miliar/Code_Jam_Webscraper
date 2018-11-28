#include<bits/stdc++.h>
using namespace std;

int N,M;
char A[30][30],orig[30][30];

void leftdown(int x,int y)
{
	int mini=y,maxi=y;
	
	int i,j;
	
	for (i=y-1;i>0;i--)
	{
	//	cout<<x<<" "<< y <<" "<<i<<endl;
		if(A[x][i]!='?')
		{
			break;
		}
		mini=i;
		A[x][i]=A[x][y];
	}
	
	for (i=y+1;i<=M;i++)
	{
		if(A[x][i]!='?')
		break;
		maxi=i;
		A[x][i]=A[x][y];
	}
	
	//cout<<A[x][y]<<endl;
	//cout<<mini<<endl;
	for (i=x+1;i<=N;i++)
	{
		int flag=1;
		for (j=mini;j<=maxi;j++)
		{
			if(A[i][j]!='?')
			flag=0;
		}
		
		if(flag==0)
		{
		
			break;
		}
		
		for (j=mini;j<=maxi;j++)
		A[i][j]=A[x][y];
		
	}
	
	//	cout<<"Painted till\n";
	//		cout<<x<<" "<<y<<" To "<<i-1<<" "<<mini<<endl;
	
}

void upright(int x,int y)
{
	int maxi=y,mini=y;
	
	int i,j;
	for (i=y+1;i<=M;i++)
	{
		if(A[x][i]!='?')
		{
			break;
		}
		
		
		A[x][i]=A[x][y];
		
		maxi=i;
	}
	
	for (i=y-1;i>0;i--)
	{
		if(A[x][i]!='?')
		break;
		A[x][i]=A[x][y];
		mini=i;
	}
	
//	cout<<A[x][y]<<endl;
	for (i=x-1;i>0;i--)
	{
		int flag=1;
		for (j=mini;j<=maxi;j++)
		{
			if(A[i][j]!='?')
			{
				flag=0;
			}
		}
		
		
		if(flag==0)
		break;
		
		for (j=mini;j<=maxi;j++)
		A[i][j]=A[x][y];
	}
	
//	cout<<"Painted upright "<<x<<" "<<y<<" to "<<i+1<<" "<<maxi<<endl;
}
/*
3 4
?H??
EFC?
GDAB
4 2
??
?A
??
B?

*/
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++)
	{
		
		scanf("%d%d",&N,&M);
		memset(orig,0,sizeof(orig));
		int i,j;
		
		for (i=1;i<=N;i++)
		{
		//	for(j=1;j<=M;j++)
			scanf("%s",A[i]+1);
		}
		
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=M;j++)
			{
				if(A[i][j]!='?')
				orig[i][j]=1;
			}
		}
		
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=M;j++)
			{
				if(orig[i][j])
				{
				//	printf("%d %d\n",i,j);
					leftdown(i,j);
				}
			}
		}
		
		for (i=N;i>0;i--)
		{
			for (j=M;j>0;j--)
			{
				if(orig[i][j])
				{
					upright(i,j);
				}
			}
		}
		
		for (int t1=1;t1<=625;t1++)
		{
		
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=M;j++)
			{
				if(A[i][j]=='?')
				{
					if(j>1 && A[i][j-1]!='?')
					A[i][j]=A[i][j-1];
					
					else A[i][j]=A[i][j+1];
				}
			}
		}
		}
		printf("Case #%d:\n",t);
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=M;j++)
			printf("%c",A[i][j]);
			printf("\n");
		}
		
	}
}
