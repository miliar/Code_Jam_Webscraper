#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

const int mod = 1e9+7;
const ld pi = 3.14159265358979;

int n,k;
pair<ll,ll> a[1000];
ld res;

int main()
{
   	ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cout<<fixed<<setprecision(10);
    
    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {
    	res=0;
    	cin>>n>>k;
    	for (int i=0; i<n; i++)
    		cin>>a[i].first>>a[i].second;
    		
    	
    	sort(a,a+n,
    		[](pair<ll,ll> x, pair<ll,ll> y){ return (x.first*x.second > y.first*y.second);});
    		
    	for (int i=0; i<n; i++)
    	{
    		ld b = 0;
    		b += a[i].first*a[i].first;
    		int good = 1;
    		b+=2*a[i].first*a[i].second;
    		for (int j=0; good<k && j<n; j++)
    			if (a[j].first<=a[i].first && j!=i) b+=2*a[j].first*a[j].second,good++;
    		if (good<k) continue;
    		res = max(res,b);
    	}
    	
    
    	cout<<"Case #"<<testi<<": ";
    	cout<<res*pi;
    	cout<<'\n';
    	
    	cerr<<"Case #"<<testi<<": ";
    	cerr<<res;
    	cerr<<'\n';
    }
    return 0;
}
