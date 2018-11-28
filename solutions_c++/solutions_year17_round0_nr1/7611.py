#include<iostream>
#include<string>
using namespace std;
int main()
{
	int tc,k,co=0,flag=0,n,i,j,p;
	string str;
	cin>>tc;
	for( i=0;i<tc;i++)
	{
		cin>>str;
		cin>>k;
		n=str.size();
		co=0;
		flag=0;
		for( j=0;j<str.size();j++)
		{
			if(str[j]=='-')
			{
				for(p=0;p<k;p++)
				{
					if((j+p)!=n)	
					{
						if(str[j+p]=='-')
						str[j+p]='+';
						else
						str[j+p]='-';
					}
					else
					{
						flag=1;
						break;
					}
						
				}		
					
			co=co+1;				
			}	
			if(flag==1)
			break;	
			
		}
		if(flag==1)
		cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<i+1<<": "<<co<<endl;
	}
return 0;
}
