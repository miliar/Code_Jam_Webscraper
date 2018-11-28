#include <cstdio>
#include <queue>
using namespace std;
const double det=0.0001;
const double eps=1e-12;
int t,n,k;
double p,u;
priority_queue<double,vector<double>,greater<double> > que;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%d%d%lf",&n,&k,&u);
        for (int i=0;i<n;++i) {
            scanf("%lf",&p);
            que.push(p);
        }
        while (u>eps*100) {
            u-=det;
            double temp=que.top();
            if (temp>=1.0-eps)
                break;
            temp+=det;
            que.pop();
            que.push(temp);
        }
        double res=1;
        while (!que.empty()) {
            res*=que.top();
            que.pop();
        }
        printf("Case #%d: %.12f\n",cas,res);
    }
    return 0;
}
