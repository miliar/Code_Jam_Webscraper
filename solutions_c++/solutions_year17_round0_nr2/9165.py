#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iterator>
#include <bitset>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <string>
#include <cstring>
#include <climits>
using namespace std;
typedef long long ll;
ll n;
int digs;
int main()
{
	int t;
	cin>>t;
	ll temp;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		temp=n;
		digs=0;
		while(temp)
		{
			digs++;
			temp/=10;
		}
		int prev=1;
		ll ans=0;
		ll poss=0;
		for(int j=digs-1;j>=1;j--)
				poss=poss*10+9;
		for(int j=1;j<=digs;j++)
		{
			int fl=0;
			//cout<<"ENTERS at "<<j<<" as "<<ans<<endl;
			ll cur=0;
			for(int k=prev;k<=9;k++)
			{
				temp=ans;
				for(int x=j;x<=digs;x++)
					temp=temp*10+k;
				if(temp<=n)
				{
					prev=k;
					temp=ans;
					temp=temp*10+k;
					cur=temp;
					fl=1;
				}
			}
			//cout<<" FOr the dig "<<j<<" "<<cur<<endl;
			if(!fl)
			{
				ans=poss;
				break;
			}
			else
				ans=cur;
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";		
	}
	return 0;
}