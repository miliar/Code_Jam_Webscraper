#include<iostream>
#include<algorithm>
#include<limits>
#include<vector>
#include<cmath>
#include<bitset>
#include<map>
#include<stdio.h>
#include <iomanip>


using namespace std;

typedef long long ll;
typedef long double ld;

int main()
{
	int t;
	int t2;	
	cin>>t;
	t2=t;
	while(t)
	{
		ll n;
		cin>>n;
		vector<int> dig;
		int i;
		while(n!=0)
		{
			dig.push_back(n%10);
			n=n/10;
		}
		int flag=0;
		int ptr;
		for(i=dig.size()-1;i>0;i--)
		{
			if(dig[i]>dig[i-1])
			{
				//cout<<i<<endl;
				//flag=1;
				int j;
				for(j=i+1;j<dig.size();j++)
				{
					if(dig[j]!=dig[i])
					{
						//j++;
						break;
					}
				}
				ptr=j-1;
				dig[ptr]--;
				for(j=ptr-1;j>=0;j--)
				{
					dig[j]=9;
				}
				break;
			}
		}
		cout<<"Case #"<<t2-t+1<<": ";
		for(i=dig.size()-1;i>=0;i--)
		{
			if(dig[i]!=0)
			{
				flag=1;
			}
			if(flag!=0)
			{
				cout<<dig[i];
			}
			
		}
		cout<<endl;
		
		t--;
	}


	return 0;
}

