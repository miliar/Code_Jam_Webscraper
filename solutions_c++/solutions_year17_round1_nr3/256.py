#include<bits/stdc++.h>
using namespace std;
const int MX = 100 , inf = (1<<29);
int buff , debuff;
int HD;
int assure(int health , int attack , int dhealth , int dattack){
    int ret =0;
    if(health <= 0) return inf;
    if(dhealth == 0) return 0;
    if(dhealth - attack <= 0) return 1;
    if(HD - dattack - dattack <= 0) return inf;
    while(1){
        ++ret;
        //puts("#");
        if(dhealth - attack <= 0) return ret;
        if(health - dattack <= 0) health = HD;
        else dhealth -= attack;
        health -= dattack;
    }
    return ret;
}
int solve(int health , int attack , int dhealth , int dattack){
    int cur = 0 , ret = assure(health , attack , dhealth , dattack);
    while(cur <= 100){
        ++cur;
        if(health - dattack <= 0) health = HD;
        else attack += buff;
        health -= dattack;
        ret = min(ret , cur + assure(health , attack , dhealth , dattack));
        if(attack > dhealth) break;
    }
    return ret;
}
int T , Tn;
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    int aa = 0;
    while(T--){
        int health , attack , dhealth , dattack;
        cin>>health>>attack>>dhealth>>dattack>>buff>>debuff;
        HD = health;
    //    cerr<<"ok"<<++aa<<endl;
        printf("Case #%d: ",++Tn);
        if(dhealth - attack <=  0){
            puts("1");
            continue;
        }
        if(health - dattack + debuff <= 0){
            puts("IMPOSSIBLE");
            continue;

        }
        int ans = solve(health , attack , dhealth , dattack);
        int cur = 0;
        while(cur <= 100){
            ++cur;
            if(health - dattack + debuff > 0){
                dattack -= debuff;
                dattack = max(dattack , 0);
            }
            else health = HD;
            health -= dattack;
            ans = min(ans , cur + solve(health , attack , dhealth , dattack));
            if(dattack == 0) break;
        }
        if(ans == inf) ans = -1;
        if(ans == -1) puts("IMPOSSIBLE");
        else cout<<ans<<endl;
    }
}

