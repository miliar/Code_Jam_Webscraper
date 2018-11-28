#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		int r,c;
		cin>>r>>c;
		
		char A[r+1][c+1];
		
		for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
		cin>>A[i][j];
		
		int i,j;
		bool empty[r+1];
		for(int i=1;i<=r;i++)
		empty[i]=false;
		
		for(i=1;i<=r;i++)
		{
			char ch='#';
			for(j=1;j<=c;j++)
			{
				if(A[i][j]!='?')
				{
					ch = A[i][j];
					break;
				}
			}
			
			if(ch!='#')
			{
				for(j=1;j<=c;j++)
				{
					if(A[i][j]!=ch && A[i][j]!='?')
					ch = A[i][j];
					else
					A[i][j] = ch;
				}
			}
			else
			empty[i]=true;
		}
		
		for(i=2;i<=r;i++)
		{
			if(empty[i]==true && empty[i-1]!=true)
			{
				for(j=1;j<=c;j++)
				{
					A[i][j]=A[i-1][j];
				}
				empty[i]=false;
			}
		}
		
		for(i=r-1;i>=1;i--)
		{
			if(empty[i]==true && empty[i+1]!=true)
			{
				for(j=1;j<=c;j++)
				{
					A[i][j]=A[i+1][j];
				}
				empty[i]=false;
			}
		}
		
		cout<<"Case #"<<k<<":"<<endl;
		for(int i=1;i<=r;i++)
		{
		for(int j=1;j<=c;j++)
			cout<<A[i][j];
			cout<<endl;
		}
		k++;
	}
	return 0;
}
