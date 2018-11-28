#include <bits/stdc++.h>

using namespace std;

int vis[101][101][101][101];

typedef struct estado{
  int hd, ad, hk, ak;;
} Estado;

queue<Estado> q;

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    if(c != 1)
      memset(vis, 0, sizeof vis);

    Estado e, aux;
    int b, d;
    scanf("%d %d %d %d %d %d", &e.hd, &e.ad, &e.hk, &e.ak, &b, &d);
    q.push(e);
    vis[e.hd][e.ad][e.hk][e.ak] = 1;

    int ans = -1;
    while(!q.empty()){
      Estado i = q.front(); q.pop();

      if(i.ad >= i.hk){ // ele mata o carinha nesse round o/ 
        ans = vis[i.hd][i.ad][i.hk][i.ak];
        while(!q.empty()) 
          q.pop();
        break;
      }

      if(e.hd > i.ak && !vis[e.hd-i.ak][i.ad][i.hk][i.ak]){ // se healou
        aux = i;
        
        i.hd = e.hd - i.ak;

        q.push(i);
        vis[i.hd][i.ad][i.hk][i.ak] = vis[aux.hd][aux.ad][aux.hk][aux.ak] + 1;
      
        i = aux;
      }
      if(i.hd > max(i.ak-d, 0) && !vis[i.hd-max(i.ak-d, 0)][i.ad][i.hk][max(i.ak-d,0)]){ // debuff
        aux = i;

        i.ak = max(i.ak-d, 0);
        i.hd = i.hd-i.ak;

        q.push(i);
        vis[i.hd][i.ad][i.hk][i.ak] = vis[aux.hd][aux.ad][aux.hk][aux.ak] + 1;

        i = aux;
      }
      if(i.hd > i.ak && !vis[i.hd-i.ak][min(i.ad+b, i.hk)][i.hk][i.ak]){ // buff 
        aux = i;

        i.hd = i.hd - i.ak;
        i.ad = min(i.ad+b, i.hk);

        q.push(i);
        vis[i.hd][i.ad][i.hk][i.ak] = vis[aux.hd][aux.ad][aux.hk][aux.ak] + 1;

        i = aux;
      }
      if(i.hd > i.ak && !vis[i.hd-i.ak][i.ad][i.hk-i.ad][i.ak]) { // attack
        aux = i;

        i.hd = i.hd - i.ak;
        i.hk = i.hk - i.ad;

        q.push(i);
        vis[i.hd][i.ad][i.hk][i.ak] = vis[aux.hd][aux.ad][aux.hk][aux.ak] + 1;

        i = aux;
      }
    }

    if(ans == -1) printf("Case #%d: IMPOSSIBLE\n", c);
    else printf("Case #%d: %d\n", c, ans);
  }
}