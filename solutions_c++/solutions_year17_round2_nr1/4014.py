#include <bits/stdc++.h>

#define INF                         (long long)1e15
#define EPS                         1e-9
#define MOD   1000000007
#define checkbit(n,b)                ( (n >> b) & 1)
#define min3(a,b,c)                  ( a<b?(a<c?a:c):(b<c?b:c) )
#define max3(a,b,c)                  ( a>b?(a>c?a:c):(b>c?b:c) )
//dataTypes
#define ll long long int
#define ld long double
#define vi vector<int>
#define vll vector<long long int>
#define vp vector< pair<long long, long long > >
//STLFunctions
#define pb(x) push_back(x)
#define maxElement(v) *max_element(v.begin(), v.end())
#define minElement(v) *min_element(v.begin(), v.end())
#define SORT(v) sort(v.begin(),v.end())
#define mp(x,y) make_pair(x,y)
//loops
#define f(i,a,n) for( i=a; i<n; i++)

using namespace std;



int main() {
   int it,t;
   cin>>t;
   for(it=1; it<=t; it++)
   {

   	cout<<"Case #"<<it<<": ";
    ll n, i, j;
    double d;
    cin>>d>>n;
    vector< pair<double,double> > v(n);

    f(i,0,n) 
    {
    	double x, y;
    	cin>>x>>y;
    	v[i]=mp(x,y);
    }

    sort(v.rbegin(), v.rend());

    double dist=v[0].first, sp=v[0].second, tm0=0;
    for(i=1; i<n; i++)
    {

    	double ds=abs(dist-v[i].first);
    	double s=abs(sp-v[i].second);

    	double tm=ds/s;

    	double pos = v[i].first + tm*v[i].second;

    	if(pos<d && v[i].second > sp)
    	{
    	    dist = pos;
    		sp=min(sp,v[0].second);
    		tm0=tm0+tm;
    		
    	}

    	else
    	{
    	    
    	    dist=v[i].first;
    		sp=v[i].second;
    		
    	}
        //cout<<dist<<" "<<sp<<endl;



    }

    double tme=(d-dist)/sp;
    
    tme= tme+tm0;
    double ans=d/tme;

    printf("%f\n", ans);



   }  


   return 0;
}