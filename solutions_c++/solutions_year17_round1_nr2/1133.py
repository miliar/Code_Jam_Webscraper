#include <bits/stdc++.h>
using namespace std;

const int MAXN=57; 
const int MOD=1000000007; 
const int INF=2147483647;
const double EPS=1e-8;

struct Package{
	int l,m,r;
	friend ostream& operator <<(ostream& os, const Package &p)
	{
		os<<p.m<<":["<<p.l<<","<<p.r<<"]";
		return os;
	}
};

int i,j,k,n,m,p,t,x,y,z,ans,cnt,tcase,xcase;
string s;
bool f;
int a[MAXN]; 
double nl[MAXN],nr[MAXN],need[MAXN];
Package tmp;
deque<Package> q[MAXN];

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
			for (int i = 0; i < MAXN; ++i)
			{
				q[i].clear();
			}
			ans=0;
			cin>>n>>p;
			for (int i = 0; i < n; ++i)
			{
				cin>>need[i];
				nl[i]=need[i]*0.9;
				nr[i]=need[i]*1.1;
			}
			// cout<<endl;
			for (int i = 0; i < n; ++i)
			{
				for (int j = 0; j < p; ++j)
				{
					cin>>a[j];
				}
				sort(a,a+p);
				for (int j = 0; j < p; ++j)
				{
					tmp.m=a[j];
					tmp.l=ceil(double(tmp.m)/nr[i]);
					tmp.r=floor(double(tmp.m)/nl[i]);
					if (tmp.l<=tmp.r) q[i].push_back(tmp);
				}
				// for (int j = 0; j < q[i].size(); ++j) cout<<q[i][j]<<" ";
				// cout<<endl;
			}
			while (!q[0].empty())
			{
				tmp=q[0].front();
				q[0].pop_front();
				f=false;
				for (int i = tmp.l; i <= tmp.r; ++i)
				{
					cnt=1;
					for (int j = 1; j < n; ++j)
					{
						while (q[j].size()>0 && q[j][0].r<i) q[j].pop_front();
						if (q[j].size()==0 || q[j][0].l>i) break;
						cnt++;
					}
					if (cnt==n)
					{
						f=true;
						break;
					}
				}
				if (f)
				{
					for (int j = 1; j < n; ++j) q[j].pop_front();
					ans++;
				}
			}
			cout<<ans<<endl;
		}	
	}
	return 0;
}