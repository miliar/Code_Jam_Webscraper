#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int e,z,upt,tempor,o,n,noi;
	cin>>e;
	noi=1;
	while(e--)
	{
		upt=0,tempor=0;
		string b;
		cin>>b;
		cin>>o;
		long long int l=b.length();
		if (o<=0)
		cout<<"Case #"<<noi<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
		for(n=0;n<=(l-o);n++)
		{
			if(b[n]=='-')
			{
				b[n]='+';
				for(z=n+1;z<n+o;z++)
				{
					if(b[z]=='-')
					b[z]='+';
					else if(b[z]=='+')
					b[z]='-';
				}
				upt++;
				
				
			}
		}
		
        	for(n=0;n<l;n++)
			{
				if(b[n]=='-')
				{
					tempor=1;
					break;
				}
			}
			if(tempor==0)
			{
				cout<<"Case #"<<noi<<": "<<upt<<endl;
			}
			else
			cout<<"Case #"<<noi<<": "<<"IMPOSSIBLE"<<endl;
		}
		noi++;
     }
    
	
	return 0;
}
