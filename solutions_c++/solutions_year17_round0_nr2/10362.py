#include <bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t,n,cp,rem,flag,x;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		while(n>=1)
		{
			flag=1;
			cp=n;
			rem=cp%10;
			cp=cp/10;
			while(cp!=0)
			{
				x=cp%10;
				if(x<=rem)
				{
					rem=x;
					cp=cp/10;
				}
				else
				{
					flag=0;
					break;
				}
			}
			if(flag==1)
			{
				cout<<"Case #"<<i<<": "<<n<<"\n";
				break;
			}
			n--;
		}
	}
}