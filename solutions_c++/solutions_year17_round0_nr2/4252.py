#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int l=s.length();
		int c=0,j;
		for(j=0;j<l-1;j++)
		{
			if(s[j]==s[j+1])
			{
				c++;
			}
			else if(s[j]>s[j+1])
			break;
			else
			c=0;
		}
		if(j!=l-1)
		{
			j=j-c;
			s[j]--;
			for(int k=j+1;k<l;k++)
			{
				s[k]=57;
			}
		}
		if((s[0]-48)!=0)
		cout<<"Case #"<<i+1<<": "<<s<<endl;
		else
		{
			cout<<"Case #"<<i+1<<": ";
			for(int z=1;z<l;z++)
			cout<<s[z];
			cout<<endl;
		}
	}
}
