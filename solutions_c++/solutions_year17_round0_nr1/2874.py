#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

int main()
{
	
	int n;
	cin>>n;
	for (int t=1;t<=n;t++)
	{
		string s;
		int k,flips=0;
		cin>>s>>k;
		for (int i=0;i+k<=s.size();i++)
		{
			if(s[i]=='+')
			{
				
				continue;
			}
			flips++;
			for (int j=i;j<i+k;j++)
			{
				s[j]=s[j]=='+'?'-':'+';
			}

		}
		cout<<"Case #"<<t<<": ";
		if(count(s.begin(),s.end(),'-'))
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<flips<<endl;
	}
	return 0;
}
