using namespace std;
#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define ull unsigned long long 
#define FF first
#define SS second
#define MOD 1000000007

typedef vector<ll> vll;


int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
	ll n;
	cin>>n;
	ll ans = 0;
	ll factor =1;
	vector<int> v;	
	while(n>0)
	{	
		v.pb(n%10);
		n/=10;
	}
	reverse(v.begin(),v.end());
	int q = 100;
	while(q--){
	for(int i=0;i<v.size()-1;i++)
	{
		if(v[i]>v[i+1])
		{
			v[i]--;
			for(int j=i+1;j<v.size();j++)
			{
				v[j]=9;
			}
			break;
		}
	}

}
	factor = 1;
	for(int i=v.size()-1;i>=0;i--)
	{
		ans+=factor*v[i];
		factor*=10;
	}
	cout<<"Case #"<<tt<<": "<<ans<<endl;


}
}








