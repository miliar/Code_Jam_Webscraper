#include <bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	cin>>test;
	int count=0;
	while(test--)
	{
		count++;
		
		string s;
	cin>>s;
	int k;
	cin>>k;
	cout<<"Case #"<<count<<": ";
	int n = s.length();
	int min_chg =0;
	int i;
	for( i =0;i<=n-k;i++)
	{
		if(s[i]=='-')
		{
			min_chg++;
			for(int j =i;j<i+k;j++)
			{
				if(s[j]=='+')
					s[j] = '-';
				else
					s[j]='+';
			}
		}
	}
	for( i = n-k+1;i<n;i++)
	{
		if(s[i]=='-')
			break;
	}
	if(i==n)
		cout<<min_chg<<endl;
	else
		cout<<"IMPOSSIBLE"<<endl;

	}
}
