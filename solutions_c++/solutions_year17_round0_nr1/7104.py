#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;
main()
{
	ifstream file;
	ofstream outs;
	file.open("doc3.txt");
	outs.open("out.txt");
	int t;
	file>>t;
	int tc=1;
	while(t--)
	{
		string s;
		file>>s;
		long long int k;
		file>>k;
		int c1=0,count=0;
		while(c1<=s.length()-k)
		{
			if(s[c1]=='-')
			{
				count++;
				for(int i=0;i<k;i++)
				{
				if(s[c1+i]=='+')
				s[c1+i]='-';
				else
				s[c1+i]='+';
			    }
			}
			c1++;
		}
		int flag=0;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
			
			flag=1;
			//continue;	
			}
		}
		if(flag==0)
		outs<<"Case #"<<tc++<<": "<<count<<endl;
		else
		outs<<"Case #"<<tc++<<": "<<"IMPOSSIBLE"<<endl;
	}
}
