/***************************************
    codeforces = topcoder = sahedsohel
    IIT,Jahangirnagar University(42)
****************************************/
#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define inf (INT_MAX/10)
#define linf (LLONG_MAX/10LL)
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)
#define mem(a) memset(a,0,sizeof(a))
#define memn(a) memset(a,-1,sizeof(a))
#define pb push_back
#define aov(a) a.begin(),a.end()
#define mpr make_pair
#define PI (2.0*acos(0.0)) //#define PI acos(-1.0)
#define xx first
#define yy second
#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])
#define pll pair< ll , ll >
#define pii pair< int , int >
#define pcs(a) printf("Case %d: ", a)
#define nl puts("")
#define endl '\n'
#define dbg(x) cout<<#x<<" : "<<x<<endl

template <class T> inline T bigmod(T p,T e,T M){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p) % M;p = (p * p) % M;}return (T)ret;}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}   // M is prime}
template <class T> inline T bpow(T p,T e){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p);p = (p * p);}return (T)ret;}

int toInt(string s){int sm;stringstream ss(s);ss>>sm;return sm;}
int toLlint(string s){long long int sm;stringstream ss(s);ss>>sm;return sm;}


///int mnth[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int dx[]={-1,+1,0,1,0,-1}; // Hexagonal Direction   **
///int dy[]={-1,+1,1,0,-1,0}; //                       *#*
///                                                     **
///const double eps=1e-9;
///int dx[]={0,1,0,-1};int dy[]={1,0,-1,0}; //4 Direction

/*****************************************************************/
/// ////////////////////   GET SET GO    ////////////////////// ///
/*****************************************************************/


#define intx(i,j,k,l) ((a[i]*b[j]-b[i]*a[j])*(a[k]-a[l])-(a[i]-a[j])*(a[k]*b[l]-b[k]*a[l]))/((a[i]-a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]-a[l]))
#define inty(i,j,k,l) ((a[i]*b[j]-b[i]*a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]*b[l]-b[k]*a[l]))/((a[i]-a[j])*(b[k]-b[l])-(b[i]-b[j])*(a[k]-a[l]))
#define dst(u,v,x,y) sqrt((x*1.0-u*1.0)*(x*1.0-u*1.0)+(y*1.0-v*1.0)*(y*1.0-v*1.0))
#define area(p1,p2,p3) (p1.xx*p2.yy+p2.xx*p3.yy+p3.xx*p1.yy-p1.yy*p2.xx-p2.yy*p3.xx-p3.yy*p1.xx)
#define dstt(u,v,x,y) ((ll)(x-u)*(ll)(x-u)+(ll)(y-v)*(ll)(y-v))

int ts,kk=1;

#define sqr(x) ((x)*(x))

/// 	   0123456789ABCDEF
#define M  1000005
#define MD 1000000007LL
#define MX 1000005
#define mid ((s+e)>>1)
#define lft ((i<<1)+1)
#define rgt (lft+1)

int n,m;
char gr[25][28];
int cs[25][28];
int vs[25][25][25][25];
int ok[25][25][25][25];
bool p[25][25][25][25];

#define get(d,l,u,r) (cs[u][r]-((l>0)?cs[u][l-1]:0)-((d>0)?cs[d-1][r]:0)+((d>0&&l>0)?cs[d-1][l-1]:0))

bool dp(int d,int l,int u,int r)
{
	if(l>r||d>u)return 1;
	if(get(d,l,u,r)==0)return 0;
	if(get(d,l,u,r)==1)return 1;
	
	bool &pr=p[d][l][u][r];
	if(vs[d][l][u][r]==kk)return pr;
	vs[d][l][u][r]=kk;
	
	pr=0;
	for(int i=d;i<u;i++)
	{
		if( dp(d,l,i,r)&&dp(i+1,l,u,r) )
		{
			ok[d][l][u][r]=i+1;
			return pr=1;
		}
	}
	for(int i=l;i<r;i++)
	{
		if( dp(d,l,u,i)&&dp(d,i+1,u,r) )
		{
			ok[d][l][u][r]=-(i+1);
			return pr=1;
		}
	}
	return pr=0;
}

void prnt(int d,int l,int u,int r)
{
	if(l>r||d>u)return ;
	if(get(d,l,u,r)==1)
	{
		int i,j;
		char ch='?';
		for(i=d;i<=u;i++)
		{
			for(j=l;j<=r;j++)
			if(gr[i][j]!='?')
			{
				ch=gr[i][j];
				break;
			}
			if(j<=r)break;
		}
		//if(ch=='?')cerr<<d<<" "<<l<<" : "<<u<<" "<<r<<endl;
		fl(d,i,u+1)
		fl(l,j,r+1)
		gr[i][j]=ch;
		
		return ;
	}
	
	if(ok[d][l][u][r]>=0)
	{
		int i=ok[d][l][u][r]-1;
		prnt(d,l,i,r);
		prnt(i+1,l,u,r);
	}
	else
	{
		int i=-ok[d][l][u][r]-1;
		prnt(d,l,u,i);
		prnt(d,i+1,u,r);
	}
	return ;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,i,j,k,l;
	
	sc(ts);
	while(ts--)
	{
		sc2(n,m);
		f(i,n)
		{
			scanf(" %s",gr[i]);
			f(j,m)
			{
				cs[i][j]=(gr[i][j]!='?');
				if(i)cs[i][j]+=cs[i-1][j];
				if(j)cs[i][j]+=cs[i][j-1];
				if(i&&j)cs[i][j]-=cs[i-1][j-1];
				//cerr<<cs[i][j];
			}
			//nl;
		}
		dp(0,0,n-1,m-1);
		prnt(0,0,n-1,m-1);
		printf("Case #%d:\n",kk++);
		f(i,n)printf("%s\n",gr[i]);
	}
	
	return 0;
}
