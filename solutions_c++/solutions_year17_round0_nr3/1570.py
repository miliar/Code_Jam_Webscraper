#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;

int T;
struct Node {
    long long x,y;
    bool operator <(const Node o)const {
        return x < o.x;
    }
};
long long n,m;
priority_queue<Node> PQ;

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large-out.txt","w",stdout);
    int i,j,k;
    long long p,q,r;
    long long t,tt,ttt;
    long long now,ans1,ans2,prev;
    struct Node u,uu,uuu;

    scanf("%d",&T);
for(int ii=0;ii<T;ii++) {
    now = 0;
    prev = 0;
    scanf("%I64d %I64d",&n,&m);
    while(!PQ.empty()) {
        PQ.pop();
    }
    u.x = -1; u.y = -1;
    PQ.push(u);
    u.x = n; u.y = 1;
    PQ.push(u);
    while(!PQ.empty()) {
        u = PQ.top();
        PQ.pop();
        while(1) {
            uu = PQ.top();
            if(u.x == uu.x) {
                u.y += uu.y;
                PQ.pop();
            } else break;
        }
        if(u.x % 2 == 0) {
            ans1 = u.x / 2;
            ans2 = ans1 - 1;
        } else {
            ans1 = u.x / 2;
            ans2 = ans1;
        }
        uu.x = ans1;
        uu.y = u.y;
        PQ.push(uu);
        uu.x = ans2;
        uu.y = u.y;
        PQ.push(uu);

        prev = now;
        now += (u.y);
        if(prev < m && m <= now) {
            break;
        }
    }

    printf("Case #%d: ",ii+1);
    printf("%I64d %I64d\n",ans1,ans2);
}



    return 0;
}
