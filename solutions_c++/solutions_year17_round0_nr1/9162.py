#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	long long int t,m,count,tempry,k,no,num;
	cin>>t;
	num=1;
	while(t--)
	{
		count=0,tempry=0;
		string a;
		cin>>a;
		cin>>k;
		long long int len=a.length();
		if (k<=0)
		cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
		for(no=0;no<=(len-k);no++)
		{
			if(a[no]=='-')
			{
				a[no]='+';
				for(m=no+1;m<no+k;m++)
				{
					if(a[m]=='-')
					a[m]='+';
					else if(a[m]=='+')
					a[m]='-';
				}
				count++;
				
				
			}
		}
		
        	for(no=0;no<len;no++)
			{
				if(a[no]=='-')
				{
					tempry=1;
					break;
				}
			}
			if(tempry==0)
			{
				cout<<"Case #"<<num<<": "<<count<<endl;
			}
			else
			cout<<"Case #"<<num<<": "<<"IMPOSSIBLE"<<endl;
		}
		num++;
     }
    
	
	return 0;
}

