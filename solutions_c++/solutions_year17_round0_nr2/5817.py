#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,q=1;
	cin>>t;
	while(t--)
	{
		char num[25],k=0;//taking input 
		int i,mem,local=0;
		cin>>num;
		mem=strlen(num);//length of string
		if(mem==1)
		{cout<<"Case #"<<q++<<": ";
			cout<<num<<endl;
		}
		else
		{
			for(i=0;i<mem-1;i++)//loop
			{
			    if(num[i+1]<num[i] && num[i]!='1' && (num[i]-num[i-1])==0)
				{
				    num[0]-=1;
				    for(i=1;i<mem;i++)   
				    num[i]='9';
				}         
				else if(num[i+1]<num[i] && num[i]!='1' && abs(num[i+1]-num[i])>0)
				{
					local=i+1;
					num[i]-=1;
					for(i=local;i<mem;i++)
						num[i]='9';
				}
				
				else if(num[i+1]<num[i] && num[i]=='1')
				{
					k=1;
					for(i=0;i<mem;i++)
						num[i]='9';
				}    
			}
			if(k==0)
			{
			    cout<<"Case #"<<q++<<": ";
				for(i=0;i<mem;i++)
					cout<<num[i];
				cout<<endl;
			}
			else if(k==1)
			{
			    cout<<"Case #"<<q++<<": ";
				for(i=1;i<mem;i++)
					cout<<num[i];
				cout<<endl;
			}
		}

	}
	return 0;
}
