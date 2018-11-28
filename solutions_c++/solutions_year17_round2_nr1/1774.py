#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;

const ll INF=1e18;

const int mod=1000000007;

typedef struct horses
{
    ll k,s;
} horses;

int main()
{
    ll t,n,m,i,j,k,l,x,y;
    FILE *f1,*f2;

    f1=fopen("input.txt","r");
    f2=fopen("output.txt","w");
    fscanf (f1,"%lld",&t);
    for (ll q=1;q<=t;++q)
    {
        fscanf (f1,"%lld %lld",&m,&n);
        horses arr[n];
        for (i=0;i<n;++i)
            fscanf (f1,"%lld %lld",&arr[i].k,&arr[i].s);
        sort (arr,arr+n,[](horses x, horses y)
        {
            if (x.k==y.k)
                return x.s<y.s;
            return x.k<y.k;
        });
        double time[n],s=0.0;
        for (i=n-1;i>=0;--i)
        {
            time[i]=(1.0*(m-arr[i].k))/arr[i].s;
            s=max(s,time[i]);
        }
        fprintf (f2,"Case #%lld: %0.8lf\n",q,m/s);
    }
    fclose(f1);
    fclose(f2);

	return 0;
}
