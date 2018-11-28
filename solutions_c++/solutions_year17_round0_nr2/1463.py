#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
bool isgood(ll n)
{
	int last=n%10;
	while(n>0)
	{
		if(n%10<=last)
		{
			last=n%10;
		}
		else
		{
			return false;
		}
		n/=10;
	}
	return true;
}
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	int arr[20];
	ll temp;
	int pos;
	int con;
	ll n;
	while(t--)
	{
		z++;
		cin>>n;
		cout<<"Case #"<<z<<": ";
		if(n<10)
		{
			cout<<n<<endl;
			continue;
		}
		temp=n;
		pos=0;
		while(temp>0)
		{
			arr[pos]=temp%10;
			pos++;
			temp/=10;
		}
		for(int i=0;i<pos/2;i++)
			swap(arr[i],arr[pos-1-i]);
		con=-1;
		for(int i=0;i<pos-1;i++)
		{
			if(arr[i]>arr[i+1])
			{
				con=i;break;
			}
		}
		if(con==-1)
		{
			cout<<n<<endl;
			continue;
		}
		int i=con;
		while(i>0 && arr[i]==arr[i-1])
		{
			i--;
		}
		// cout<<i<<endl;
		arr[i]=arr[i]-1;
		for(int j=i+1;j<pos;j++)
			arr[j]=9;
		ll ans=0;
		for(int i=0;i<pos;i++)
		{
			ans=ans*10+arr[i];
		}
		cout<<ans<<endl;
	}
}