#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	string arr[t];
	for(int i=0;i<t;i++)
	{
		long int n;
		cin>>n;
		int r;char ch;
		string s="";
		while(n>0)
		{
			r=n%10+48;
			ch=r;
			s=ch+s;
			n=n/10;
		}
		int l=s.length();
		if(l==1) arr[i]=s;
		else
		{
		for(int j=l-1;j>0;j--)
		{
			
			 if (s[j]=='0') 
			{
				s[j-1]=s[j-1]-1;
				s[j]='9';
				for(int k=l-1;k>j;k--)
				s[k]='9';	
			}
			 else if (s[j]<s[j-1]) 
			{
				s[j-1]=s[j-1]-1;
				s[j]='9';
				for(int k=l-1;k>j;k--)
				s[k]='9';
			}
			
		}
		if(s[0]=='0') arr[i]=s.substr(1);
		else arr[i]=s;
		}
		
	}
	for(int i=0;i<t;i++)
	cout<<"Case #"<<(i+1)<<": "<<arr[i]<<endl;
return 0;
	
}
