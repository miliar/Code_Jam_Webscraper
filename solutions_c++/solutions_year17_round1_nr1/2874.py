#include<iostream>
using namespace std;

int main()
{
	char board[25][25],e;
	int t,i,j,k,l,x,y,chk=0,c,r,cnt,o=1;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>r;
		cin>>c;
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				cin>>board[j][k];

			}
		}
		chk=0;cnt=0;
		for(j=0;j<r;j++)
		{
			cnt=0;
			if(chk==0)
			{

				 e='?';
				for(k=0;k<c;k++)
				{
					if(board[j][k]=='?' && e=='?')
					{
						cnt++;
					}
						else if(board[j][k]=='?' && e!='?')
					{
						board[j][k]=e;
					}
		 			else if(board[j][k]!='?' && cnt==0)
					{
						e=board[j][k];
					}
					else if(board[j][k]!='?' && cnt!=0)
					{
					    e=board[j][k];
						for(l=0;l<cnt;l++)
						{
						 //   	cout<<cnt<<k<<"\n";
								board[j][k-l-1]=e;
						}
						cnt=0;
					}
				}
				if(cnt==c && j!=0)
				{
					cnt=0;
					for(k=0;k<c;k++)
					{
						board[j][k]=board[j-1][k];
					}	
				}
				if(cnt==c && j==0)
				{
					cnt=0;
					chk=1;
				}
			}
			else
			{
				char e='?';
				for(k=0;k<c;k++)
				{
					if(board[j][k]=='?' && e=='?')
					{
						cnt++;
					}
					else if(board[j][k]=='?' && e!='?')
					{
						board[j][k]=e;
						for(y=0;y<chk;y++)
						{
							board[j-y-1][k]=e;
						}
					}
		 			else if(board[j][k]!='?' && cnt==0)
					{
						e=board[j][k];
						for(y=0;y<chk;y++)
						{
							board[j-1-y][k]=e;
						}
					}
					else if(board[j][k]!='?' && cnt!=0)
					{
e=board[j][k];
board[j-1][k]=e;						
						for(l=0;l<cnt;l++)
						{
								board[j][k-l-1]=e;
								for(y=0;y<chk;y++)
								{
									board[j-1][k-l-1]=e;
								}
						}
						cnt=0;
					}
				}
				if(cnt==c )
				{
						cnt=0;
						chk=chk+1;
				}
				else
				{
					cnt=0;
					chk=0;
				}

			}
			
		}	
cout<<"Case #"<<o<<":\n";
o++;
		for(j=0;j<r;j++)
		{	
			for(k=0;k<c;k++)
			{
				cout<<board[j][k];
				
			}
			cout<<"\n";
		}
	}
}
			
			
