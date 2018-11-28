#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<b;++i)
#define mod 1000000007
#define rev(i,a,b) for(i=a;i>b;--i)
#define ll long long int
#define si(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sstr(x) scanf("%s",x)
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vll vector<ll>
#define mapii map<int, int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ins(x) insert(x)
#define mulmap multimap<int, int>
#define itr ::iterator
ll pow(ll, ll);
ll max(ll, ll);
ll min(ll, ll);
using namespace std;
int check(string s)
{
	int i,len,j;
	len = s.length();
	j=0;
	while(s[j]=='0')
		j++;
	rep(i,j,len-1)
	{
		if(s[i]>s[i+1])
			return i;
	}
	return len;
}
int main()
{
	int t,num,len,rv,i,j;
	string s;
	cin>>t;
	num=1;
	while(t--)
	{
		cin>>s;
		len=s.length();
		while(1)
		{
			rv = check(s);
			if(rv>=len-1)
				break;
			else
			{
				s[rv] = s[rv]-1;
				rep(i,rv+1,len)
					s[i]='9';
			}
		}

		cout<<"Case #"<<num<<": ";
		i=0;
		while(s[i]=='0')
			i++;
		rep(j,i,len)
			cout<<s[j];
		cout<<endl;
		num++;
	}
	return 0;
}
ll max(ll a, ll b)
{
	if(a>b)
		return a;
	else
		return b;
}
ll min(ll a, ll b)
{
	if(a>b)
		return b;
	else
		return a;
}
ll pow(ll a, ll b)
{
	ll ans=1;
	while(b)
	{
		if(b&1)
		{
			ans=ans*a;
		}
		a=a*a;
		b=b>>1;
	}
	return ans;
}
