#include <bits/stdc++.h>
#include <string.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large-practice.out","w",stdout);
	int test;
	cin>>test;
	for(int m=1;m<=test;m++)
	{
		string s;
		int k,flip=0,success=0;
		cin>>s>>k;
		for (int a = 0; a < s.length(); a++)
		{
			
			if (s[a]=='+')
				success++;
		}
		if (success==s.length())
		{
			cout<<"Case #"<<m<<": 0"<<endl;
			continue;
		}
		int i=0;
		for(i=0;i<s.length()-k+1;i++)
		{
			if(s[i]=='-')
			{
				//cout<<"i "<<i<<endl;
				for (int j = i; j < i+k; j++)
				{
					//cout<<"changing this i "<<j<<endl;
					if(s[j]=='-')
						s[j]='+';
					else s[j]='-';
					
					//cout<<"inter s "<<s<<endl;
				} flip++;
			}
		}//cout<<"final s "<<s<<endl;
		//cout<<flip<<endl;
		success=0;
		for (int a = 0; a < s.length(); a++)
		{
			
			if (s[a]=='+')
				success++;
		}
		if (success==s.length())
		{
			cout<<"Case #"<<m<<": "<<flip<<endl;
			continue;
		}

		if(i==s.length()-k+1)
			cout<<"Case #"<<m<<": IMPOSSIBLE"<<endl;
	}
}