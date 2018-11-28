#include<bits/stdc++.h>

using namespace std;

int main()
{
	int test;
	cin>>test;
	int t=test;
	while(test--)
	{
		char s[1000];
		cin>>s;
		char c = 'a';
		int k=1,temp=0,temp1=-1;
		int len = strlen(s),flag=0;
		for(int i=0;i<len-1;i++)
		{
			if(s[i]>s[i+1])
			{
				for(int j=i+1;j<len;j++)
				{
					s[j]='0';
				}
				flag=1;	
			}
		}
		if(flag==1)
		{
			for(int i=len-1;i>=0;i--)
			{
				if(s[i] != '0')
				{
					if(c == 'a' && i!=0)
					{
						c = s[i];
						k=i;
						temp=k;
					}
					else if(s[i] == c && s[i+1] == c)
					{
						k=i+1;
						temp1=k;
						if(i==0)
						{
//							cout<<k<<" 1"<<endl;
							for(int a=k;a<len;a++)
							{
								s[a] = '9';
							}
							s[k-1] = s[k-1]-1;					
						}
					}
					else
					{
						if(k == temp && temp != temp1)
							k=k+1;
//						cout<<k<<endl;
						for(int a=k;a<len;a++)
						{
							s[a] = '9';
						}
						s[k-1] = s[k-1]-1;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<t-test<<": ";
		if(s[0]!='0' || len==1)
			cout<<s<<endl;
		else
		{
			for(int i=1;i<len;i++)
				cout<<s[i];
			cout<<endl;
		}
	}
	return 0;
}
