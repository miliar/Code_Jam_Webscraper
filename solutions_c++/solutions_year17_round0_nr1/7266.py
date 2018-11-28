#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <algorithm>
#include <vector>

using namespace std;
int c=1;
void solve()
{
	string s;
	cin>>s;
	int k,count=0,l,flag=0;
	cin>>k;
	int n=s.size();
	for(int i=0;i<n;)
	{
		l=i+k;
		if(s[i]=='-')
		{
			while(l <= n && i!=l)
			{
				if(s[i]=='-')
				s[i]='+';
				else if(s[i]=='+')
				s[i]='-';
				i++;
			}
			if(l > n)
			{
				cout<<"Case #"<<c++<<": "<<"IMPOSSIBLE"<<endl;
				return;
			}
			else if(i==l)
			{
				flag=0;
				for(int j=0;j<n;j++)
				{
					if(s[j]=='-')
					{
						flag=1;
						i=j;
						break;
					}

				}

			}
			count++;
			if(flag==0)
				break;
		}
		else
		i++;
	}
	if(flag==0)
	cout<<"Case #"<<c++<<": "<<count<<endl;
}
int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

	int t;
	cin>>t;
	while(t--)
	{
		solve();
	}
}
