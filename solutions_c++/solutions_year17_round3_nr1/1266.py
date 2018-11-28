#include <bits/stdc++.h>
using namespace std;

const long long MAXN=1007; 
const long long MOD=1000000007; 
const long long INF=2147483647;
const double EPS=1e-8;
const double PI=acos(-1.0);

struct Pancake
{
	long long r,h;
	bool operator <(const Pancake &p) const
	{
		long long side=r*h*2LL;
		long long sideP=p.r*p.h*2LL;
		return side > sideP;
	}
	long long side()
	{
		return r*h*2LL;
	}
	long long top()
	{
		return r*r;
	}
};

long long i,j,k,n,m,p,t,x,y,z,cnt,tcase,xcase,mxr,mkr;
string s;
double ans;
Pancake a[MAXN]; 


int main()
{
#ifdef Smile
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	// ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": ";
			cin>>n>>k;
			for (long long i = 0; i < n; ++i)
			{
				cin>>a[i].r>>a[i].h;
			}
			sort(a,a+n);
			mxr = 0;
			for (long long i = 0; i < n; ++i)
			{
				if (a[i].r > a[mxr].r)
				{
					mxr = i;
				}
			}
			cnt=0;
			mkr=0;
			for (long long i = 0; i < k-1; ++i)
			{
				cnt+=a[i].side();
				// cout<<cnt<<endl;
				if (a[i].r > a[mkr].r)
				{
					mkr = i;
				}
			}
			if (a[k-1].r > a[mkr].r)
			{
				mkr = k-1;
			}
			// cout<<mxr<<">"<<mkr<<endl;
			// for (long long i = 0; i < n; ++i)
			// {
			// 	cout<<a[i].r<<", "<<a[i].h<<endl;
			// }
			if (mxr>=k)
				cnt += max(a[mxr].side()+a[mxr].top(),a[k-1].side()+a[mkr].top());
			else
				cnt += a[k-1].side()+a[mkr].top();
			ans=cnt;
			ans*=PI;
			// cout<<cnt<<endl;
			// cout<<ans<<endl;
			printf("%.10f\n", ans);
		}	
	}
	return 0;
}