#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-output-final.out","w",stdout);
	int t,a[5],b[5];
	char jo;
	char c[102][1005],ch[102][1005];
	cin>>t;
	for(int i=1;i<=t+1;i++)
	{
		int j1=0,w=0;
		int no=0,j,no_of_moves=0;
		if(i==1)
		{
			gets(c[i]);
		
		}
		int co=0;
			
		if(i!=1)
		{
		
			gets(c[i]);
			for(int y=0;;y++)
			{
				if(c[i][y]==' ')
				{
					for(w=0;;w++)
					{
						if(c[i][y+w]=='\0')
						{
							goto a;
						}
						else
							jo= c[i][y+w+1];
							a[w]=atoi(&jo);
					}
				}
			}
			a:
				co=0;
				for(int z=w-2;z>=0;z--)
				{
						
					j1 = j1+a[z]*pow(10,co);
					co++;
				}
			
			ch[i][0]='+';
			for( j=0;;j++)
			{
				if(c[i][j]!=' ')
					{
						ch[i][j+1]=c[i][j];
						no++;
					}
				else
					break;
			}
			cout<<"Case #"<<i-1<<": ";
			for(j=0;j<=no;j++)
			{
				if(no-j>=j1)
				{
				
					if(ch[i][j]!=ch[i][j+1])
					{
				
					
							for(int k=0;k<j1;k++)
							{
								if(ch[i][j+k+1]=='+')
									ch[i][j+k+1]='-';
								else
									ch[i][j+k+1]='+';
								
							}
							no_of_moves++;
					}
				}
			}
			int count=0;
			for(int j=0;j<=no;j++)
			{
				if(ch[i][j]=='-' && count==0)
				{
				
					cout<<"IMPOSSIBLE"<<endl;
					count++;
				}	
			}
	
			if(count==0)
				cout<<no_of_moves<<endl;
		}
	}
	
}
