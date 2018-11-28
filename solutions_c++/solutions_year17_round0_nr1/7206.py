#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	int t,k,count,length,flag=0,j=1;
	char s[1000];
	cin>>t;
	while(t--)
	{
		cin>>s;
		cin>>k;
		count = 0;
		length = strlen(s);
		for(int i=0 ; i<=length-k ; i++)
		{
			if(s[i]==45)
			{
				for(int l=i ; l<i+k ; l++)
				{
					if(s[l]==45)
						s[l] = 43;
					else
						s[l] = 45;
				}
			
				count += 1;
			}
		}
		
		for(int i=length-k ; i<length ; i++)
		{
			if(s[i] == 45)
				flag = 1;
		}
		
		cout<<"Case #"<<j++<<": ";
		if(flag==1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<count<<endl;
		flag = 0;
	}
	
	return 0;
}
