#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

int n,m;
int a[6];
int c[3];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cout<<fixed<<setprecision(10);
    
    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {
    	string r,s;
    	bool f=1;
		
		cin>>n;
		for (int i=0; i<6; i++)
			cin>>a[i];

		pair<int,char> p[3];
		p[0] = {a[0],'R'};
		p[1] = {a[2],'Y'};
		p[2] = {a[4],'B'};
		
		sort(p,p+3);
		reverse(p,p+3);

		for (int i=0; i<p[0].first; i++)
			s+=p[0].second;
		for (int i=0; i<p[1].first; i++)
			s+=p[1].second;
		for (int i=0; i<p[2].first; i++)
			s+=p[2].second;
		r=s;

		int pp = 0;
		for (int i=0; i+i<n; i++)
			r[i+i] = s[pp], pp++;
		for (int i=0; i+i+1<n; i++)
			r[i+i+1] = s[pp], pp++;
			
		for (int i=0; i<n; i++)
			f &= (r[i] != r[(i+1)%n]);
    	
    	cout<<"Case #"<<testi<<": ";
    	if (!f) cout<<"IMPOSSIBLE", cerr<<r<<'\n';
    	else cout<<r;
    	cout<<'\n';
    	
    }
    
    return 0;
}
