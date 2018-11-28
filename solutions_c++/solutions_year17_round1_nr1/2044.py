#include<iostream>
#include<conio.h>
//using namespace std;
using std::cout;
using std::cin;
int main()
{
	int s,t,r,c,temp,i,j;
	char A[25][25];
	cin>>t;
	for(s=0;s<=t-1;s++)
	{
		cin>>r>>c;
		for(i=0;i<=r-1;i++)
		for(j=0;j<=c-1;j++)
		cin>>A[i][j];
		for(i=0;i<=r-1;i++)
		for(j=0;j<=c-1;j++)
		{
			if(A[i][j]=='?')
			{
				temp=j;
				if(j!=0)
				{
					A[i][j]=A[i][j-1];
				}
				else
				{
				 while(A[i][j]=='?')
		         {	
		            j++;
		            if(j==c)
		            {
		               break;
					}
					else if(A[i][j]!='?')
					{
						for(;j>=1;j--)
						{
							A[i][j-1]=A[i][j];
						}
					}
				 }
				 j=temp;
			    }
			    
				 
			}
		}
		for(i=0;i<=r-1;i++)
		{
			if(A[i][0]=='?')
			{
				if(i==0)
				{
					while(A[i][0]=='?')
					i++;
					for(;i>=1;i--)
					for(j=0;j<=c-1;j++)
					A[i-1][j]=A[i][j];
				}
				else
				{
					for(j=0;j<=c-1;j++)
					A[i][j]=A[i-1][j];
				}
			}
		}
		cout<<"Case #" << s+1 << ": \n";
		for(i=0;i<=r-1;i++)
		{
		   for(j=0;j<=c-1;j++)
		   cout<<A[i][j];
		   cout<<"\n";
        }
	}
}
