
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

ll needHit(ll atk, ll h) {
    if(h%atk)
        return h/atk;
    return h/atk + 1;
}

struct stat{
    ll Hd, Ad, Hk, Ak, turn;
    stat() {};
    stat(ll ihd, ll iad, ll ihk, ll iak, ll iturn):
        Hd(ihd), Ad(iad), Hk(ihk), Ak(iak), turn(iturn) {};
};

struct cmp{
    bool operator()(stat s1, stat s2) {
        if(s1.Hd != s2.Hd)
            return s1.Hd < s2.Hd;
        if(s1.Ad != s2.Ad)
            return s1.Ad < s2.Ad;
        if(s1.Hk != s2.Hk)
            return s1.Hk < s2.Hk;
        return s1.Ak < s2.Ak;
    }
} ;

void sol(){
    ll Hd, Ad, Hk, Ak, B, D ;
    scanf("%lld%lld%lld%lld%lld%lld", &Hd, &Ad, &Hk, &Ak, &B, &D);
    queue<stat> Q ; 
    Q.push(stat(Hd, Ad, Hk, Ak, 0));
    set<stat, cmp> vis;
    while(!Q.empty()) {
        auto s = Q.front();
        Q.pop();
        if(vis.find(s) != vis.end())
            continue;
        vis.insert(s);
        if(s.Hd <= 0)
            continue;
        if(true) { // Attack
            auto ns = s;
            ns.turn++;
            ns.Hk -= ns.Ad;
            if(ns.Hk <= 0) {
                printf("%d\n", ns.turn);
                return;
            }
            ns.Hd -= ns.Ak;
            Q.push(ns);
        }
        //if(needHit(s.Ad+B, Hk) < needHit(s.Ad, Hk)) { // Buff
        if(B){
            auto ns = s;
            ns.turn++;
            ns.Ad += B;
            ns.Hd -= ns.Ak;
            Q.push(ns);
        }
        if(s.Hd < Hd-s.Ak) { // cure
            auto ns = s;
            ns.turn++;
            ns.Hd = Hd-ns.Ak;
            Q.push(ns);
        }
        if(s.Ak && D) { // Debuf
            auto ns = s;
            ns.turn++;
            ns.Ak = max(0LL, s.Ak-D);
            ns.Hd -= ns.Ak;
            Q.push(ns);
        }
    }
    puts("IMPOSSIBLE");
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


