#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
const ll nINF = -(1e17);
ll T, n, k;
string str;
ll minus[1005];

int main()
{
	ll t=1;
	cin>>T;
	while(t<=T)
	{
		cin>>str>>k;
		n = str.size();
		ll pos=0, ans = 0;
		bool found = 0;
		for(ll j=pos; j<n; ++j)
			{
				if(str[j]=='-')
				{
					pos = j;
					found = 1;
					break;
				}
			}
		if(found)
		{
			bool flag = 0;
			bool error = 0;
			while(1)
			{
				//cout<<"pos = "<<pos<<endl;
				if(pos==n)
					{flag=1;break;}

				for(ll j=0; j<k; ++j)
				{
					if(pos+j>=n)
					{
						error = 1;
						break;
					}
					str[pos+j] = (str[pos+j]=='+'?'-':'+');
				}
				if(error)
					{break;}
				++ans;
				bool nxt = 0;
				for(ll j=pos; j<n; ++j)
				{
					if(str[j]=='-')
					{
						pos = j;
						nxt = 1;
						break;
					}
				}
				//cout<<"nxt  = "<<nxt<<" pos = "<<pos<<endl;
				if(!nxt)
					{flag=1;break;}
			}

		if(flag)
			cout<<"Case #"<<t<<": "<<ans<<endl;
		else
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		
		}
		else
		{
			cout<<"Case #"<<t<<": "<<0<<endl;	
		}

		++t;
	}
	return 0;
}