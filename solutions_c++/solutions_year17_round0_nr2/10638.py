#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int t;
int main()
{
freopen("q1.in","r",stdin);
freopen("q1.out","w",stdout);
cin >> t;
ll res;
for(int i=1; i<=t; i++)
{
	ll n,j;
	cin >> n;
	for(j=n; j>=1; j--)
	{
		ll temp = j;
		bool flag = 1;
		int x, y=10;
		while(temp)
		{
			x = temp%10;
			if(x <= y)
			{
				y = x;
			}
			else
			{
				flag = 0;
				break;
			}
			temp /= 10;
		}
		if(flag)
		{
			cout<<"Case #"<<i<<": "<<j<<endl;
			break;
		}		
	}
}
return 0;
}

