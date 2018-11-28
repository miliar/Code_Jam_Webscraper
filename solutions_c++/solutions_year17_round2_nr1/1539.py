#include<bits/stdc++.h>
#define up(j,k,i) for(i=j;i<k;i++)
#define down(j,k,i) for(i=j;i>k;i--)
#define pp(n) printf("%lld\n",n)
#define ps(s) printf("%s",s)
#define is(n) scanf("%lld",&n)
#define ips(n) scanf("%lld",n)
#define ss(s) scanf("%s",s)
#define cool 0
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define f(i) cout<<i<<endl;
#define pll pair<lld,lld> 
#define pi acos(-1)
#define dg(x) cout<<#x<<' '<<x<<endl;
#define dg2(x,y) cout<<#x<<' '<<x<<' '<<#y<<' '<<y<<endl;
#define dg3(x,y,z) cout<<#x<<' '<<x<<' '<<#y<<' '<<y<<' '<<#z<<' '<<z<<endl;
#define ds(n,m) scanf("%lld %lld",&n,&m)
#define ts(n,m,k) scanf("%lld %lld %lld",&n,&m,&k)
typedef long double ld;
typedef long long int lld;
using namespace std;
const lld M=1e4;
lld i,j,k,z,t,n,m,sum,ans,x,y;
ld start_point[M],speed[M];
ld d;
bool check(ld test)
{		
		up(0,n,i)
		if(speed[i]<test and test*start_point[i]<d*(test-speed[i]))
		return false;
	
	return true;
}
int main()
{
		freopen("BB.in","r",stdin);
		freopen("1.out","w",stdout);
	lld tt;
	is(tt);
	up(1,tt+1,t)
	{
	
		cin>>d>>n;
	   ld myspeed=0;
		up(0,n,i)
		{
		  cin>>start_point[i]>>speed[i];
	    ld temp=((d-start_point[i])/speed[i]);
	    if(temp>myspeed)myspeed=temp;
	  
	  }
	  myspeed=d/myspeed;
	  
		
	
		cout<<"Case #"<<t<<": "; cout<<fixed<<setprecision(6)<<myspeed<<endl;
	
	}
}
