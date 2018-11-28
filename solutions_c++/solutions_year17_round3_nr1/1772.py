#include <bits/stdc++.h>
using namespace std;

#define min(a,b) ((a<b) ? (a) : (b))
#define max(a,b) ((a>b) ? (a) : (b))
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORL(i,n) for(long long i=0;i<n;i++)
#define MOD 1000000007
#define PI 3.141592653589793238
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>

bool fun(const pll &p1 , const pll &p2)
{
	if(p1.first==p2.first)
		return p1.second>p2.second;
	return p1.first>p2.first;
}

bool fun2(const pll &p1 , const pll &p2)
{

	if ((p1.first*p1.second) == (p2.first*p2.second))
		return p1.first>p2.first;

	return ((p1.first*p1.second) > (p2.first*p2.second));
}

int main()
{
    fastio
    freopen("input_1.txt", "r", stdin);
    freopen("output_1.txt", "w", stdout);
    vector<pll > v;
    int test;
   	double ans=0.0;
   

    cin>>test;
    int k,n,i;
    ll h,r;
    for(int t=1;t<=test;t++)
    {
    	
        //ans=0.0;
    	cin>>n>>k;
    	
    	v.clear();
    	FOR(i,n)
    	{
    		cin>>r>>h;

    		v.pb(mp(r,h));
    	}
    	sort(v.begin(),v.end(),fun);
    	//ans=PI*(double)(v[0].first*v[0].first);
    	ans=0.0;
    	double ansm=0.0;
    	int j;
    	//ans+=2.0*PI*(double)(v[0].first*v[0].second);
    	//v.erase(v.begin());

    	//sort(v.begin(),v.end(),fun2);
    	//k--;


    	FOR(j,(n-k+1))
    	{
    		ans=0.0;
    		vector<pll > v2=v;
    		v2.erase(v2.begin(),v2.begin()+j+1);
    		sort(v2.begin(),v2.end(),fun2);
    		ans=(PI*((double)v[j].first * (v[j].first + 2*v[j].second)));
    		FOR(i,(k-1))
	    	{
	    		ans+=(2.0*PI*((double)v2[i].first * v2[i].second));
	    		
	    	}
	    	if(ans>ansm)
	    		ansm=ans;
    	}
    	
    	
    	printf("Case #%d: %0.9lf\n",t,ansm);

        //cout<<"Case #"<<t<<": "<<ans<<endl;







    }
    return 0;
}

