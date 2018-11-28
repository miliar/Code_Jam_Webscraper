/*input
4
132
1000
7
111111111111111110
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
string convert_to_string(ll x)
{
	string temp = "";
	while(x > 0)
	{
		ll d = x%10;
		temp = (char)(d+48) + temp;
		x /= 10;
	}
	return temp;
}
bool check(string s)
{
	ll n = s.length();
	F(i,0,n-2)
	{
		if(s[i] > s[i+1])
			return 0;
	}
	return 1;
}
ll ans[100000005]; // for brute force
void brute()
{
	F(i,1,100000000)
	{
		string s = convert_to_string(i);
		if(check(s))
			ans[i] = i;
		else
			ans[i] = ans[i-1];
	}
}
int main() 
{
	std::ios::sync_with_stdio(false);
	//brute();
	//F(i,1,100)
	//	cout<<ans[i]<<" ";
	//cout<<endl;*/
	freopen("is1.txt","r",stdin);
	freopen("os1.txt","w",stdout);
	//cout<<ans[1023456]<<endl;
	ll tc=1;
	ll t;
	cin>>t;
	//S(t);
	while(t--)
	{
		cout<<"Case #"<<tc++<<": ";
		ll n;
		cin>>n;
		string s = convert_to_string(n);
		ll m = s.length();
		while(1)
		{
			//cout<<s<<endl;
			if(check(s))
				break;
			bool flag = 0;
			F(i,0,m-2)
			{
				if(s[i] > s[i+1])
				{
					s[i+1] = '9';
					s[i]--;
					flag = 1;
					//cout<<s<<endl;
					F(j,i+2,m-1)
						s[j] = '9';
				}
				if(flag)
					break;
			}
		}
		ll i=0;
		while(s[i]=='0')
			i++;
		F(j,i,m-1)
			cout<<s[j];
		//cout<<" "<<ans[n];
		cout<<endl;
	}
	return 0;
}