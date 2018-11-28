#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int counter=0;
	while(t--)
	{	counter++;
		char s[1000];
		int k;
		cin>>s>>k;
		int length=0;
		while(s[length]!='\0')
		{
			length++;
		}
		int count=0,flag=0;
		//cout<<"Length :"<<length<<endl;
		for(int i=0;i<length;i++)
		{
			if(s[i]=='-')
			{
				if((length-i)/k >=1)
				{
					count++;
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else s[j]='-';
				}
				//i=i+k;
				}
				else 
					{
						cout<<"Case #"<<counter<<": "<<"IMPOSSIBLE"<<endl;
						flag=1;
						break;
					}
				
			}
			
		}
		if(flag!=1)
			cout<<"Case #"<<counter<<": "<<count<<endl;
	}

}