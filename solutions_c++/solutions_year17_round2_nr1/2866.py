/*   ayushkmr                 **
**   Ayush Kumar			  **
**   IIT (ISM) Dhanbad        */
#include<bits/stdc++.h>
#define gc getchar
#define pb(x) push_back(x)
#define eb(x) emplace_back(x)
#define mp(x,y) make_pair((x),(y))
#define sz size()
#define ff first
#define ss second
#define all(x) (x).begin(),(x).end()
#define mset(m,v) memset(m,v,sizeof(m))
#define Abs(a,b) ((a) < (b) ? (b)-(a) : (a)-(b))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define remax(a,b) (a)=max((a),(b));
#define remin(a,b) (a)=min((a),(b));
#define nu 500005
#define pnu 10
#define MOD 1000000007
#define MAX 1000000000
#define MAXL 1000000000000000000LL
#define nmod(a,b) ((a%b)+b)%b
 
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef stack<int> sti;
typedef queue<int> qi;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<vi> vvi;
typedef vector<ii> vii;

inline int in()
{
    int NR=0;
    register char c=gc();
    while( c < 48 || c > 57 ){c=gc();}
    while(c>47 && c< 58)
    {
		NR = (NR << 3) + (NR << 1) + (c - 48);
		c=gc();
    }
    return NR;
}
int main()
{
	//ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    ll tt=in(),d,n,i,zz;
    double dd;
    double t,mt,x,y,an;
    for(zz=1;zz<=tt;zz++)
        {
        d=in();
        dd=d;
        i=n=in();
        mt=0;
        while(i--)
            {
            cin>>x>>y;
            t=(d-x)/y;
            remax(mt,t);
        }
        an=dd/mt;
        cout<<"Case #"<<zz<<": ";
        printf("%.6lf\n",an);
    }
	return 0;
}
