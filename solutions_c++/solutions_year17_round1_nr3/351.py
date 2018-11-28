#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

using namespace std;

struct Node{
    int Hd,Ad,Hk,Ak;
    bool operator < (const Node &b) const{
        if(Hd != b.Hd) return Hd < b.Hd;
        if(Ad != b.Ad) return Ad < b.Ad;
        if(Hk != b.Hk) return Hk < b.Hk;
        return Ak < b.Ak;
    }
};

map<Node,int> dis;
set<Node> inque;
int HD,AD,HK,AK,B,D;

void solve(){
    
    queue<Node> que;
    que.push((Node){HD,AD,HK,AK});
    inque.clear();
    dis.clear();
    dis[(Node){HD,AD,HK,AK}] = 0;
    inque.insert((Node){HD,AD,HK,AK});
    int res = 0x3f3f3f3f;
    while(!que.empty()){
        Node cur = que.front();
        que.pop();
        inque.erase(cur);
        if(!cur.Hd) continue;
        if(!cur.Hk) res = min(res,dis[cur]);
        //Atk
        Node aftatk = cur;
        aftatk.Hk = max(aftatk.Hk-aftatk.Ad,0);
        if(aftatk.Hk) aftatk.Hd = max(aftatk.Hd-aftatk.Ak,0);
        if(aftatk.Hd && (!dis.count(aftatk) || dis[aftatk] > dis[cur] +1)){
            dis[aftatk] = dis[cur] + 1;
            if(!inque.count(aftatk)) {
                que.push(aftatk);
                inque.insert(aftatk);
            }
        }
        //Deb
        Node aftdeb = cur;
        aftdeb.Ak = max(aftdeb.Ak-D,0);
        aftdeb.Hd = max(aftdeb.Hd-aftdeb.Ak,0);
        if(aftdeb.Hd && (!dis.count(aftdeb) || dis[aftdeb] > dis[cur] + 1)){
            dis[aftdeb] = dis[cur] + 1;
            if(!inque.count(aftdeb)){
                que.push(aftdeb);
                inque.insert(aftdeb);
            }
        }
        
        //Cur
        Node aftcur = cur;
        aftcur.Hd = HD;
        aftcur.Hd = max(aftcur.Hd-aftcur.Ak,0);
        if(aftcur.Hd && (!dis.count(aftcur) || dis[aftcur] > dis[cur] + 1)){
            dis[aftcur] = dis[cur] + 1;
            if(!inque.count(aftcur)){
                que.push(aftcur);
                inque.insert(aftcur);
            }
        }
        //Buf
        Node aftbuf = cur;
        aftbuf.Ad += B;
        aftbuf.Hd = max(aftbuf.Hd-aftbuf.Ak,0);
        if(aftbuf.Ad > 2*aftbuf.Hk) continue;
        if(aftbuf.Hd && (!dis.count(aftbuf) || dis[aftbuf] > dis[cur] + 1)){
            dis[aftbuf] = dis[cur] + 1;
            if(!inque.count(aftbuf)){
                que.push(aftbuf);
                inque.insert(aftbuf);
            }
        }
    }
    if(res >= 0x3f3f3f3f-1) puts("IMPOSSIBLE");
    else printf("%d\n",res);
    
}

int main(int argc, char *argv[]){
    
    int caseCnt = 0;
    scanf(" %d",&caseCnt);
    for(int d = 1;d <= caseCnt;d++){
        printf("Case #%d: ",d);
        scanf(" %d %d %d %d %d %d",&HD,&AD,&HK,&AK,&B,&D);
        solve();
    }
    
    return 0;
}
