#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector< pair<ll,ll> > vpii;
 
#define boost std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define all(x) (x).rbegin() , (x).rend()
#define F first
#define S second
#define pi 3.14159265358979323846
 
typedef struct heheheh
{
	ll r,h,idx;
}heheheh;
int main()
{
    boost;
    int t,tcase=1;
    cin>>t;
    while(t--)
    {
        ll n,m,i,j,k;
        cin>>n>>k;
        heheheh a[n];
        FOR(i,0,n) 
        cin>>a[i].r>>a[i].h;
        FOR(i,0,n) 
        a[i].idx=i;
        vpii barr(n);
        FOR(i,0,n)
        {
        	barr[i].F = a[i].r*a[i].h;
        	barr[i].S = i;
        }
        sort(barr.begin(), barr.end());
        reverse(barr.begin(), barr.end());
        double ans=0.0;
        FOR(i,0,n)
        {
        	double sum = 2*pi*a[i].r*a[i].h + pi*a[i].r*a[i].r;
        	int yo=1;
        	FOR(j,0,n)
        	{
        		if(yo==k) 
        			break;
        		if(barr[j].S==i) 
        			continue;
        		double here = 2*pi*barr[j].F;
        		sum+=here;
        		yo++;
        	}
        	ans=max(ans,sum);
        }
        printf("Case #%d: %.10f\n",tcase,ans); 
        tcase++;
    }
    return 0;
}     