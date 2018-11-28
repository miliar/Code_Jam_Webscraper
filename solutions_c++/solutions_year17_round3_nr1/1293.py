
#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
const double PI = 3.141592653589793238462643383279502884; 
using namespace std;

typedef vector<int> vi;
typedef long long int lli;
typedef vector<lli> vli;
typedef pair<int, int> pii;

void foo()
{
    int n,k;
    cin>>n>>k;

    vector<pair<double,double> > v;
    int i;double r,h;

    for(i=0;i<n;i++)
    {
        cin>>r>>h;
        v.pb(mp(r,h));
    }

    sort(v.rbegin(), v.rend());

    

    vector<double> csa(n);
    for(i=0;i<n;i++)
    {
        r = v[i].first;
        h = v[i].second;
        csa[i] = 2*r*h;
    }

    int j;
    double tmp;
    double ans = 0;
    vector<double> T;
    for(i=0;i<n;i++)
    {
        tmp = csa[i];
        tmp += v[i].first * v[i].first;

        if((i+k-1) >= n)
        {
          break;
        }

        for(j=i+1;j<n;j++)
        {
            T.pb(csa[j]);
        }
        sort(T.rbegin(), T.rend());
        for(j=0;j<k-1;j++)
        {
            tmp += T[j];
        }
        T.clear();
        if(tmp>ans)
            ans = tmp;


    }

    double area = ans * PI;
    cout<<setprecision(30)<<area<<endl;


   
}


int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        foo();
    }

}
