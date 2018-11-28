#include <bits/stdc++.h>
using namespace std;

const int64_t inf = 1e18;
int64_t calc(int64_t att, int64_t buff, int64_t enehp){
    int64_t ans = inf;
    for(int64_t i=0;(i-1)<=4*enehp;++i){
        ans = min(ans, i + 1+(enehp-1)/(att+i*buff));
    }
    return ans;
}

int64_t simulate(int64_t hp2, int64_t eneat, int64_t debuff, int64_t i, int64_t enehp, int64_t atk, int64_t bless_cnt){
    assert(hp2>0&&eneat>=0&&debuff>=0 && i>=0 && enehp>0 && atk>0);
    int64_t hp = hp2;
    for(int64_t it=0;it<1e3;++it){
        assert(enehp>0);
        if(hp<=0) break;
        if(!bless_cnt && enehp<=atk) return it+1;
        if(i){
            if(hp>eneat-debuff){
                --i;
                eneat-=debuff;
                eneat = max(eneat, 0ll);
            } else {
                hp = hp2;
            }
        } else {
            if(hp>eneat){
                if(bless_cnt){
                    --bless_cnt;
                } else {
                    enehp-=atk;
                }
            } else {
                hp=hp2;
            }
        }
        hp-=eneat;
    }
    return inf;

}
int main()
{
    freopen("inC.txt", "r", stdin);
    freopen("outC.txt", "w", stdout);
    cin.tie(0);ios_base::sync_with_stdio(false);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";

        int64_t hp, atk, enehp, eneat, buff, debuff;
        cin >> hp >> atk >> enehp >> eneat >> buff >> debuff;

        int64_t out = inf;
        for(int bless_cnt=0;bless_cnt<=enehp;++bless_cnt){
            for(int i=0;i<=eneat;++i){
                int64_t tmp = simulate(hp, eneat, debuff, i, enehp, atk+ bless_cnt*buff, bless_cnt);
                if(tmp < out){
                    out = tmp;
                    //cerr << bless_cnt << " / " << i << " : " << tmp << "\n";
                }
            }
        }

        if(out == inf){
            cout << "IMPOSSIBLE";
        } else {
            cout << out;
        }
        cerr << out << "\n";



        cout << "\n";
    }


    return 0;
}

