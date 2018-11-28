#include <cstdio>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;
int HD,AD,HK,AK,B,D;
struct arg_t{
    int hd;
    int ad;
    int hk;
    int ak;
}typedef bttarg;
bool operator==(bttarg a,bttarg b){
    return a.hd == b.hd && a.ad == b.ad && a.hk == b.hk && a.ak == b.ak;
}
bool operator!=(bttarg a,bttarg b){
    return !(a == b);
}
bttarg parent[105][105][105][105];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    queue<bttarg> q;
    bttarg cur,next;
    bttarg NILARG;
    NILARG.hd = NILARG.ad = NILARG.hk = NILARG.ak = -1;
    for(int i = 1; i <= t; i++){
        for(int m = 0; m < 105; m++){
            for(int j = 0; j < 105; j++){
                for(int k = 0; k < 105; k++){
                    for(int l = 0; l < 105; l++){
                        parent[m][j][k][l] = NILARG;
                    }
                }
            }
        }
        //printf("CHK1");
        scanf("%d%d%d%d%d%d",&HD,&AD,&HK,&AK,&B,&D);
        bttarg startarg;
        startarg.hd = HD;
        startarg.ad = AD;
        startarg.hk = HK;
        startarg.ak = AK;
        q.push(startarg);
        bool b = false;
        while(!q.empty()){
            cur = q.front();
            q.pop();
            /// SKILL ONE:
            next = cur;
            next.hk -= next.ad;
            next.hd -= next.ak;
            if(next.hk <= 0){
                b = true;
                break;
            }else if(next.hd > 0 && parent[next.hd][next.ad][next.hk][next.ak] == NILARG){
                parent[next.hd][next.ad][next.hk][next.ak] = cur;
                q.push(next);
            }

            /// SKILL TWO:
            next = cur;
            next.ad += B;
            next.hd -= next.ak;
            if(next.hd > 0 && parent[next.hd][next.ad][next.hk][next.ak] == NILARG){
                parent[next.hd][next.ad][next.hk][next.ak] = cur;
                q.push(next);
            }
            /// SKILL THREE:
            next = cur;
            next.hd = HD - next.ak;
            if(next.hd > 0 && parent[next.hd][next.ad][next.hk][next.ak] == NILARG){
                parent[next.hd][next.ad][next.hk][next.ak] = cur;
                q.push(next);
            }

            /// SKILL FOUR:
            next = cur;
            next.ak -= D;
            next.ak = max(next.ak,0);
            next.hd -= next.ak;
            if(next.hd > 0 && parent[next.hd][next.ad][next.hk][next.ak] == NILARG){
                parent[next.hd][next.ad][next.hk][next.ak] = cur;
                q.push(next);
            }
        }
        while(!q.empty()){
            q.pop();
        }
        if(!b){
            printf("Case #%d: IMPOSSIBLE\n",i);
            continue;
        }
        int c = 1;
        while(cur != startarg){
            cur = parent[cur.hd][cur.ad][cur.hk][cur.ak];
            c++;
        }
        printf("Case #%d: %d\n",i,c);
    }
    return 0;
}
