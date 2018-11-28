#include <bits/stdc++.h>
#define maxn 1020
#define X first
#define Y second
#define pi acos(-1.0)
using namespace std;
typedef pair<double, double>pdd;
pdd p[maxn], q[maxn];
int n, m; 

bool cmp(pdd a, pdd b){
	return a.X*a.Y>b.X*b.Y;
}

double get_ans(pdd f, pdd *p){
	double now=2.0*pi*f.X*f.Y;
	for (int i=1;i<m;i++)
		now+=2.0*pi*p[i].X*p[i].Y;
	now+=pi*f.X*f.X;
	// cout<<"now: "<<now<<endl;
	return now;
}



int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++){
			scanf("%lf%lf",&p[i].X, &p[i].Y);
			q[i].X=p[i].X;
			q[i].Y=p[i].Y;
		}
		double ans=0;
		pdd f;
		for (int i=1;i<=n;i++){
			f.X=q[i].X;
			f.Y=q[i].Y;
			p[i].X=p[i].Y=0;
			sort(p+1, p+n+1, cmp);
			//for (int i=1;i<=n;i++) cout<<p[i].X<<' '<<p[i].Y<<endl;
			ans=max(ans, get_ans(f, p));
			memcpy(p, q, sizeof(q));
		}
		printf("Case #%d: %.6f\n",o, ans);
	}

	return 0;
}