
// ... copyright @ASHISH JHA ... _/\_******
/*Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
  Ashish_Jha wrote this file. As long as you retain this notice you
  can do whatever you want with this stuff. If we meet some day, and you think
  this stuff is worth it, you can buy me a beer or coffee in return
*/
#include<bits/stdc++.h>
#include<fstream>
using namespace std;
typedef long long int ll;
#define MOD 1000000007
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<ll,pair<ll,ll>>
#define psi pair<string,ll>
#define INF 1000000000

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t;
	cin>>t;
	ll re=1;
	while(t--)
	{
		string str;
		ll n;
		cin>>str>>n;
		cout<<"Case #"<<re<<": ";
		ll count_=0,flg=0;
		re++;
		for(ll i=0;i<str.size();++i)
		{
			if(str[i]!='+')
			{
				for(ll j=0;j<i+n;++j)
				{
					if(j>(str.size()-1))
					{
						count_++;
						break;
					}
					if(str[j]=='+')
					     str[j]='-';
					     else
					     str[j]='+';
				}
				if(count_>0)
				break;
				flg++;
			}
		}
		if(!count_)
            cout<<flg<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;

	}
	return 0;
}
