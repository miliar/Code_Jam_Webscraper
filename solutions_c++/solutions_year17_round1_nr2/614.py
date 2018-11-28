#include <bits/stdc++.h>

#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define pb push_back
#define LL long long
#define F first
#define S second
#define VPI vector< pair<int,int> >
#define VVI vector< vector<int> > 
#define BC(x) __builtin_popcount(x)

#define maxn 59
#define maxp 59

using namespace std;

int l[maxn][maxp], r[maxn][maxp];
int c[maxn];

struct mycomp
{
	bool operator()(pair<int, pair<int,int> > &a , pair<int, pair<int,int> > &b  )
	{
		if(a.F < b.F)
			return true;
		else if(a.F == b.F && a.S.S < b.S.S)
			return true;
		else if(a.F == b.F && a.S.S == b.S.S && a.S.F < b.S.F)
			return true;
		return false;
	}
};

int main()
{
	int t;
	icin(t);
	for(int tc=1; tc<=t; tc++)
	{
		int n,p;
		icin(n);
		icin(p);
		for(int i=1; i<=n; i++)
			icin(c[i]);
		vector< pair<int, pair<int,int> > > vec;
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=p; j++)
			{
				int a;
				icin(a);
				double x = (10*a*1.0)/(11*c[i]);
				double y = (10*a*1.0)/(9*c[i]);
				l[i][j] = ceil(x);
				r[i][j] = floor(y);
			//	cout << l[i][j] << " " << r[i][j] << endl;
				vec.pb({l[i][j],{i,1}});
				vec.pb({r[i][j],{i,2}});
			}
		}
		sort(vec.begin(),vec.end(), mycomp());
		vector<int> oc(n+1,0),ig(n+1,0);
		int cur = 0;
		int ans = 0;
		for(auto it:vec)
		{
			int a = it.S.F;
			int t = it.S.S;
		//	cout << it.F << " " << a << " " << t << endl;
			if(t == 1)
			{
				oc[a]++;
				cur = 0;
				for(int i=1; i<=n; i++)
				{
					if(oc[i] > 0)
						cur++;
				}
				if(cur == n)
				{
					ans++;
					for(int i=1; i<=n; i++)
					{
						oc[i]--;
						ig[i]++;
					}
				}
			}
			else
			{
				if(ig[a] > 0)
					ig[a]--;
				else
					oc[a]--;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}


