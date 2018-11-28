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
#define MAXN 100
char M[MAXN][MAXN];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;

    for(int tt=1;tt<=t;tt++)
    {
        int n,m;
        sc2(n,m);
        for(int i=0;i<n;i++)cin>>M[i];
        for(int i=0;i<n;i++)
        {
            int first=-1;
            for(int j=0;j<m;j++)
            {
                if(M[i][j]!='?')
                {
                    first=j;
                    break;
                }
            }
            if(first>-1)
            {
                for(int j=0;j<first;j++)M[i][j]=M[i][first];
                for(int j=0;j<m;j++)if(M[i][j]=='?')M[i][j]=M[i][j-1];
            }
        }
        for(int i=n-1;i>=0;i--)
        {
            for(int j=0;j<m;j++)
            {
                if(M[i][j]=='?')
                {
                    if(i+1<n)
                    {
                        M[i][j]=M[i+1][j];
                    }
                    else
                    {
                        M[i][j]=M[i-1][j];
                    }
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(M[i][j]=='?')
                {
                    if(i-1>=0)
                    {
                        M[i][j]=M[i-1][j];
                    }
                }
            }
        }
        cout<<"Case #"<<tt<<":"<<endl;
        for(int i=0;i<n;i++)cout<<M[i]<<endl;
    }
    return 0;
}
