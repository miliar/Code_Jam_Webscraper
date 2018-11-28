/*
TASK: Steed 2: Cruise Control
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	int tt=0;
	while(T--)
	{
	    vector<pair<double,double>> v;
	    double km,s;
	    scanf("%d%d",&M,&N);
	    for(i=0;i<N;i++)
        {
            scanf("%lf%lf",&km,&s);
            v.pb(mp(km,s));
        }
        sort(ALL(v));

        double st=0.0,ed=1.0e12,mid,ans;
        int cc=4000;
        double x,y,z,t;
        double Mc=0;
        for(i=N-1;i>=0;i--)
        {
            x=M-v[i].X;
            t=x/v[i].Y;
            Mc=max(t,Mc);
        }

        tt++;

        printf("Case #%d: %f\n",tt,M/Mc);
	}
	return 0;
}
