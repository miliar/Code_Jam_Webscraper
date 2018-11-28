#include<bits/stdc++.h>
using namespace std;
int main()
{
string s;
int k,t;
int c=1;
cin>>t;
while(t--)
{
	cin>>s;
	cin>>k;
	int size=s.length();
	int count=0,x=0;
	for(int i=0;i<size-k+1;i++)
	{
		if(s[i]=='-')
		{
		  for(int j=0;j<k;j++)
			if(s[i+j]=='-')
				s[i+j]='+';
			else
				s[i+j]='-';
		  count++;
		}
	}
	for(int i=0;i<size;i++)
	{
		if(s[i]=='-')
		{
			x=1;
			cout<<"Case #"<< c <<": IMPOSSIBLE"<<endl;
			break;
		}
	}
	if(x!=1)
	cout<<"Case #"<< c <<": "<< count<<endl;
	c++;
}
return 0;
}
