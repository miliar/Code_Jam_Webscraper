#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int counter=0;
		int flag=0;
		int i=0;
		while(s[i+k]!='\0')	
		{
			
			if(s[i]=='-')
			{
				int count=i;
				counter++;
				for(int z=0;z<k;z++)
				{
					if(s[z+count]=='-')
						s[z+count]='+';
					else	
						s[z+count]='-';
				}
			}
			i++;
		}
		int b=i;
		if(s[b]=='-')
		{
			while(s[b++]!='\0')
			{
				if(s[b]=='-')
					s[b]='+';
				else if(s[b]=='+')
					s[b]='-';
				
			}
		counter++;
		}	
		
		while(s[i++]!='\0')
		{	
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		cout<<"Case #"<<q<<": ";
		if(flag==1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<counter<<endl;			
	}
	return 0;
}
