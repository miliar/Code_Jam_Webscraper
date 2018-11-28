#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define N 210

struct loli{
    int hidari, migi;
    bool type;
    loli(const int &a=0, const int &b=0, const bool &c=false): hidari(a), migi(b), type(c){}
    bool operator <(const loli &another) const{
        return hidari < another.hidari;
    }
}kitune[N];

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int n, m, t=0;
        scanf("%d%d", &n, &m);
        for(int i=1; i<=n; i++){
            int a, b;
            scanf("%d%d", &a, &b);
            kitune[i] = loli(a, b, false);
        }
        for(int i=n+1; i<=n+m; i++){
            int a, b;
            scanf("%d%d", &a, &b);
            kitune[i] = loli(a, b, true);
            t += b-a;
        }
        n += m;
        sort(kitune+1, kitune+n+1);
        kitune[n+1] = kitune[1];
        kitune[n+1].hidari += 1440;
        kitune[n+1].migi += 1440;
        int ans=0, s=0;
        vector<int> inu, neko;
        for(int i=1; i<=n; i++){
            if(kitune[i].type != kitune[i+1].type){
                ans++;
                s += kitune[i+1].hidari-kitune[i].migi;
            }else{
                if(kitune[i].migi == kitune[i+1].hidari) continue;
                if(kitune[i].type){
                    ans += 2;
                    inu.push_back(kitune[i+1].hidari-kitune[i].migi);
                }else{
                    neko.push_back(kitune[i+1].hidari-kitune[i].migi);
                }
            }
        }
        sort(inu.begin(), inu.end());
        for(int i=0; i<(int)inu.size(); i++){
            t += inu[i];
            if(t <= 720){
                ans -= 2;
            }else break;
        }
        t += s;
        if(t < 720){
            sort(neko.begin(), neko.end());
            for(int i=(int)neko.size()-1; i>=0; i--){
                ans += 2;
                t += neko[i];
                if(t >= 720) break;
            }
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
