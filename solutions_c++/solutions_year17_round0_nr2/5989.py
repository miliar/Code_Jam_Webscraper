#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;

string ans;
void tidy(ll num)
{
	if(num<=0)
	{
		return;
	}
	if( (num/10) ==0 )
	{
		ans+= ('0'+num);
		return;
	}

	ll n1=num%10;
	num/=10;

	ll flag=0,temp=num,mn=n1;

	while(temp)
	{
		if(temp%10 > mn )
			{
				flag=1;
				break;
			}

		if(temp%10 < mn)
		mn = temp%10;

		temp/=10;

	}

	if(flag)
	{
		ans +='9';
		tidy(num-1);
	}
	else
	{
		ans += (n1+'0');
		tidy(num);
	}

}

int main() {

	ll tc;cin>>tc;

	for(ll t=1;t<=tc;t++)
	{
		
		ll num;cin>>num;
		ans="";

		tidy(num);
		

		cout<<"Case #"<<t<<": ";

		for(ll i=ans.length()-1;i>=0;i--)
		{
			cout<<ans[i];
		}
		
		cout<<"\n";

	}

	return 0;
}