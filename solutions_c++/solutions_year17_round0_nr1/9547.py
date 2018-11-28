#include <iostream>
#include <string>
using namespace std;
int n,count=0;
string flip(string str,int i)
{
	for(int j=i;j<i+n;j++)
	{
		if(str[j]=='+')
			str[j]='-';
		else
			str[j]='+';
	}
	return str;
}
int pancake(string str,int len)
{	
	count=0;
	for(int i=0;i<=len-n;i++)
	{
		if(str[i]=='-')
			{
				str=flip(str,i);
				count=count+1;
			}
	}
	for(int i=0;i<len;i++)
	{
		if(str[i]=='-')
			{
				return -1;	
			}
	}
	return count;
}

int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	int len,ans;
	string str;
	cin>>str;
	cin>>n;
	len=str.length();
	ans=pancake(str,len);
	if(ans==-1)
	cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
	else
	cout<<"Case #"<<k<<": "<<ans<<endl;
	
		
	}
	return 0;
}