#include<bits/stdc++.h>
#define MOD 1000000007
using namespace std;
typedef long long int ll;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	ll t,p;
	cin>>t;
	for(p=1;p<=t;p++)
	{
		string s;
		ll k,i=0,count=0,c=0,flag=0;
		cin>>s;
		cin>>k;
		while(i<s.length())
		{
			if(s[i]=='-')
			{
				s[i]='+';
				ll j=i+1,m=k;
				while(--m)
				{
					if(j<s.length())
					{
						if(s[j]=='+')
						s[j]='-';
						else
						s[j]='+';
						j++;
					}
					else
					break;
				}
				if(m==0)
				{
					count++;
				}
				else
				flag=1;
			}
			i++;
		}
		if(flag==0)
		cout<<"Case #"<<p<<": "<<count;
		else
		cout<<"Case #"<<p<<": "<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}


