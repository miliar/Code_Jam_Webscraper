//Bismillahir Rahmanir Rahim
#include<bits/stdc++.h>
using namespace std;
#define pb      push_back
#define _       ios_base::sync_with_stdio(false);
#define ct      cin.tie(NULL);
#define ll      long long
#define eps     1e-10
#define ms(n,i) memset(n,i,sizeof n)
#define pi      2*acos(0)
#define inf     1<<30
#define fr(i,n) for(i=0;i<n;i++)
#define fr1(i,n)for(i=1;i<=n;i++)
#define abs(x)  ((x<0)?-(x):x)
#define MAX 30005
#define sp(i)      cout<<fixed<<setprecision(i)
//STL
typedef      vector<int> vi;
typedef      vector<ll> vl;
typedef      pair<int,int>ii;
#define mp      make_pair
#define ft      first
#define sd      second
#define IT      iterator
#define pr(c,x) ((c).find(x)!=(c).end())
#define sz(a) int((a).size())
#define all(c)  c.begin(), c.end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin();i!=c.end();i++)
#define vpresent(c,x) (find(all(c),x)!=(c).end())
#define eb      emplace_back
//


//input output
#define sf      scanf
#define pf      printf

#define sf1(a)  sf("%d",&a)
#define sf2(a,b)  sf("%d%d",&a,&b)
#define sf3(a,b,c)   sf("%d%d%d",&a,&b,&c)

#define nl cout<<"\n"
//eof

//seg tree
#define lc      (s+e)>>1
#define rc      (lc)+1
#define Ln      n<<1
#define Rn      (Ln)|1
//end of seg tree
ll M=100000007;
inline ll Pow(ll g,ll h)
{
    ll z=1;
    while(h--)
        z*=g;
    return z;
}

inline ll bigmod(ll b,ll p)
{
    ll res=1;
    for(;p;p>>=1,b=b*b%M)if(p&1)res=res*b%M;
    return res;
}
inline ll InverseM(ll n)
{
    return bigmod(n,M-2);
}




//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

string a;
int n;
ll dp[10][19][2];
bool vis[10][19][2];

ll fun(int pr,int ps,int ck)
{
    if(ps>=n)
        return 0;
    if(vis[pr][ps][ck])return dp[pr][ps][ck];
    vis[pr][ps][ck]=1;
    ll an=0,wz;int i,b;
    if(!ck)
    {
        for(i=ps;i<n;i++)
            an=(an*10)+9;
    }
    else
        {

            b=a[ps]-'0';

            if(b<pr)return -2000000000000000000;
            an=fun(b,ps+1,1)+(Pow(10,n-1-ps))*b;
            if(b>pr)
            {
                wz=fun(b-1,ps+1,0)+Pow(10,n-1-ps)*(b-1);
                an=max(an,wz);
            }

        }
    return dp[pr][ps][ck]=an;

}
int main()
{
       // freopen("D:\\Coding\\B-large.in","r",stdin);
     //   freopen("D:\\Coding\\out.txt","w",stdout);

    int t,z,i,w;
    ll an,wz,zz,kk;
    cin>>t;
    fr1(z,t)
    {
        cin>>a;
        cout<<"Case #"<<z<<": ";
        n=a.length();ms(vis,0);
        an=fun(0,0,1);
        cout<<an;nl;
    }

    return 0;
}

