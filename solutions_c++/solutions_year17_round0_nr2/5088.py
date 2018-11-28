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
		cin>>str;
		cout<<"Case #"<<re<<": ";
		ll si=str.size();
		if(str.size()==1)
		   cout<<str;
		else
		{
			char ch=str[0];
			ll rt=-1;
			for(ll i=0;i<str.size();++i)
			{
				if(ch>str[i])
				{
					rt=i-1;
					break;
				}
				ch=str[i];
			}
			if(rt==-1)
			cout<<str;
			else
			{
               while(rt>=0 && str[rt]<='1')
                rt--;
					if(rt<0)
					{
						si--;
						for(ll i=0;i<si;++i)
						cout<<'9';

					}
					else
					{
						char isval=str[rt];
						for(;rt>=0;rt--)
						{
							if(str[rt]!=isval)
							break;
							isval=str[rt];
						}
						rt++;
						for(ll i=0;i<rt;++i)
						{
							cout<<str[i];
						}
						cout<<(char)((int)str[rt]-1);
                   for(ll i=rt+1; i<=(si-1); ++i)
                    cout<<'9';
					}
			}
		}
		cout<<endl;
		re++;
		}
		return 0;
	}
