#include <bits/stdc++.h>
using namespace std;

const int MAXN=207; 
const int MOD=1000000007; 
const int INF=2147483647;
const int TOTAL=1440;
const int HALF=720;
const double EPS=1e-8;

struct Interval
{
	int l,r,belong;
	bool operator <(const Interval &p) const
	{
		return l<p.l;
	}
	Interval () {}
	Interval (int l, int r, int belong):l(l),r(r),belong(belong) {}
};

int i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
int s[2],r[2];
Interval a[MAXN]; 
vector<int> b[2];

int main()
{
#ifdef Smile
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	while (cin>>tcase)
	{
		xcase=0;
		while (xcase<tcase)
		{
			xcase++;
			cout<<"Case #"<<xcase<<": ";
			b[0].clear();
			b[1].clear();
			s[0]=0;
			s[1]=0;
			r[0]=HALF;
			r[1]=HALF;
			cnt=0;
			cin>>n>>m;
			for (int i = 0; i < n; ++i)
			{
				cin>>a[i].l>>a[i].r;
				a[i].belong=0; // 0 for n
				r[0]-=a[i].r-a[i].l;
			}
			for (int i = 0; i < m; ++i)
			{
				cin>>a[i].l>>a[i].r;
				a[i].belong=1; // 0 for m
				r[1]-=a[i].r-a[i].l;
			}
			sort(a,a+n+m);
			x=a[0].belong;
			for (int i = 1; i < n+m; ++i)
			{
				if (a[i].belong==a[i-1].belong) // 连续两段属于同一个人
				{
					if (a[i-1].r<a[i].l) // 中间有空隙
					{
						b[a[i].belong].push_back(a[i].l-a[i-1].r);
						s[a[i].belong]+=a[i].l-a[i-1].r;
					}
				}
				else
				{
					cnt++;
				}
			}
			if (a[0].belong==a[n+m-1].belong) // 连续两段属于同一个人
			{
				if (a[n+m-1].r<a[0].l+TOTAL) // 中间有空隙
				{
					b[a[0].belong].push_back(a[0].l+TOTAL-a[n+m-1].r);
					s[a[0].belong]+=a[0].l+TOTAL-a[n+m-1].r;
				}
			} 
			else
			{
				cnt++;
			}
			// cout<<cnt<<endl;
			// cout<<r[0]<<" "<<s[0]<<endl;
			// cout<<r[1]<<" "<<s[1]<<endl;
			if (r[0]<s[0])
			{
				sort(b[0].begin(),b[0].end());
				for (int i = 0; i < b[0].size(); ++i)
				{
					r[0]-=b[0][i];
					if (r[0]<0)
					{
						cnt+=2;
					}
				}
			}
			else if (r[1]<s[1])
			{
				sort(b[1].begin(),b[1].end());
				for (int i = 0; i < b[1].size(); ++i)
				{
					r[1]-=b[1][i];
					if (r[1]<0)
					{
						cnt+=2;
					}
				}
			}
			cout<<cnt<<endl;
		}	
	}
	return 0;
}