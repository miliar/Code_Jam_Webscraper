//
//  c.cpp
//
//
//  Created by Lucca Siaudzionis on 2017-04-14.
//
//

#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii;
typedef pair<pii, pii> ppp;
typedef pair<ppp, pii> state;

int b, d;
int hd, ad;
int hk, ak;
map<state, bool> been;


int simulate(int chd, int cad, int chk, int cak, int nd, int nb){
    
    //printf("chd = %d   cad = %d  chk = %d  cak = %d  nd = %d  nb = %d\n", chd, cad, chk, cak, nd, nb);
    
    if(chk <= 0) return 0;
    if(chk - cad <= 0) return 1;
    
    if(cak < 0) cak = 0;
    
    state cur_state = state(ppp(pii(chd, cad), pii(chk, cak)), pii(nd, nb));
    
    if(been.find(cur_state) != been.end()) return 999999999;
    been[cur_state] = true;
    
    if(nd){
        
        if(cak-d >= chd){ // pause to heal and then get hit
            return 1 + simulate(hd-cak, cad, chk, cak, nd, nb);
        }
        
        // use d
        return 1 + simulate(chd-(cak-d), cad, chk, cak-d, nd-1, nb);
    }
    
    if(cak >= chd){ // pause to heal
        return 1 + simulate(hd-cak, cad, chk, cak, nd, nb);
    }
    
    if(nb){
        return 1 + simulate(chd-cak, cad+b, chk, cak, nd, nb-1);
    }
    
    //printf("--atack--\n");
    return 1 + simulate(chd-cak, cad, chk-cad, cak, nd, nb);
}

int teto(int a, int b){
    return (a+b-1)/b;
}

int main(){
    
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    
    int cases;
    cin >> cases;
    
    for(int tt = 1;tt <= cases;tt++){
        
        cin >> hd >> ad >> hk >> ak >> b >> d;
        
        
        cout << "Case #" << tt << ": ";
        if(ad >= hk){ // kill the knight with one attack
            cout << 1 << endl;
            continue;
        }
        if(ak-d >= hd){ // kill the dragon with one attack
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        
        int best = 999999999;
        int min_d = 0;
        int max_d = 0;
        if(d != 0) max_d = teto(ak, d);
        int min_b = 0;
        int max_b = 0;
        if(b != 0) max_b = teto(hk, b);
        
        for(int i = min_d;i <= max_d;i++)
        for(int j = min_b;j <= max_b;j++){
            been.clear();
            best = min(best, simulate(hd, ad, hk, ak, i, j));
        }
        
        if(best == 999999999) cout << "IMPOSSIBLE" << endl;
        else cout << best << endl;
        
    }
    
    return 0;
}
