#include <bits/stdc++.h>
using namespace std;
#define ll long long 
string return_sorted(long long n)
{
	string s = to_string(n);
	sort(s.begin(),s.end());
	return s;
}
int check(int n)
{
	string s = to_string(n);
	for(int i=1;i<s.length();i++)
	{
		if(s[i]<s[i-1])
			return 0;
	}
	return 1;
}
ll Pow(ll a ,ll b)
{
	ll res=1;
	while(b)
	{
		if(b&1)
		{
			res*=a;
		}
		a*=a;
		b>>=1;
	}
	return res;
}
int main()
{
	freopen("inp.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,n,ans,val;
	cin>>t;
	for(int c = 1;c<=t;c++)
	{
			cin>>n;
		// string sorted = return_sorted(n);
		// stringstream ss(sorted);
		// ss>>val;
		// int flag=0;
		// for(int i=0;i<sorted.length();i++)
		// {
		// 	if(sorted[i]=='0')
		// 	{
		// 		flag=1;
		// 		break;
		// 	}
		// }
		// cout<<sorted<<endl;
		for(int i=n;i>=0;i--)
		{
			if(check(i))
			{
				ans=i;
				break;
			}
		}
		// ans=n;
		// if(val<n)
		// {
		// 	ll ptens = Pow(10,sorted.length()-1);
		// 	cout<<ptens<<endl;
		// 	ans=((n/ptens)-1)*ptens;
		// 	ans+=(ptens-1);
		// 	// if(flag)
		// 	// 	ans=ptens-1;
		// 	// else
		// 	// 	ans=(n/10)*10-1;
		// }	
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	
	
}