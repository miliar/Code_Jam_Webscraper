/*input
1
851
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define MAXN 100005
#define INF LLONG_MAX
#define mod 1000000007
using namespace std;

string func(ll num)
{
	string wrd = "";
	while(num>0)
	{
		ll dig = num%10;
		wrd = (char)(dig + '0') + wrd;
		num=num/10;
	}
	return wrd;
}

ll t, n;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		cin>>n;
		string num = func(n);
		ll len = num.length(), ind = -1;
		F(i,1,len-1)
		{
			if(num[i]<num[i-1])
			{
				ind = i;
				RF(j,i-2,0)
				{
					if(num[j]!=num[i-1])
						break;
					num[j] = (char)(num[j]-1);
					ind=j+1;
				}
				num[i-1] = (char)(num[i-1]-1);
				break;
			}
		}
		cout<<"Case #"<<cas<<": ";
		if(ind==-1)
			cout<<num<<endl;
		else
		{
			ll i=0;
			while(num[i]=='0' && i<ind)
				i++;
			for(;i<len;i++)
			{
				if(i>=ind)
					cout<<"9";
				else
					cout<<num[i];
			}
			cout<<endl;
		}

	}    
	return 0;
}