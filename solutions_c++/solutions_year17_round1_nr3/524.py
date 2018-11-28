#include <bits/stdc++.h>
using namespace std;
int hd, ad, hk, ak, b, d;

struct state{
    int hd;
    int ad;
    int hk;
    int ak;
};
void fi(state& s, int aa, int bb, int cc, int dd){
    s.hd = aa;
    s.ad = bb;
    s.hk = cc;
    s.ak = dd;
}
bool vis[101][101][101][101];
int bfs(){
    memset(vis, 0, sizeof vis);
    queue<state> q;
    state first;
    fi(first, hd, ad, hk, ak);
    int sz, depth = 0;
    vis[first.hd][first.ad][first.hk][first.ak] = 1;

    q.push(first);
    while(sz = q.size()){
    while(sz--){//cout << 1 << endl;
        state pr = q.front();q.pop();//cout << pr.hd << ' ' << pr.ad << ' ' << ' ' << pr.hk << ' ' << pr.ak << endl;
        if(pr.hk <= 0)return depth;
        if(pr.hd <= 0)continue;
        state next;
        fi(next, hd - pr.ak, pr.ad, pr.hk, pr.ak);
        next.hd = max(next.hd, 0);
        if(!vis[next.hd][next.ad][next.hk][next.ak]){
            vis[next.hd][next.ad][next.hk][next.ak] = 1;
            q.push(next);
        }
        next = *(new state);
        fi(next, pr.hd - pr.ak, pr.ad, pr.hk - pr.ad, pr.ak);
        next.hd = max(next.hd, 0);
        if(!vis[next.hd][next.ad][next.hk][next.ak]){
            vis[next.hd][next.ad][next.hk][next.ak] = 1;
            q.push(next);
        }
                    next = *(new state);

        fi(next, pr.hd - pr.ak, pr.ad + b, pr.hk, pr.ak);
        next.hd = max(next.hd, 0);
        if(!vis[next.hd][next.ad][next.hk][next.ak]){
        vis[next.hd][next.ad][next.hk][next.ak]  = 1;
            q.push(next);
        }
                    next = *(new state);
        fi(next, pr.hd - ((pr.ak - d > 0) ? (pr.ak - d) : 0), pr.ad, pr.hk, (pr.ak - d > 0) ? (pr.ak - d) : 0);
        next.hd = max(next.hd, 0);
        if(!vis[next.hd][next.ad][next.hk][next.ak]){
            vis[next.hd][next.ad][next.hk][next.ak]  = 1;
            q.push(next);
        }
    }
    depth++;
    }
    return -1;

}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for(int cs = 0;cs < tc;cs++){
        cin >> hd >> ad >> hk >> ak >> b >> d;

        int res = bfs();
        if(res == -1)
            printf("Case #%d: IMPOSSIBLE\n", cs + 1);
        else
            printf("Case #%d: %d\n", cs + 1, res);
    }
}
