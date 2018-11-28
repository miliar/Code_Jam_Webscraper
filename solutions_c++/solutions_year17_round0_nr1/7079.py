#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	int t;
	in>>t;
	int testnum=0;
	while(t--)
	{
		testnum++;
		string s;
		in>>s;
		int num;
		in>>num;
		int len=s.size();
		int ans=0;
		for(int i=0;i<=len-num;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				for(int j=i;j<i+num;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		bool flag=true;
		for(int i=len-num+1;i<len;++i)
		{
			if(s[i]=='-')
			{
				flag=false;
				break;
			}
		}
		out<<"Case #"<<testnum<<": ";
		if(flag)
			out<<ans<<endl;
		else
			out<<"IMPOSSIBLE"<<endl;
			
	}
}
