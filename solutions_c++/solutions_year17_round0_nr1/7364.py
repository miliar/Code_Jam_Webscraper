#include <iostream>
#include <cstring>
#include <string.h>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for (int h = 0; h < t; ++h)
	{
		string s;
		int k;
		int output=0;
		bool temp = 0;
		cin>>s;
		cin >>k;
		int i=0;
		int n=s.size();
		while(true)
		{
			if(s[i]=='+')
			{
				i++;
				if(i==n){break;}
			}
			else
			{
				if(i+k-1<n)
				{
					for(int j=i;j<i+k && j<n;j++)
					{
						if(s[j]=='+'){s[j]='-';}
						else{s[j]='+';}
					}
					i++;
					output++;
					if(i==n){break;}
				}
				else
				{
					break;
				}
			}
		}
		for (int i = 0; i < n; ++i)
		{
			if(s[i]=='-'){temp=1;}
		}

		if(temp){cout<<"Case #"<<h+1<<": IMPOSSIBLE"<<endl;}
		else{cout<<"Case #"<<h+1<<": "<<output<<endl;}
	}
}