#include <bits/stdc++.h>
using namespace std;

#define min(a,b) ((a<b) ? (a) : (b))
#define max(a,b) ((a>b) ? (a) : (b))
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORL(i,n) for(long long i=0;i<n;i++)
#define MOD 1000000007
#define PI 3.141592653589
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define mp make_pair
#define pb push_back

bool fun(const pair<ll,ll> &p1 , const pair<ll,ll> &p2)
{
	return p1.first<p2.first;
}
int main()
{
    fastio
    freopen("input_1.txt", "r", stdin);
    freopen("output_1.txt", "w", stdout);
    vector<pair<ll,ll> > v;
    int test;
   	double ans=0.0,time;
   	int i;

    cin>>test;
    ll n,d,m,k,s;
    for(int t=1;t<=test;t++)
    {
    	ans=0.0;
    	time=0.0;
    	v.clear();
    	cin>>d>>n;

        FOR(i,n)
        {
        	cin>>k>>s;
        	v.pb(mp(k,s));
        	time = max(time , ((double)(d-k))/((double)s));
        }
        //sort(v.begin(), v.end(),fun);

        // s=v[0].second;
        // for(i=1;i<n;i++)
        // {

        // 	time+= ((double)(v[i].first - v[i-1].first))/((double)s);
        // 	s=min(s,v[i].second);
        // }
        // time+= ((double)(d - v[i-1].first))/((double)s);
        ans=((double)d)/time;



        cout<<setprecision(6)<<fixed;
        cout<<"Case #"<<t<<": "<<ans<<endl;


    }
    return 0;
}

