#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define mod 1000000007
#define vec vector<long long>
#define arl(n) array<long long,n>
#define ard(n) array<double,n>
#define sc(n) scanf("%lld",&n)
#define prn(n) printf("%lf\n",n)
#define prs(n) printf("%lld ",n)
#define pr() printf("\n")
#define pb push_back
#define mp make_pair

int main()
{   long long t,i=0;
    cin>>t;
    for(;i<t;)
    {   cout<<"Case #"<<i+1<<": ";
        long long n,j=0;
        double as,max=0.0;
        cin>>as>>n;
        for(;j<n;j++)
        {   double x,y,q;
            cin>>x>>y;
            q=(as-x)/y;
            (max<q)?max=q:max=max;
        }
        as=as/max;
        prn(as);
        i=i+1;
    }
    return 0;
}