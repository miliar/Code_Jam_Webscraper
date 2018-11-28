/*
TASK: <Task>
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
	cin >> T;
	int tt=0;
	while(T--)
	{
	    cin >> N >> M;
        vi v;
        for(i=0;i<N;i++)
        {
            cin >> k;
            v.pb(k);
        }

        int ans=0;
        if(M==2)
        {
            k=0;
            for(i=0;i<N;i++)
            {
                if(v[i]%2==0)
                    ans++;
                else
                    k++;
            }
            ans+=((k+1)/2);
        }
        else if(M==3)
        {
            int r[3];
            r[2]=r[1]=r[0]=0;
            for(i=0;i<N;i++)
                r[v[i]%3]++;
            ans+=r[0];
            k=min(r[1],r[2]);
            ans+=k;
            r[1]-=k;    r[2]-=k;
            ans+=(r[1]+2)/3;
            ans+=(r[2]+2)/3;
        }
        else if(M==4)
        {
            int r[4];
            r[3]=r[2]=r[1]=r[0]=0;
            for(i=0;i<N;i++)
                r[v[i]%4]++;
            ans+=r[0];

            int Mc=0;
            int a,b,c,d,e,f;
            for(a=0;a<=50;a++)
            {
                if(r[2]-2*a<0)
                    break;
                r[2]-=2*a;
                for(b=0;b<=50;b++)
                {
                    if(r[1]-4*b<0)
                        break;
                    r[1]-=4*b;
                    for(c=0;c<=50;c++)
                    {
                        if(r[3]-4*c<0)
                            break;
                        r[3]-=4*c;
                        for(d=0;d<=50;d++)
                        {
                            if(r[1]-d<0)
                                break;
                            if(r[3]-d<0)
                                break;
                            r[1]-=d;
                            r[3]-=d;
                            for(e=0;e<=50;e++)
                            {
                                if(r[1]-2*e<0)
                                    break;
                                if(r[2]-e<0)
                                    break;
                                r[1]-=2*e;
                                r[2]-=e;
                                for(f=0;f<=50;f++)
                                {
                                    if(r[3]-2*f<0)
                                        break;
                                    if(r[2]-f<0)
                                        break;
                                    r[3]-=2*f;
                                    r[2]-=f;
                                    k=0;
                                    if(r[2]+r[3]+r[1])
                                        k=1;
//                                    printf("%d %d %d %d %d %d %d\n",a,b,c,d,e,f,k);
                                    Mc=max(Mc,a+b+c+d+e+f+k);
                                    r[3]+=2*f;
                                    r[2]+=f;
                                }
                                r[1]+=2*e;
                                r[2]+=e;
                            }
                            r[1]+=d;
                            r[3]+=d;
                        }
                        r[3]+=4*c;
                    }
                    r[1]+=4*b;
                }
                r[2]+=2*a;
            }
            ans+=Mc;
        }
        tt++;
        printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
