
#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<utility>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) cout<<n<<' '
#define si(n) cin>>n
#define int long long 
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
#include<iomanip>
#define F first
#define S second
#define sz(x) (int) x.size()
#define pLL(x) cout<<x<<' '
#define fill(x,c) memset(x,c,sizeof(x))
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#ifdef DEBUG
#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#else
#define DB(x)
#define DB2(x,y)
#define DB3(x,y,z)
#endif



const int N=5e5+5;

int r[N],h[N];
const double PI=atan(1)*4;

const int inf = 1e15;

VPII pp;

int dp[1005][1005];

int n,k;
int f(int idx,int taken)
{
	// take
	
	if(taken>k) return -inf;
	if(idx == n)
	{
		if(taken == k)
			return 0;
		return -inf;
	}

	int &ret = dp[idx][taken];
	if(ret!=-1) return ret;

	int r=pp[idx].F;
	int h=pp[idx].S;
	
	int x = 0;
	if(taken == 0)
		x=r*r+2*r*h;
	else
		x=2*r*h;

	ret = max(x+f(idx+1,taken+1),f(idx+1,taken));
	return ret;
}

#undef int
int main()
{
#define int long long
	ios_base::sync_with_stdio(false);
	int t,m,T,l,ans,i,j,res=0,fl;
	t=1;
	cin>>(T);
	Loop(t,T)
	{
		cout<<"Case #"<<t<<": ";
		cin>>n>>k;
		pp.clear();
		loop(i,n)
		{
			cin>>r[i]>>h[i];
			pp.pb(mp(r[i],h[i]));
		}

		sort(pp.rbegin(),pp.rend());
		int maxi = 0,curr;
		
		
		fill(dp,-1);
		ans = f(0,0);
		double val = PI*ans;


		cout<<setprecision(15)<<val<<'\n';
        

	}
	return 0;
}

