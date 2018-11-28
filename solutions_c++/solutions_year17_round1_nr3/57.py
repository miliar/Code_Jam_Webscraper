#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <random>
#include <functional>

using namespace std;

#define F first
#define S second
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)a.size()
#define pw(n) (1ll << (n))

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dbl;
const int Q = 20;


ll divUp(ll A, ll B) {
    return (A + B - 1) / B;
}

int main(){
#ifdef HOME 
    assert(freopen("C.in", "r", stdin));
    freopen("C.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        printf("Case #%d: ", tt + 1);
        ll Hd, Ad, Hk, Ak, B, D;
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

        //if (Ak - D >= Hd) {
            //puts("IMPOSSIBLE");
        //}
        
        ll timeForKill = (Hk + Ad - 1) / Ad;
        for (int i = 0; i < Q; i++) {
            ll power = Ad + B * i;
            timeForKill = min(timeForKill, (Hk + power - 1) / power + i);
        }


        vector<ll> debuffCand; 
        debuffCand.pb(0);
        for (int i = 1; i < 200; i++)
            debuffCand.pb(i);

        if (D > 0) {
            for (int z = 1; z < Q; z++) {
                ll G = divUp(Hd, z);
                ll f = divUp(Ak - G, D);
                if (f > 0)
                    debuffCand.pb(f);
            }
        }

        sort(all(debuffCand));
        //db(debuffCand.size());
        //db(timeForKill);

        ll answer = 1e10;
        //debuffCand.clear();
        //debuffCand.pb(0);
        for (auto cntDebuff: debuffCand) {
            ll usedTurn = 0;  
            ll curHp = Hd;
            ll done = 0;
            ll curDamage = Ak;
            for (; done < cntDebuff; usedTurn++) {
                if (usedTurn > 1e5) {
                    break;
                }
                if (curHp - (curDamage - D) <= 0) {
                    curHp = Hd - curDamage;
                    if (curHp <= 0)
                        break;
                }
                else {
                    done++;
                    curDamage = max(curDamage - D, 0ll);
                    curHp -= curDamage;
                }
            }

            if (done == cntDebuff) {
                int i;
                //db2(curHp, curDamage);
                for (i = 0; i < timeForKill; usedTurn++) {
                    if (usedTurn > 1e5)
                        break;
                    if (curHp - curDamage <= 0 && i + 1 != timeForKill) {
                        curHp = Hd - curDamage;
                        if (curHp <= 0)
                            break;
                    }
                    else {
                        i++;
                        curHp -= curDamage;
                    }
                }

                if (i == timeForKill)
                    answer = min(answer, usedTurn);
            } 
        }
        if (answer > INF)
            puts("IMPOSSIBLE");
        else
            cout << answer << endl;
    }
    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

