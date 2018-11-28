#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
#define fst first
#define snd second
typedef pair<int,int> pii;
const int maxn=1005;
const int inf=0x3f3f3f3f;
int t,n,p,r[maxn],mmin,mmax,pac[maxn][maxn],res;
priority_queue<pii,vector<pii>,greater<pii> > que[maxn];
priority_queue<int,vector<int>,greater<int> > po;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        for (int i=0;i<maxn;++i)
            while (!que[i].empty())
                que[i].pop();
        while (!po.empty())
            po.pop();
        scanf("%d%d",&n,&p);
        for (int i=0;i<n;++i)
            scanf("%d",&r[i]);
        for (int i=0;i<n;++i)
            for (int j=0;j<p;++j) {
                scanf("%d",&pac[j][i]);
                mmin=pac[j][i]*100/(r[i]*110)+(((pac[j][i]*100)%(r[i]*110))!=0);
                mmax=pac[j][i]*100/(r[i]*90);
                if (mmin>mmax)
                    continue;
                que[i].push(pii(mmin,mmax));
                po.push(mmin);
                po.push(mmax);
            }
        int res=0;
        while (!po.empty()) {
            int p=po.top();
            po.pop();
            bool f=false;
            for (int i=0;i<n;++i) {
                while (!que[i].empty()&&que[i].top().snd<p)
                    que[i].pop();
                if (que[i].empty()||que[i].top().fst>p) {
                    f=true;
                    break;
                }
            }
            if (!f) {
                ++res;
                for (int i=0;i<n;++i)
                    que[i].pop();
            }
            for (int i=0;i<n;++i)
                if (que[i].empty())
                    break;
        }
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
