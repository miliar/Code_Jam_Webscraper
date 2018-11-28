#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int h,z,attem,temporary,o,n,nhi;
	cin>>h;
	nhi=1;
	while(h--)
	{
		attem=0,temporary=0;
		string b;
		cin>>b;
		cin>>o;
		long long int l=b.length();
		if (o<=0)
		cout<<"Case #"<<nhi<<": "<<"IMPOSSIBLE"<<endl;
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
				attem++;
				
				
			}
		}
		
        	for(n=0;n<l;n++)
			{
				if(b[n]=='-')
				{
					temporary=1;
					break;
				}
			}
			if(temporary==0)
			{
				cout<<"Case #"<<nhi<<": "<<attem<<endl;
			}
			else
			cout<<"Case #"<<nhi<<": "<<"IMPOSSIBLE"<<endl;
		}
		nhi++;
     }
    
	
	return 0;
}
