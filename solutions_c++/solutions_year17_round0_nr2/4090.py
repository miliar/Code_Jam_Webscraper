#include <iostream>
#include <string>
using namespace std;
char f(char c)
{
	int num=c-'0';
	num--;
	char c1=char(num+'0');
	return c1;
}
int main()
{
	int T;
	string s,s1;
	cin>>T;
	int i,j,k;
	int mark;
	for(i=1;i<=T;i++)
	{
		cin>>s;
		mark=-1;
		s1="";
		for(j=0;j<s.size();j++)
		{
			if((j-1>=0)&&s[j]<s[j-1])
			{
				mark=j;
				s[j-1]=f(s[j-1]);
				break;
			}
		}
		if(mark==-1)
		{
			s1=s;
		}
		else
		{
			for(j=mark-1;j>=0;j--)
			{
				if(j-1>=0&&s[j]<s[j-1])
				{
					s1='9'+s1;
					s[j-1]=f(s[j-1]);
				}
				else if(s[j]!='0')
				{
					s1=s[j]+s1;
				}
			}
			for(j=mark;j<s.size();j++)
			{
				s1+='9';
			}
		}
		cout<<"Case #"<<i<<": "<<s1<<endl;
	}
	return 0;
}
