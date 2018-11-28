#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	int z,t;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		ll n;
		cin>>n;
		int val[70],i=0,l=0;
		ll temp=n;
		while(temp>0)
		{
			val[l++]=temp%10;
			temp/=10;
		}
		for(i=l-2;i>=0;i--)
		{
			if(val[i]<val[i+1])
				break;
		}
		if(i>=0)
		{
			i++;
			int f=val[i]-1;
			for(;i<l&&val[i]>f;i++)
			{

			}
			i--;
			val[i]=f;
			i--;
			for(;i>=0;i--)
			{
				val[i]=9;
			}
		}
		cout<<"Case #"<<z<<": ";
		if(val[l-1])
			cout<<val[l-1];
		for(i=l-2;i>=0;i--)
			cout<<val[i];
		cout<<endl;
	}
	return 0;
}