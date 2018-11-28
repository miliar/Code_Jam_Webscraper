#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

ld n,d;
ld k[1000],s[1000];

bool check(ld x)
{
	bool f=1;
	for (int i=0; i<n; i++)
		f &= (x*d <= x*k[i] + s[i]*d);
	return f;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cout<<fixed<<setprecision(10);
    
    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {
    	cin>>d>>n;
    	
    	for (int i=0; i<n; i++)
    		cin>>k[i]>>s[i];

		ld l=1e16;
		for (int i=0; i<n; i++)
			l = min(l, d*s[i]/(d-k[i]));    
    
    	cout<<"Case #"<<testi<<": ";
    	cout<<l;
    	cout<<'\n';
    	
    	cerr<<"Case #"<<testi<<": ";
    	cerr<<l;
    	cerr<<'\n';
    }
    
    return 0;
}
