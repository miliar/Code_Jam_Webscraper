#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int,int,int,int> t5;
typedef tuple<int, int,int,int> t4;

set<t4> vis;

int main(){
    int cases;
    scanf("%d", &cases);

    for(int e = 0; e<cases; e++){
        int Hd, Ad, Hk, Ak, B, D;
        scanf("%d %d %d %d %d %d",&Hd, &Ad, &Hk, &Ak, &B, &D);

        vis.clear();
        queue<t5> que; // (step, hd, ad, hk, ak)
        que.push(t5(0, Hd, Ad, Hk, Ak));

        bool found = false;
        int ans = -1;

        while(!que.empty()){
            t5 t = que.front();
            que.pop();

            int step = get<0>(t);
            int hd = get<1>(t);
            int ad = get<2>(t);
            int hk = get<3>(t);
            int ak = get<4>(t);

            if(hk <= 0){
                // printf("Popped ans %d %d %d %d %d\n", step, hd, ad,hk,ak);
                ans = step;
                found = true;
                break;
            }

            if(hd <= 0){
                continue;
            }

            t4 tsave(hd,ad,hk,ak);

            if(vis.count(tsave)){
                continue;
            }
            vis.insert(tsave);

            // printf("Popped %d %d %d %d %d\n", step, hd, ad,hk,ak);


            // Attack
            {
                int next_step = step+1;
                int next_hd = max(hd - ak,0);
                int next_ad = ad;
                int next_hk = max(hk - ad, 0);
                int next_ak = ak;
                t5 next_t(next_step, next_hd, next_ad, next_hk, next_ak);
                t4 next_tsave(next_hd, next_ad, next_hk, next_ak);
                if(!vis.count(next_tsave)){
                    // printf("Pushing %d %d %d %d %d\n", next_step, next_hd, next_ad, next_hk, next_ak);
                    que.push(next_t);
                }
            }

            // Buff
            if(hd-ak > 0){
                int next_step = step+1;
                int next_hd = max(hd-ak,0);
                int next_ad = ad+B;
                int next_hk = hk;
                int next_ak = ak;
                t5 next_t(next_step, next_hd, next_ad, next_hk, next_ak);
                t4 next_tsave(next_hd, next_ad, next_hk, next_ak);
                if(!vis.count(next_tsave)){
                    // printf("Pushing %d %d %d %d %d\n", next_step, next_hd, next_ad, next_hk, next_ak);
                    que.push(next_t);
                }
            }

            // Cure
            if(Hd-ak>0){
                int next_step = step+1;
                int next_hd = max(Hd - ak,0);
                int next_ad = ad;
                int next_hk = hk;
                int next_ak = ak;
                t5 next_t(next_step, next_hd, next_ad, next_hk, next_ak);
                t4 next_tsave(next_hd, next_ad, next_hk, next_ak);
                if(!vis.count(next_tsave)){
                    // printf("Pushing %d %d %d %d %d\n", next_step, next_hd, next_ad, next_hk, next_ak);
                    que.push(next_t);
                }
            }

            // Debuff
            {
                int next_step = step+1;
                int next_ak = max(ak-D, 0);
                int next_hd = max(hd-next_ak,0);
                int next_ad = ad;
                int next_hk = hk;
                t5 next_t(next_step, next_hd, next_ad, next_hk, next_ak);
                t4 next_tsave(next_hd, next_ad, next_hk, next_ak);
                if(!vis.count(next_tsave)){
                    // printf("Pushing %d %d %d %d %d\n", next_step, next_hd, next_ad, next_hk, next_ak);
                    que.push(next_t);
                }
            }


            
        }

        if(found){
            printf("Case #%d: %d\n",e+1, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", e+1 );
        }

    }

    return 0;
}