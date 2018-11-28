#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int m,v,acp,lnv,c,p,hai;
	cin>>m;
	hai=1;
	while(m--)
	{
		acp=0,lnv=0;
		string k;
		cin>>k;
		cin>>c;
		long long int u=k.length();
		if (c<=0)
				cout<<"Case #"<<hai<<": "<<"IMPOSSIBLE"<<endl;

		else
		{
		for(v=0;v<=(u-c);v++)
		{
			if(k[v]=='-')
			{
				k[v]='+';
				for(p=v+1;p<v+c;p++)
				{
					if(k[p]=='-')
					k[p]='+';
					else if(k[p]=='+')
					k[p]='-';
				}
				acp++;
			}
		}
		
        	for(v=0;v<u;v++)
			{
				if(k[v]=='-')
				{
					lnv=1;
					break;
				}
			}
			if(lnv==0)
			{
				cout<<"Case #"<<hai<<": "<<acp<<endl;
			}
			else
			cout<<"Case #"<<hai<<": "<<"IMPOSSIBLE"<<endl;
		}
		hai++;
     }	
	return 0;
}
