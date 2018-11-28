/*input
5
4 2
5 2
6 2
1000 1000
1000 1
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

ll t, n, k;
ll Max, Min;

string getBinary(ll num)
{
	string tmp="";
	while(num>0)
	{
		tmp = tmp + (char)(num%2 + '0');
		num/=2;
	}
	return tmp;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out_large.txt", "w", stdout);
    cin>>t;
    F(cas,1,t)
    {
    	cin>>n>>k;
    	string tmp = getBinary(k);
    	ll sz = tmp.length();
    	F(i,0,sz-2)
    	{
    		if(tmp[i]=='1')
    		{
    			if(n%2==0)
    				n = n/2 - 1;
    			else
    				n = n/2;
    		}
    		else
    			n = n/2;
    	}
   		Max = n/2;
    	if(n%2 == 0)
    		Min = n/2 - 1;
    	else
    		Min = n/2;
 		cout<<"Case #"<<cas<<": ";
    	cout<<Max<<" "<<Min<<endl;
    }    
	return 0;
}