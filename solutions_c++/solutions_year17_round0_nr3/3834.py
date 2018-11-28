#include<cstdio>
#include<queue>
using namespace std;

int main() {
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        int n,k;scanf("%d%d",&n,&k);
        priority_queue<int> q;
        q.push(n);
        for(int i=1;i<k;++i) {
            int now=q.top();q.pop();
            if(now&1) {
                q.push(now/2);
                q.push(now/2);
            } else {
                q.push(now/2-1);
                q.push(now/2);
            }
        }
        int now=q.top();
        int a=now/2,b=now/2;
        if(now%2==0) --b;
        printf("%d %d\n",a,b);
    }
    return 0;
}
