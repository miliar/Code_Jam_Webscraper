#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int en,o,accept,hnd,i,w,ayu;
	cin>>en;
	ayu=1;
	while(en--)
	{
		accept=0,hnd=0;
		string d;
		cin>>d;
		cin>>i;
		long long int p=d.length();
		if (i<=0)
		cout<<"Case #"<<ayu<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
		for(o=0;o<=(p-i);o++)
		{
			if(d[o]=='-')
			{
				d[o]='+';
				for(w=o+1;w<o+i;w++)
				{
					if(d[w]=='-')
					d[w]='+';
					else if(d[w]=='+')
					d[w]='-';
				}
				accept++;
			}
		}
		
        	for(o=0;o<p;o++)
			{
				if(d[o]=='-')
				{
					hnd=1;
					break;
				}
			}
			if(hnd==0)
			{
				cout<<"Case #"<<ayu<<": "<<accept<<endl;
			}
			else
			cout<<"Case #"<<ayu<<": "<<"IMPOSSIBLE"<<endl;
		}
		ayu++;
     }	
	return 0;
}
