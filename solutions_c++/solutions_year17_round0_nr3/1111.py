#include<bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef long long int LL;
typedef pair<LL,LL> pii;
int main(){
    int t,C=0;
    scanf("%d",&t);
    LL x,y;
    while(t--){
        scanf("%lld%lld",&x,&y);
        printf("Case #%d: ",++C);
        priority_queue<pii> que;
        LL ans1,ans2;
        que.push({x,1});
        while(y>0){
            pii tmp = que.top();
            que.pop();
            if(que.size() && que.top().x == tmp.x){
                pii out = que.top();
                que.pop();
                out.y += tmp.y;
                que.push(out);
                continue;
            }
            LL ma = tmp.x / 2;
            LL mi = (tmp.x - 1) / 2;
            y -= tmp.y;
            ans1 = ma;
            ans2 = mi;
            que.push({ma, tmp.y});
            que.push({mi, tmp.y});
        }
        printf("%lld %lld\n",ans1,ans2);
    }
}

