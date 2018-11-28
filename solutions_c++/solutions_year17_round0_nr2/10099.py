#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

string leia(ll x)
{
	string resp="";
	while(x)
	{
		resp += ((x%10)+'0');
		x/=10;
	}
	reverse(resp.begin(), resp.end());
	return resp;
}

bool ok(string a)
{
	bool chave=true;
	if(a.size()==1) return true;
	for(int i=0; i<a.size()-1; i++)
	{
		if(a[i]>a[i+1]) chave=false;
	}
	return chave;
}

ll transform(string a)
{
	bool foi=false;
	for(int i=0; i<a.size()-1;i++)
	{
		if(foi)
		{
			a[i]='9';
		}
		if(a[i]>=a[i+1] && !foi)
		{
			a[i]=a[i]-1;
			foi=true;
			for(int j=i+1; j<a.size(); j++)
			{
				a[j]='9';
			}
		}
	}
	ll resp = 0;
	for(int i=0; i<a.size(); i++)
	{
		resp*=10;
		resp+=(a[i]-'0');
	}
	return resp;
}

int main() {
	// freopen("b.in", "r", stdin);
	// freopen("b2.txt", "w", stdout);
	ll n;
	int caso=1;
	scanf("%lld", &n);
	for(int j=0; j<n; j++){
		ll i;
		scanf("%lld", &i);
		string a = leia(i);
		if(!ok(a)) i = transform(a);
		printf("Case #%d: %lld\n",caso++, i);
	}
	return 0;
}
