/*
TASK: Stable Neigh-bors
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
char mm[10005];
int tb[10];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	cin >> T;
	int tt=0;
	while(T--)
	{
	    cin >> N;
	    for(i=0;i<6;i++)
            cin >> tb[i];
        vector<pair<int,char> > v;
        v.pb(mp(tb[0],'R'));
        v.pb(mp(tb[2],'Y'));
        v.pb(mp(tb[4],'B'));
        sort(ALL(v));
        int x=v[2].X;   char xx=v[2].Y;
        int y=v[1].X;   char yy=v[1].Y;
        int z=v[0].X;   char zz=v[0].Y;
        memset(mm,0,sizeof mm);
        for(i=0,j=0;i<x;i++,j+=3)
            mm[j]=xx;
        for(j=(x-1)*3+1,i=0;i<y;j-=3,i++)
            mm[j]=yy;
        for(i=0;i<z && j>0;j-=3,i++)
            mm[j]=zz;
        bool ok=false;
        if(j<0)
        {
            ok=true;
            for(j=(x-1)*3+2;i<z ;j-=3,i++)
                mm[j]=zz;
        }
        tt++;
        printf("Case #%d: ",tt);
        if(ok)
        {
            for(i=0;i<5000;i++)
            {
                if(mm[i])
                    printf("%c",mm[i]);
            }
        }
        else
            printf("IMPOSSIBLE");
        printf("\n");
	}
	return 0;
}
