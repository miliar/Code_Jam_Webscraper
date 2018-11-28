
#ifndef ONLINE_JUDGE
//#define DEBUG
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
#include <iomanip> 

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

int K[N],SS[N];

const double eps = 1e-11;
int d,n;
bool ok(long double speed)
{
	int i;
	long double tt=d/speed;
	loop(i,n)
	{
		long double pos = K[i]+(d*SS[i])/speed;

		if(pos < d) 	//and d-pos>eps)
			return 0;
	}
	return 1;
}


long double get(int idx)
{
long double v = (d-(double)K[idx])/SS[idx];
DB(v);
DB(d/v);
return d/v;
//return v;
}


#undef int
int main()
{
#define int long long
//	ios_base::sync_with_stdio(false);
	int t,m,T,l,k,ans,i,j,res=0,fl;
	t=1;
	cin>>(T);
	Loop(t,T)
	{
		cout<<"Case #"<<t<<": ";
		cin>>d>>n;
		loop(i,n)
			cin>>K[i]>>SS[i];

	        long double high=1e18+1,low;
		low = high;
		DB(get(0));
		loop(i,n)
			low = min(low,get(i));

		cout<<setprecision(20)<<low<<'\n';

		/*
		loop(i,100)
		{
			double mid = (low+high)/2;
			if(ok(mid))
				low = mid;
			else
				high = mid;
		}
*/
			
		//long double an = d/low;

	}



	return 0;
}

