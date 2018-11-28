#include<bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL)
typedef long long ll;
int main()
{
	fast;
	ll t,ojha=0;
	cin>>t;
	while(t--)
	{
		ojha++;
		ll i,j,k;
		string str;
		cin>>str;
		cin>>k;
		ll len=str.length();
		ll cnt=0;
		for(i=0;i<=len-k;i++)
		{
			if(str[i]=='-')
			{
				cnt++;
				for(j=i;j<i+k;j++)
				{
					if(str[j]=='-')
						str[j]='+';
					else
						str[j]='-';
				}
			}
		}
		bool ok=true;
		for(i=0;i<len;i++)
		{
			if(str[i]=='-')
				ok=false;
		}
		cout<<"Case #"<<ojha<<": ";
		if(!ok)
		{
			cout<<"IMPOSSIBLE\n";
		}
		else
		{
			cout<<cnt<<"\n";
		}
	}
}