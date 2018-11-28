#include <iostream>
#include <cassert>
#include <set>
#include <string>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <stdint.h>
#include <cstdio>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;

LL BB;
LL DD;
LL orig_hp;

const LL BADNESS = (1LL<<60);

typedef vector<int> KEY;

inline void try_push(vector<KEY> &next, set<KEY> &se, LL a, LL b, LL c, LL d) {
    if(a <= 0){return;}
    KEY kk;
    kk.push_back(a);
    kk.push_back(b);
    kk.push_back(c);
    kk.push_back(d);
    if(se.find(kk) == se.end()) {
        se.insert(kk);
        next.push_back(kk);
    }
}

long long dp2(LL zhp, LL zap, LL zohp, LL zoap) {
    vector<KEY> curr, next;
    set<KEY> se;
    LL out = 0;
    KEY kk;
    kk.push_back(zhp);
    kk.push_back(zap);
    kk.push_back(zohp);
    kk.push_back(zoap);
    curr.push_back(kk);
    while(!curr.empty()) {
        next.clear();
        for(int i=0;i<curr.size();++i) {
            KEY k = curr[i];
            LL hp = k[0];
            LL ap = k[1];
            LL ohp = k[2];
            LL oap = k[3];
            if(ohp <= 0) {
                return out;
            }
            {
                LL nohp = ohp - ap;
                if(nohp <= 0) {
                    try_push(next, se, hp, ap, nohp, oap);
                }
                else {
                    try_push(next, se, hp-oap, ap, nohp, oap);
                }
            }
            if(DD)
            {
                LL new_oap = max(0LL, oap - DD);
                try_push(next, se, hp - new_oap, ap, ohp, new_oap);
            }
            if(BB) {
                LL new_ap = ap + BB;
                try_push(next, se, hp - oap, new_ap, ohp, oap);
            }
            try_push(next, se, orig_hp - oap, ap, ohp, oap);
        }
        ++out;
        swap(curr, next);
    }
    return BADNESS;
}

set<vector<LL> > se;
map<vector<LL>, LL> ma;

long long dp(LL hp, LL ap, LL ohp, LL oap) {
    if(ohp <= 0){return 0;}
    if(hp <= 0){return BADNESS;}
    vector<LL> key(4, 0);
    key[0] = hp;
    key[1] = ap;
    key[2] = ohp;
    key[3] = oap;
    if(ma.find(key) != ma.end()){return ma[key];}
    if(se.find(key) != se.end()){return BADNESS;}
    se.insert(key);
    //attack
    long long out = BADNESS;
    {
        LL nohp = ohp - ap;
        if(nohp <= 0){return 1;}
        out = min(out, 1 + dp(hp - oap, ap, nohp, oap));
    }
    if(DD)
    {
        LL new_oap = max(0LL, oap - DD);
        out = min(out, 1 + dp(hp - new_oap, ap, ohp, new_oap));
    }
    if(BB) {
        LL new_ap = ap + BB;
        out = min(out, 1 + dp(hp - oap, new_ap, ohp, oap));
    }
    out = min(out, 1 + dp(orig_hp - oap, ap, ohp, oap));
    se.erase(key);
    ma[key] = out;
    return out;
}


#if 0
long long play(const LL orig_hp, LL ap, LL ohp, LL oap, LL B, LL D, LL num_b, LL num_d) {
    LL hp = orig_hp;
    long long out = 0;
    for(int i=0;i<num_d;++i) {
        int tout = 1000;

        while(1) {
            LL newoap = max(0, oap-D);
            if(hp-newoap > 0) {
                out += 1;
                oap = newoap;
                hp -= oap;
                break;
            }
            else {
                //need to cure
                out += 1;
                hp = orig_hp;
            }
        }
    }
}
#endif

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        long long myh, mya, kh, ka, B, D;
        cin >> myh >> mya >> kh >> ka >> B >> D;
        ::BB = B;
        ::DD = D;
        ::orig_hp = myh;
        se.clear();
        ma.clear();
        long long out = dp2(myh, mya, kh, ka);
        if(out >= BADNESS) {
            printf("Case #%d: %s\n", cn, "IMPOSSIBLE");
        }
        else {
            printf("Case #%d: %lld\n", cn, out);
        }
    }
    return 0;
}
