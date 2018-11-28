#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
ll find(ll n,ll k)
{
	ll cum=1;
	n--;
	ll val1;
	ll val2;
	ll cnt1;
	ll cnt2;
	if(n%2==0)
	{
		val1=n/2;
		cnt1=2;
		cnt2=0;
		val2=-1;
	}
	else
	{
		val1=n/2;
		val2=n-n/2;
		cnt1=1;
		cnt2=1;
	}
	ll temp;
	while(true)
	{
		if(cum+cnt1+cnt2>=k)
			break;
		cum=cum+cnt1+cnt2;
		if(val2!=-1)
		{
			if(val1/2!=val2/2)
			{
				temp=val1/2;
				val1=temp;
				val2=temp+1;
				cnt1=cnt2+2*cnt1;
				cnt2=cnt2;
			}
			else
			{
				temp=val1/2;
				val1=temp-1;
				val2=temp;
				cnt1=cnt1;
				cnt2=cnt1+2*cnt2;
			}
		}
		else
		{
			temp=val1;
			temp--;
			if(temp%2==0)
			{
				val1=temp/2;
				cnt1=2*cnt1;
				cnt2=0;
				val2=-1;
			}
			else
			{
				val1=temp/2;
				val2=temp-temp/2;
				cnt1=cnt1;
				cnt2=cnt1;
			}		
		}
		
		// cout<<val1<<" "<<val2<<" "<<cnt1<<" "<<cnt2<<" "<<cum<<endl;
		
	}

	// cout<<val1<<" "<<val2<<endl;
	if(val2==-1)
		return val1;
	if(cum+cnt2>=k)
		return val2;
	else
		return val1;

}
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	ll ans;
	ll n,k;
	while(t--)
	{
		z++;
		cout<<"Case #"<<z<<": ";
		cin>>n>>k;
		if(k==1)
		{
			n--;
			cout<<(n-(n/2))<<" "<<n/2<<endl;
			continue;
		}
		ans=find(n,k);
		// cout<<ans<<endl;
		ans--;
		cout<<(ans-(ans/2))<<" "<<ans/2<<endl;
		// z++;
	}
}