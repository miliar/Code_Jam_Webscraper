#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int a,i,amt,temp,k,j,r;
	cin>>a;
	r=1;
	while(a--)
	{
		amt=0,temp=0;
		string m;
		cin>>m;
		cin>>k;
		long long int l=m.length();
		if (k<=0)
		cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
		for(i=0;i<=(l-k);i++)
		{
			if(m[i]=='-')
			{
				m[i]='+';
				for(j=i+1;j<i+k;j++)
				{
					if(m[j]=='-')
					m[j]='+';
					else if(m[j]=='+')
					m[j]='-';
				}
				amt++;
				
				
			}
		}
		
        	for(i=0;i<l;i++)
			{
				if(m[i]=='-')
				{
					temp=1;
					break;
				}
			}
			if(temp==0)
			{
				cout<<"Case #"<<r<<": "<<amt<<endl;
			}
			else
			cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;
		}
		r++;
     }
    
	
	return 0;
}
