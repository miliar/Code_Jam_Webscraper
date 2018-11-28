#include <bits/stdc++.h>
#define ll long long
using namespace std;

bool tidy(ll n)
{
	ll a=111111111111111111,b;
	while(n)
	{
		b=n%10;
		if(b<=a)
			a=b;
		else
			return false;
		n/=10;
	}
	return true;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll t,i,j=1,a,b;
	cin>>t;
	while(t--)
	{
		cin>>a;
		if((a/10)==0)
			cout<<"Case #"<<j<<": "<<a<<endl;
		else{
			for(i=a;i>=0;i--)
			{
				if(tidy(i))
					break;
			}
			cout<<"Case #"<<j<<": "<<i<<endl;
		}
		j++;
	}
	
	return 0;
}
