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
int v[10];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        vii aux;
        vi resp[1010];
        vi out;
        for(int i=0;i<1010;i++)resp[i].clear();
        int mx=0;
        int n;
        cin>>n;
        for(int i=0;i<6;i++)
        {
            sc(v[i]);
            aux.pb(mp(-v[i],i));
            if(v[i]>v[mx])mx=i;
        }
        sort(aux.begin(),aux.end());
        int pos=0;
        for(int i=0;i<aux.size();i++)
        {
            int size=-aux[i].fi;
            int curr=aux[i].se;
            for(int j=0;j<size;j++)
            {
                resp[pos].pb(curr);
                pos++;
                pos%=v[mx];
            }
        }
        cout<<"Case #"<<tt<<": ";
        for(int i=0;i<v[mx];i++)
        {
            for(int j=0;j<resp[i].size();j++)
            {
                out.pb(resp[i][j]);

            }
        }
        bool valid=true;
        if(out[n-1]==out[0])valid=false;
        for(int i=0;i<n-1;i++)
        {
            if(out[i]==out[i+1])valid=false;
        }
        if(valid)
        {
             for(int i=0;i<n;i++)
            {
                switch(out[i])
                {
                    case 0: cout<<"R"; break;
                    case 1: cout<<"O"; break;
                    case 2: cout<<"Y"; break;
                    case 3: cout<<"G"; break;
                    case 4: cout<<"B"; break;
                    case 5: cout<<"V"; break;
                }
            }
            cout<<endl;
        }
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
