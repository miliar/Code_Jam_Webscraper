#include <bits/stdc++.h>
using namespace std;

long long n , t;
set < long long > good;

void gen(int x , long long num , int last)
{
	if(num > 1e18 || x > 18) return;
	
	good.insert(num);

	for(int i=last;i<=9;i++)
	{
		gen(x + 1 , num * 10 + i , i);
	}
}


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	gen(0 , 0 , 1);
	vector < long long > v;
	for(set<long long>::iterator it = good.begin();it!=good.end();it++) v.push_back(*it);
	
	cin >> t;
	
	for(int q=1;q<=t;q++)
	{
		cin >> n;
		
		long long ans = 0;
		
		for(int i=v.size()-1;i>=0;i--)
		{
			if(v[i] <= n)
			{
				ans = v[i];
				break;
			}	
		}
	
		printf("Case #%d: %I64d\n",q,ans);
	}
	
}