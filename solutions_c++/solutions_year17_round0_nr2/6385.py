/*
Author    : MANISH RATHI
Institute : NIT KURUKSHETRA

*******************************
Don't Stop when you are tired  *
Stop When you are Done         *
******************************* 
*/

#include<bits/stdc++.h>
using namespace std;
#define MAX 1000007
#define mode 1000000007
#define ll long long
#define ii pair<int,int>
#define vi vector<int>
#define vii vector< ii >
#define vvi vector< vi >
#define vvii vector< vii >
#define mp make_pair
#define pb push_back
#define read(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define read2(x,y) scanf("%d%d",&x,&y);
#define print2(x,y) printf("%d %d\n",x,y);
#define read_s(x) scanf("%s",x);
#define print_s(x) printf("%s",x);
#define rep(i,a,b) for(i=a;i<=b;i++)
ll superPow(ll a,ll b)
{
    if(b==0)
        return 1;
    if(b==1)
        return a;
    ll temp= superPow(a,b/2);
    if(b&1)// odd
        return (temp*temp*a);
    else
        return (temp*temp);
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("tidyLarge.txt", "w", stdout);
    int t,h;
    cin>>t;
    for(h=1;h<=t;h++)
    {
    	ll n;
    	cin>>n;
    	vector<ll> v;
    	ll temp=n;
    	while(temp)
    	{
    		v.pb(temp%10);
    		temp/=10;
    	}
    	int len= v.size();
    	int idx,i;
    	for(i=len-1;i>0;i--)
    	{
    		if(v[i]>v[i-1])
    		{
    			idx=i;
    			break;
    		}
    	}
    	ll ans;
    	if(i==0)// perfect tidy no
    	{
    		ans=n;
    		// ans=0;
    	}
    	else
    	{
    		for(i=idx;i<len-1;i++)
    		{
    			v[i]=v[i]-1;
    			if(v[i+1]<=v[i])
    				break;
    		}
    		if(i==len-1)
    			v[i]=v[i]-1;
    		idx=i-1;
    		for(i=idx;i>=0;i--)
    			v[i]=9;
    		ll num=0;
    		for(i=0;i<len;i++)
    		{
    			num=v[i]*superPow(10,i)+num;
    		}
    		ans=num;
    	}
    	cout<<"Case #"<<h<<": "<<ans<<endl;
    }
    return 0;
}
