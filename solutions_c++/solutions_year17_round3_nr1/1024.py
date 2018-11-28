#include<bits/stdc++.h>
#include <ext/numeric>
using namespace std;
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define scd(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf%lf",&a,&b)
#define scd3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define scd4(a,b,c,d) scanf("%lf%lf%lf%lf",&a,&b,&c,&d)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ALL(x) x.begin(), x.end()
#define BUFF ios::sync_with_stdio(false);
#define endl "\n"
#define power(a,x) __gnu_cxx::power(a, x)
#define forN(i,n) for(int i=0;i<n;i++)
#define eps 1e-5
#define INF INT_MAX
#define INFLL LLONG_MAX
#define gcd(a,b) __gcd(a,b)
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vector<int> >vvi;
typedef pair<double,double> pdd;
const double PI = 3.141592653589793;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n,k;
        cin>>n>>k;
        vector<pdd> v;
        for(int i=0;i<n;i++)
        {
            v.pb(mp(0,0));
            cin>>v[i].fi>>v[i].se;
        }
        sort(v.begin(),v.end());
        reverse(v.begin(),v.end());
        double best=0;
        for(int i=0;i<n;i++)
        {
            double curr=PI*v[i].fi*v[i].fi + 2*PI*v[i].se*v[i].fi;
            vector<double> aux;
            for(int j=i+1;j<n;j++)
            {
                aux.pb(2*PI*v[j].se*v[j].fi);
            }
            if(aux.size()>0)
            {
                 sort(aux.begin(),aux.end());
                reverse(aux.begin(),aux.end());
                for(int j=0;j<k-1;j++)
                {
                    curr+=aux[j];
                }
            }
            best=max(curr,best);
        }
        std::cout << std::fixed;
        std::cout << std::setprecision(9);
        cout<<"Case #"<<tt<<": "<<best<<endl;
    }
    return 0;
}
