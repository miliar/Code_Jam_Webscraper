#include <iostream>
using namespace std;
int main()
{
	int test,r,c;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cin>>r>>c;
		int j0=0;
		char ch[r][c];
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				cin>>ch[j][k];
			}		
		}
		cout<<"Case #"<<i<<":"<<endl;
		for(int j=0;j<r;j++)
			{	int loc=-1;
				int flag=0;
				for(int k=0;k<c;k++)
				{
					if(ch[j][k]>='A'&&ch[j][k]<='Z')
					{
						loc=k;
						if(flag>0)
						{
							while(flag)
							{
								ch[j][k-flag]=ch[j][k];
								flag--;
							}
						}
					}
					else if	(ch[j][k]=='?')
					{
						if(loc>-1)
						{
							ch[j][k]=ch[j][loc];
						}
						else
						{
							flag++;
						}
					}
					
					
				}
				if(loc==-1)
				{
				//	cout<<"J"<<j<<"j0"<<j0;
					if(j==j0)
					{j0++;
					//cout<<j0;
					}
					else
					{
						for(int k=0;k<c;k++)
						{
							ch[j][k]=ch[j-1][k];
						}
					}
				}
				else if( j0>0)
				{	
				while(j0)
				{
					for(int k=0;k<c;k++)
					{ch[j-j0][k]=ch[j][k];}
				j0--;
				}
				
				}
				
			}
			
	for(int j=0;j<r;j++)
	{
		for(int k=0;k<c;k++)
		{
		cout<<ch[j][k];
		}
		cout<<endl;
	}
	}
	return 0;
}
