#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> P;

priority_queue<P> a,b;

int pos[3][1005];

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    int n,m,c;
    scanf("%d",&T);
    for(int cs = 1;cs <= T;cs++){
        scanf("%d%d%d",&n,&c,&m);
        memset(pos,0,sizeof(pos));
        int na,nb,ans,pro;
        na = nb = ans = pro = 0;
        for(int i = 0;i < m;i++){
            int x,y;
            scanf("%d%d",&x,&y);
            pos[y][x]++;
            if(y == 1) na++;
            if(y == 2) nb++;
        }
        for(int i = 2;i <= n;i++){
            if(pos[1][i]) a.push(P(pos[1][i],i));
            if(pos[2][i]) b.push(P(pos[2][i],i));
        }
        if(pos[1][1]){
            ans += pos[1][1];
            while(!b.empty()&&pos[1][1]){
                P tmp = b.top();
                b.pop();
                if(pos[1][1]<tmp.first){
                    b.push(P(tmp.first-pos[1][1],tmp.second));
                    //ans += pos[1][1];
                    pos[1][1] = 0;
                }
                else{
                    pos[1][1] -= tmp.first;
                    //ans += tmp.first;
                }
            }
            //ans += pos[1][1];
        }
        if(pos[2][1]) b.push(P(pos[2][1],1));
        while(!a.empty()&&!b.empty()){
            P tmpa = a.top(); a.pop();
            ans += tmpa.first;
            while(tmpa.first != 0&&!b.empty()){
                P tmpb = b.top(); b.pop();
                if(tmpb.second == tmpa.second){
                    while(tmpa.first!=0&&!b.empty()){
                        P tmp = b.top(); b.pop();
                        //ans += min(tmpa.first,tmp.first);
                        if(tmpa.first < tmp.first){
                            tmp.first -= tmpa.first;
                            b.push(tmp);
                            tmpa.first = 0;
                        }
                        else{
                            tmpa.first -= tmp.first;
                        }
                    }
                    //ans += min(tmpa.first,tmpb.first);
                    pro += min(tmpa.first,tmpb.first);
                    if(tmpa.first < tmpb.first){
                        tmpb.first -= tmpa.first;
                        b.push(tmpb);
                        tmpa.first = 0;
                    }
                    else{
                        tmpa.first -= tmpb.first;
                    }
                    //b.push(tmpb);
                }
                else{
                    if(tmpa.first < tmpb.first){
                        tmpb.first -= tmpa.first;
                        b.push(tmpb);
                        tmpa.first = 0;
                    }
                    else{
                        tmpa.first -= tmpb.first;
                    }
                }
            }
            //ans += tmpa.first;
        }
        while(!a.empty()){
            P tmp = a.top(); a.pop();
            ans += tmp.first;
        }
        while(!b.empty()){
            P tmp = b.top(); b.pop();
            ans += tmp.first;
        }
        printf("Case #%d: %d %d\n",cs,ans,pro);

    }
    return 0;
}
