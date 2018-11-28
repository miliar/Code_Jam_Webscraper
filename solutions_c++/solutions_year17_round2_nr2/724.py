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

//bool p[3][3][1002][1002];
//int vs[3][3][1002][1002],qk;
char rs[1005];

//map< int, char >p[3][1002][1002];
//char lst[]={"RBY"};

//int dp(char st,char ls,int r,int b,int g)
//{
	//if(r+b+g==0)
	//{
		//if(st!=ls)return 1;
		//return 0;
	//}
	
	//if( p[ls][r][b].find(g)!=p[ls][r][b].end() )return 0;
	//p[ls][r][b][g]=0;
	
	////bool &pr=p[st][ls][r][b];
	////if(vs[st][ls][r][b]==qk)return pr;
	////vs[st][ls][r][b]=qk;
	
	//if( r && ls!=0 && dp(st,0,r-1,b,g) )return p[ls][r][b][g]=1;
	//if( b && ls!=1 && dp(st,1,r,b-1,g) )return p[ls][r][b][g]=2;
	//if( g && ls!=2 && dp(st,2,r,b,g-1) )return p[ls][r][b][g]=3;
	//return 0;
//}

//void prnt(char st,char ls,int r,int b,int g)
//{
	//if(r+b+g==0)
	//{
		//rs[r+b+g]=lst[st];
		//return ;
	//}
	
	//int q=p[ls][r][b][g];
	
	//if( q==1 )
	//{
		//rs[r+b+g]=lst[0];
		//prnt(st,0,r-1,b,g);
		//return ;
	//}
	//else if( q==2 )
	//{
		//rs[r+b+g]=lst[1];
		//prnt(st,1,r,b-1,g);
		//return ;
	//}
	//else if( q==3 )
	//{
		//rs[r+b+g]=lst[2];
		//prnt(st,2,r,b,g-1);
		//return ;
	//}
	//assert(0);
//}

//void slve(int n,int r,int b,int g)
//{
	//int i,j,k;
	
	//lst[0]='R';
	//lst[1]='B';
	//lst[2]='Y';
	//int q[3];
	//q[0]=r;
	//q[1]=b;
	//q[2]=g;
	
	//f(i,n)
	//{
		//f(j,2)
		//{
			//if( q[j]>q[j+1] )
			//{
				//swap(q[j],q[j+1]);
				//swap(lst[j],lst[j+1]);
			//}
		//}
	//}
	
	
	//if(r)
	//{
		//f(i,r+1)f(j,g+1)f(k,3)p[k][i][j].clear();
		//if(dp(0,0,r-1,g,b))
		//{
			//prnt(0,0,r-1,g,b);
			//rs[n]=0;
			//printf("Case #%d: %s\n",kk++,rs);
			//return ;
		//}
	//}
	//if(g)
	//{
		//f(i,r+1)f(j,g+1)f(k,3)p[k][i][j].clear();
		//if(dp(1,1,r,g-1,b))
		//{
			//prnt(1,1,r,g-1,b);
			//rs[n]=0;
			//printf("Case #%d: %s\n",kk++,rs);
			//return ;
		//}
	//}
	//if(b)
	//{
		//f(i,r+1)f(j,g+1)f(k,3)p[k][i][j].clear();
		//if(dp(2,2,r,g,b-1))
		//{
			//prnt(2,2,r,g,b-1);
			//rs[n]=0;
			//printf("Case #%d: %s\n",kk++,rs);
			//return ;
		//}
	//}
	//printf("Case #%d: IMPOSSIBLE\n",kk++);
//}

pair< int , char >q[3];

void slv(int n,int r,int b,int y)
{
	q[0]=mpr(r,'R');
	q[1]=mpr(b,'B');
	q[2]=mpr(y,'Y');
	sort(q,q+3);
	reverse(q,q+3);
	
	q[0].xx-=q[1].xx;
	
	if( q[0].xx>q[2].xx )
	{
		printf("Case #%d: IMPOSSIBLE\n",kk++);
		return ;
	}
	
	q[2].xx-=q[0].xx;
	
	if(q[2].xx>q[1].xx)
	{
		printf("Case #%d: IMPOSSIBLE\n",kk++);
		return ;
	}
	
	//cerr<<q[1].xx<<" : "<<q[0].yy<<q[1].yy<<endl;
	//cerr<<q[0].xx<<" : "<<q[0].yy<<q[2].yy<<endl;
	//cerr<<q[2].xx<<" : "<<q[2].yy<<endl;
	
	int i;
	printf("Case #%d: ",kk++);
	int cnt=0;
	f(i,q[1].xx)
	{
		printf("%c%c",q[0].yy,q[1].yy);
		cnt+=2;
		if(q[2].xx)
		{
			q[2].xx--;
			cnt++;
			printf("%c",q[2].yy);
		}
	}
	
	
	//cerr<<q[2].xx<<" : "<<q[2].yy<<endl;
	f(i,q[0].xx)
	{
		printf("%c%c",q[0].yy,q[2].yy);
		cnt+=2;
	}
	nl;
	//cerr<<n<<" :: "<<cnt<<endl;
	assert(cnt==n);
}

int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	int t,i,j,k,l;
	
	int n,r,o,y,g,b,v;
	sc(ts);
	while(ts--)
	{
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		if(o+g+v==0)
		{
			slv(n,r,b,y);
			continue;
		}
		assert(0);
	}
	
	return 0;
}
