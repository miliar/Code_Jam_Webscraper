#include<iostream>
#include<algorithm>
#include<limits>
#include<vector>
#include<cmath>
#include<bitset>
#include<map>
#include<stdio.h>
#include <iomanip>
#include <cstdio>


using namespace std;

typedef long long ll;
typedef long double ld;

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output2x.txt","w",stdout);
	int t;
	cin>>t;
	int t2=t;
	while(t)
	{
		string s;
		int k;
		cin>>s>>k;
		ll cnt=0;
		int ptr;
		int i;
		int flag=0;
		for(i=0;i<s.size();i++)
		{
			if(s[i]=='-' && i+k>s.size())
			{
				flag=1;
				break;
			}
			else if(s[i]=='-' && i+k<=s.size())
			{
				cnt++;
				int j;
				int flag2=0;
				for(j=0;j<k;j++)
				{
					
					if(s[i+j]=='-')
					{
						s[i+j]='+';
					}
					else
					{
						if(flag2==0)
						{
							ptr=i+j-1;
							flag2=1;
						}
						s[i+j]='-';
					}
				}
				if(flag2==0)
				{
					ptr=i+j-1;
				}
				i=ptr;
			}
			
		}
		if(flag==1)
		{
			cout<<"Case #"<<t2-t+1<<": "<<"IMPOSSIBLE"<<endl;
			
		}
		else
		{
			cout<<"Case #"<<t2-t+1<<": "<<cnt<<endl;
		}
		t--;
	}


	return 0;
}

