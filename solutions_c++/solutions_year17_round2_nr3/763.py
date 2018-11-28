/*
TASK: Pony Express
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
double ti[127];
long long tb[127][127];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("C-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j;
	long long k;
	cin >> T;
	int tt=0;
	while(T--)
	{
	    tt++;
	    cin >> N >> M;
	    vii xx;
	    xx.pb(mp(0,0));
	    for(i=1;i<=N;i++)
        {
            cin >> j >> k;
            xx.pb(mp(j,k));
        }
	    vi v;
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=N;j++)
            {
                cin >> k;
                tb[i][j]=k;
                if(k==-1)
                    tb[i][j]=(long long)1000*1000000000;
                if(i==j)
                    tb[i][j]=0;
            }
        }
        for(k=1;k<=N;k++)
            for(i=1;i<=N;i++)
                for(j=1;j<=N;j++)
                    tb[i][j]=min(tb[i][j],tb[i][k]+tb[k][j]);
        printf("Case #%d:",tt);
        int x,y,z;
        while(M--)
        {
            cin >> x >> y;
            for(i=1;i<=N;i++)
                ti[i]=1.0e15;
            ti[x]=0;
            priority_queue<pair<double,int> > pq;
            pq.push(mp(0.0,x));
            double p,q,r;
            while(!pq.empty())
            {
                p=-pq.top().X;
                z=pq.top().Y;
                pq.pop();
//                printf(">>> %f %d\n",p,z);
                if(p!=ti[z])
                    continue;

                for(i=1;i<=N;i++)
                {
                    if(tb[z][i]<=xx[z].X && p+(double)tb[z][i]/xx[z].Y<ti[i])
                    {
                        ti[i]=p+(double)tb[z][i]/xx[z].Y;
                        pq.push(mp(-ti[i],i));
//                        printf("%f %d\n",ti[i],i);
                    }
                }
            }

            printf(" %f",ti[y]);
        }
        printf("\n");
	}
	return 0;
}
