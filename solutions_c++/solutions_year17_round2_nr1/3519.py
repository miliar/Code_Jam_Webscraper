//Sinha Saab
//NARUTO Fan



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 1e18
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

struct data
{
	double p,s;
};

double d;
ll n;
data a[1005];

bool way(data x,data y)
{
	if(x.p!=y.p)
		return x.p<y.p;
	return x.s<y.s;
}

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    ll tc,t,i;
    double x,ans;
    cin>>t;
    for(tc=1;tc<=t;tc++)
    {
    	cin>>d>>n;
    	//if(tc==51)
		//    cout<<d<<" "<<n<<"\n";
    	for(i=0;i<n;i++)
    	{
    		cin>>a[i].p>>a[i].s;
    	//	if(tc==51)
    	//		cout<<a[i].p<<" "<<a[i].s<<"\n";
    	}
    	//continue;
    	sort(a,a+n,way);
    	ans=maxVal;
    	for(i=(n-1);i>=0;i--)
    	{
    		if(a[i].p>=d)
    			continue;
    		if(i==(n-1))
    		{
    			x=(d-a[i].p)/a[i].s;
    			ans=min(ans,d/x);
    		}
    		else
    		{
    			if(true||a[i].s<=a[i+1].s)
    			{
    				x=(d-a[i].p)/a[i].s;
	    			ans=min(ans,d/x);
    			}
    		}
    	}
    	printf("Case #%lld: %0.6lf\n",tc,ans);
    }
    return 0;
}